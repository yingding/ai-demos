# Intro

repository and demo folder for multi model document intelligence

## Reference
* ARGUS (vision ai based content extraction) https://github.com/azure-samples/ARGUS#
* content extraction solution accelerator https://github.com/microsoft/content-processing-solution-accelerator
* Azure Multimodal AI and LLM solution accelerator https://github.com/Azure/multimodal-ai-llm-processing-accelerator?tab=readme-ov-file#azure-multimodal-ai--llm-processing-accelerator
* Azure Content Understanding https://github.com/retkowsky/azure-content-understanding/blob/main/README.md
* Conversation Knowledge Mining Solution Accelerator https://github.com/microsoft/Conversation-Knowledge-Mining-Solution-Accelerator/tree/main?tab=readme-ov-file#conversation-knowledge-mining-solution-accelerator
* Azure AI Document Processing Samples Collection (important) https://github.com/Azure-Samples/azure-ai-document-processing-samples
* Multi modal Vision embedding https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-vision-vectorize

* Azure AI Search with Multi modal Embedding https://techcommunity.microsoft.com/blog/azure-ai-services-blog/azure-ai-search-now-supports-ai-vision-multimodal-and-ai-studio-embedding-models/4136743
* Semantic Rerank with Language Understanding Model in Azure AI Search https://learn.microsoft.com/en-us/azure/search/semantic-search-overview
* Azure AI Search (General Doc) https://learn.microsoft.com/en-us/azure/search/
* Semantic Answer in Azure AI Search https://learn.microsoft.com/en-us/azure/search/semantic-answers
* Content Understanding https://learn.microsoft.com/en-gb/azure/ai-services/content-understanding/overview
* Content Understanding project in Azure AI Foundry https://learn.microsoft.com/en-gb/azure/ai-services/content-understanding/quickstart/use-ai-foundry#analyzer-templates

## How Semantic Ranking Works

* Initial Ranking: The search results are initially ranked using BM25 or Reciprocal Rank Fusion (RRF) [(BM25, RRF)](./keywords_and_rankfusion.md)
* Secondary Ranking: Semantic ranker applies a secondary ranking using deep learning models to promote the most semantically relevant results
* Captions and Answers: The ranker can return semantic captions and optionally extract answers to improve the user's search experience [(Captions, Answers)](./caption_answer.md)
* Query Rewrite: It can expand an initial query string into multiple semantically similar queries, correcting typos or rephrasing the query 
