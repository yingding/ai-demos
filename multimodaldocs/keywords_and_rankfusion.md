## BM25 (Best Matching 25)
BM25 is a ranking function used by search engines to determine how relevant a document is to a given search query. It is part of the probabilistic information retrieval model and works by considering several factors:
1. Term Frequency (TF): This measures how often a query term appears in a document. The more frequently a term appears, the more relevant the document is considered to be.
2. Document Length: BM25 adjusts for the length of the document to prevent longer documents from being overly favored. It normalizes the term frequency by the document length.
3. Inverse Document Frequency (IDF): This measures how common or rare a term is across all documents. Rare terms are given more weight because they are more likely to be significant.

BM25 uses two key parameters, $k1$ and $b$ to control term frequency saturation and length normalization, respectively. These parameters help fine-tune the ranking function to improve search relevance.

## Reciprocal Rank Fusion (RRF)
RRF is a method used to combine the results of multiple search algorithms or ranking systems. It is a data fusion technique that focuses on the rank of a document in different result sets rather than its score.

Here's how RRF works:
1. Rank-Based: RRF looks at the rank of a document in different result sets. For example, if you have two different search algorithms, each producing a ranked list of documents, RRF will consider the position of each document in these lists.
2. Reciprocal Rank Score: RRF assigns a score to each document based on its rank in the result sets. The score is calculated using the formula $$
\text{RRF\_score} = \sum_{i=1}^{n} \frac{1}{k + \text{rank}_i}
​$$, Where:
    * $RRF_score$ is the combined Reciprocal Rank Score.
    * $n$ is the number of different ranking lists.
    * $k$ is a constant (usually a small value like 60).
    * $rank_i$ is the rank of the document in the $i$-th ranking list.

3. Combining Ranks: The RRF score for a document is the sum of its reciprocal rank scores from different result sets. This combined score is used to produce a unified ranking.

**Example** 

Imagine you have two search algorithms:
* Algorithm **A** ranks documents based on keyword matching.
* Algorithm **B** ranks documents based on semantic similarity.

For a given query, Algorithm A might rank Document X as 1st and Document Y as 2nd, while Algorithm B might rank Document Y as 1st and Document X as 3rd. RRF will combine these rankings to produce a final ranking that considers both **keyword matching** and **semantic similarity**.

**Why Use BM25 and RRF?**
* BM25 is great for traditional keyword-based search, providing a relevance score based on term frequency and document length.
* RRF is useful when you have multiple ranking methods and want to combine their strengths to produce a more accurate and reliable final ranking.

By using BM25 or RRF, Azure AI Search ensures that the initial ranking of search results is both relevant and comprehensive, leveraging different aspects of the documents and queries to provide the best possible results.


