## Introduction of Multimodal embedding and search

Azure AI Search supports multimodal embedding and search by leveraging Azure AI Vision's multimodal embeddings API. This enables you to vectorize both images and text into a shared embedding space, allowing semantic search across different modalities.

Here's a detailed step-by-step guide on how you can implement multimodal embedding and search:

### **1. What is Multimodal Embedding?**
Multimodal embedding involves generating vector representations for multiple types of data (e.g., images and text) in a shared vector space. This allows semantic similarity searches across different data types, such as searching images using text queries or vice versa.

### **2. Azure AI Vision Multimodal Embeddings Skill**
Azure AI Search provides a built-in cognitive skill called **Azure AI Vision Multimodal Embeddings Skill**, which generates embeddings for both images and text.

### **2. How to Implement Multimodal Embedding with Azure AI Search**

| **Step** | **Description** | **Details** | **Documentation** |
|----------|-----------------|-------------|-------------------|
| 1 | **Provision Azure AI Vision and Azure AI Search** | Create Azure AI Vision and Azure AI Search resources in supported regions. | [Azure AI Vision multimodal embeddings skill](https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-vision-vectorize) |
| 2 | **Create a Skillset** | Define a skillset in Azure AI Search using the multimodal embeddings skill from Azure AI Vision. | [Multimodal Embeddings Skill](https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-vision-vectorize) |
| 3 | **Define Index Schema** | Create an index schema that includes vector fields for multimodal embeddings. | [Create Vector Index](https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-create-index) |
| 4 | **Index Data** | Use an indexer to process your images and text, generating embeddings via Azure AI Vision. | [Indexer Overview](https://learn.microsoft.com/en-us/azure/search/search-indexer-overview) |
| 4 | **Perform Multimodal Search** | Query the index using text or image embeddings to retrieve semantically similar content. | [Vector Search Overview](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) |

### **3. Example Implementation (Python)**
see the code examples in this repo

### **4. Benefits of Multimodal Search with Azure AI Search**
- **Semantic Matching**: Match images and text based on semantic similarity.
- **Hybrid Search**: Combine keyword and vector-based searches in a single query.
- **Scalability**: Efficiently handle large-scale multimodal datasets.

### **Documentation References:**
- [Azure AI Vision Multimodal Embeddings Skill](https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-vision-vectorize)
- [Multimodal Embeddings Concepts](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-image-retrieval)
- [Vector Search Overview](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)
