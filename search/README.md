# Azure AI Search

[Multimodal Search with Azure AI Search](./multimodal_search.md)

## References

### Hybrid Search
* Hybrid Search Overview https://learn.microsoft.com/en-gb/azure/search/hybrid-search-overview
* Python example https://github.com/Azure/azure-search-vector-samples/blob/main/README.md

* RAG in Azure AI Search https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview
* Skillset in Azure AI Search https://learn.microsoft.com/en-us/azure/search/cognitive-search-working-with-skillsets
* AI enrichment in Azure AI Search https://learn.microsoft.com/en-us/azure/search/cognitive-search-concept-intro

* vison-enabled chat models https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/gpt-with-vision?tabs=rest 


### Unstructured Data to Structured Data
* Content Understanding https://learn.microsoft.com/en-gb/azure/ai-services/content-understanding/overview

### Models
* OpenAI Serivce models https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions

### Azure AI Agent Service
* https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357

## Multi-modal search
* AI Vision multimodal embeddings https://learn.microsoft.com/en-us/azure/search/cognitive-search-skill-vision-vectorize
* Azure AI Vision multimodal embedding https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/image-retrieval?tabs=csharp
* Region availability https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-image-analysis?tabs=4-0#region-availability

* Auto Indexing with Indexer (Azure AI Search) https://learn.microsoft.com/en-us/azure/search/vector-search-overview#azure-integration-and-related-services

### Code examples of Vector Search
* examples https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/search/azure-search-documents/samples
* Vector Search examples https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_vector_search.py
* Indexing with Indexer https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_indexers_operations.py
* Azure AI Search Client Python SDK https://learn.microsoft.com/en-us/python/api/overview/azure/search-documents-readme?view=azure-python
* Vectors in Azure AI Search (Important) https://learn.microsoft.com/en-gb/azure/search/vector-search-overview#nearest-neighbors-search

### Python
* Self typing https://realpython.com/python-type-self/

### Semantic Ranker
* Attach Semantic Ranker Configuration to the index and use the Semantic Ranker to rerank the initial search results (important python sample) https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/semantic-ranker/semantic-ranker.ipynb
* Keyword and Vector Search simple Hybrid https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/search/azure-search-documents/samples/sample_vector_search.py#L175

### Scoring profile
how search scoring works in Azure AI Search https://learn.microsoft.com/en-us/azure/search/index-add-scoring-profiles#how-search-scoring-works-in-azure-ai-search

1. Scoring Profiles
Scoring profiles allow you to boost search scores based on custom parameters, such as field values, freshness, or geographic proximity. You define these profiles within your index schema.
    * Use Case: Boosting recent documents, prioritizing certain categories, or emphasizing geographic proximity.
    * Documentation: [Add scoring profiles - Azure AI Search](https://learn.microsoft.com/en-us/azure/search/index-add-scoring-profiles)

2. Semantic Ranking
Semantic ranking uses advanced language understanding models to rerank search results based on semantic relevance. It significantly improves the relevance of results by understanding the intent behind queries.   
    * Use Case: Improving relevance in natural language queries, hybrid searches, and vector searches.
    * Documentation: [Semantic ranking overview](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview)