from typing import Any, Dict, Self 
import requests
import re
import numpy as np


class EmbedResult:
    def __init__(self, result: Dict[str, Any]):
        self.model_version = self.from_result(result, "modelVersion")
        self.vector = self.from_result(result, "vector")
        self.error = self.from_result(result, "error")
        self.size = len(self.vector)

    @classmethod
    def cosine_similarity(cls, vector1, vector2):
        np_float = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        # convert np_float to python float
        return float(np_float)
    
    # class methods to get the vector, model version and error message
    @classmethod
    def from_result(cls, result: Dict[str, Any], key: str = None):
        """Get the key from the input dict."""
        if isinstance(result, dict) and key in result:
            return result[key]
        return None
    
    def relevance_score(self, emb_result: "EmbedResult") -> float:
        """Calculate the relevance score between two embedding results."""
        if not isinstance(emb_result, EmbedResult):
            raise TypeError("Input must be an instance of EmbedResult")
        
        # check if the vectors are of the same length
        if self.size != emb_result.size:
            raise ValueError("Vectors must be of the same length")
        
        return self.cosine_similarity(self.vector, emb_result.vector)
    
    # repr method also print the []
    # def __repr__(self):
    #     return f"EmbedResult(model_version={self.model_version}, vector=[{repr(self.vector[:3])},...], size={self.size}, error={self.error})"
    
    def __repr__(self):
        return f"EmbedResult(model_version={self.model_version}, vector=[{",".join(list(map(str, self.vector[:3])))},...], size={self.size}, error={self.error})"


class EmbedBase:
    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.endpoint = config.get("AZURE_COMPUTER_VISION_ENDPOINT", None)
        self.key = config.get("AZURE_COMPUTER_VISION_KEY", None)  
        self.apiversion = config.get("API_VERSION", None) # 2024-02-01
        self.modelversion = config.get("MODEL_VERSION", None) # 2023-04-15

    def embed(self, input: Any):
        raise NotImplementedError("Subclasses should implement this method")
    
    def gen_data(self, input: Any) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses should implement this method")
    
    def _get_endpoint(self, svc_str):
        # endpoint already has https:// and /computervision/retrieval
        return f"{self.endpoint}/computervision/retrieval:{svc_str}?api-version={self.apiversion}&model-version={self.modelversion}"
    
    def _gen_headers(self):
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.key,
            # "api-version": self.apiversion,
            # "model-version": self.modelversion
        }
        return headers
    
    def _post(self, endpoint, headers, data):
        # Make the POST request
        response = requests.post(endpoint, headers=headers, json=data)

        # Check for HTTP errors
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} - {response.text}")
        else:
            return response.json()
        
    def _embed(self, input: Any):
        headers = self._gen_headers()
        data = self.gen_data(input)
        return self._post(self.image_endpoint, headers, data)
          
    def embed(self, input: Any) -> str:
        """Embed the image or text using the specified service."""
        result: Dict = self._embed(input)
        return EmbedResult(result)
        
    
class EmbedImage(EmbedBase):
    """
    The file size of the image must be less than 20 megabytes (MB)
    The dimensions of the image must be greater than 10 x 10 pixels and less than 16,000 x 16,000 pixels
    https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-image-retrieval#input-requirements
    """
    def __init__(self, config):
        super().__init__(config)
        self.service = "vectorizeImage"
        self.image_endpoint = self._get_endpoint(self.service)

    def gen_data(self, input: Any) -> Dict[str, str]:
        """Generate the data payload for the image embedding request."""
        if not isinstance(input, str):
            raise TypeError("Input must be a string representing a URL")
        
        # Validate that the input is a valid HTTPS URL
        url_pattern = re.compile(r'^https://[^\s]+$')
        if not url_pattern.match(input):
            raise ValueError("Input must be a valid HTTPS URL")
        
        return {"url": input}


class EmbedText(EmbedBase):
    """
    The text string must be between (inclusive) one word and 70 words.
    https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-image-retrieval#input-requirements
    """
    def __init__(self, config):
        super().__init__(config)
        self.service = "vectorizeText"
        self.image_endpoint = self._get_endpoint(self.service)

    def gen_data(self, input: Any) -> Dict[str, str]:
        """Generate the data payload for the text embedding request."""
        if not isinstance(input, str):
            raise TypeError("Input must be a string representing a text")
        
        # check the length of the input string between 1 and 70 words
        word_count = len(input.split())
        if word_count < 1 or word_count > 70:
            raise ValueError("Input must be between 1 and 70 words")
              
        return {"text": input}