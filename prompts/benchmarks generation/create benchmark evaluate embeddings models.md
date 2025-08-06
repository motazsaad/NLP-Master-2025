# Create benchmark dataset to evaluate embeddings models

## Embedding Models in the Context of Retrieval-Augmented Generation (RAG)

Embedding models are a crucial component in Retrieval-Augmented Generation (RAG) systems. These models convert text into dense vector representations (embeddings) that capture semantic meaning. In RAG, embedding models serve two primary purposes:

1. **Retrieval**: Embedding models are used to encode both queries and documents into vectors. The similarity between these vectors (often computed using cosine similarity) helps in retrieving the most relevant documents for a given query.

2. **Generation**: After retrieving relevant documents, embedding models can also be used to encode the context for generative models. This context helps the generative model produce more accurate and contextually relevant responses.

By leveraging embedding models, RAG systems can effectively combine the strengths of retrieval-based and generation-based approaches, leading to more accurate and informative outputs.

Evaluating different embedding models is crucial for several reasons, especially when focusing on a specific language like Italian and a specialized domain such as Environmental, Social, and Governance (ESG). Here are the key reasons:

1. **Language Specificity**:
   - Embedding models trained on general datasets may not capture the nuances of the Italian language effectively. Evaluating models ensures that the chosen model handles Italian syntax, semantics, and idiomatic expressions accurately.

2. **Domain Relevance**:
   - ESG is a specialized domain with its own terminology and context. General-purpose embedding models might not perform well in capturing the specific vocabulary and concepts related to ESG. Evaluating models helps in identifying those that are better suited for this domain.

3. **Performance Metrics**:
   - Different embedding models can be compared using various performance metrics such as accuracy, precision, recall, and F1-score. This helps in quantifying how well each model performs in tasks relevant to the Italian language and ESG domain.

4. **Task-Specific Evaluation**:
   - Embedding models can be evaluated based on specific tasks such as text classification, sentiment analysis, or information retrieval. This ensures that the model chosen excels in the particular tasks that are important for your project.

5. **Adaptability and Fine-Tuning**:
   - Some models might be more adaptable and easier to fine-tune for the Italian language and ESG domain. Evaluating different models helps in identifying those that can be fine-tuned with minimal effort and maximum effectiveness.

6. **Resource Efficiency**:
   - Evaluating models also involves considering computational resources and efficiency. Some models might provide a good balance between performance and resource consumption, making them more suitable for practical applications.

By systematically evaluating different embedding models, you can determine the best one that meets the specific requirements of the Italian language and ESG domain, ensuring higher accuracy and relevance in your applications.


## Use LLMs to create a benchmark dataset for search relevance in the domain of interest

## Generation Prompts 

### All in a single prompt 

```prompt
Generate [number] search queries in the [Lang] language related to the [domain] domain. Each query should belong to one of the following categories:

For each generated query, create three documents in [Lang] language, categorized as follows:
- Relevant document (label: "relevant") – A document that directly and comprehensively addresses the query.
- Somewhat relevant document (label: "somewhat relevant") – A document that touches on related concepts but lacks full relevance.
- Irrelevant document (label: "irrelevant") – A document that is unrelated to the query.

Ensure the output is formatted in valid JSON with the following structure, including the domain information
```

Expected JSON Output:
```JSON
{
  "benchmark": [
    {
      "index": 1,
      "query": "Query text.",
      "documents": [
        {
          "text": "Highly relevant document text.", 
          "relevance": 3, 
          "label": "relevant"
        },
        {
          "text": "somewhat relevant text.", 
          "relevance": 2, 
          "label": "somewhat relevant"
        },
        {
          "text": "irrelevant text.", 
          "relevance": 0, 
          "label": "irrelevant"
        }
      ]
    },
    {
        
      "index": 2,
      "query": "Query text.",
      "documents": [
        {
          "text": "Highly relevant document text.", 
          "relevance": 3, 
          "label": "relevant"
        },
        {
          "text": "somewhat relevant text.", 
          "relevance": 2, 
          "label": "somewhat relevant"
        },
        {
          "text": "irrelevant text.", 
          "relevance": 0, 
          "label": "irrelevant"
        }
      ]
    }
  ]
}
```

### Two prompts 

You can split the task into two sub tasks 

#### Task1: Generate Queries 

```prompt 
Generate [number] search queries in the [Lang] language related to the [domain] domain
```

#### Task2: documents for earch query 

Loop over queries and submit the following prompt: 

```prompt 
For the query "[query]", create three documents in [Lang] language, categorized as follows:
- Relevant document (label: "relevant") – A document that directly and comprehensively addresses the query.
- Somewhat relevant document (label: "somewhat relevant") – A document that touches on related concepts but lacks full relevance.
- Irrelevant document (label: "irrelevant") – A document that is unrelated to the query.

Ensure the output is formatted in valid JSON with the following structure, including the domain information
```

Expected JSON Output:
```JSON
{
  "benchmark": [
    {
      "index": 1,
      "query": "Query text.",
      "documents": [
        {
          "text": "Highly relevant document text.", 
          "relevance": 3, 
          "label": "relevant"
        },
        {
          "text": "somewhat relevant text.", 
          "relevance": 2, 
          "label": "somewhat relevant"
        },
        {
          "text": "irrelevant text.", 
          "relevance": 0, 
          "label": "irrelevant"
        }
      ]
    },
    {
        
      "index": 2,
      "query": "Query text.",
      "documents": [
        {
          "text": "Highly relevant document text.", 
          "relevance": 3, 
          "label": "relevant"
        },
        {
          "text": "somewhat relevant text.", 
          "relevance": 2, 
          "label": "somewhat relevant"
        },
        {
          "text": "irrelevant text.", 
          "relevance": 0, 
          "label": "irrelevant"
        }
      ]
    }
  ]
}
```




---

## Quality Assurance

Perform a review of labels to check for consistency and accuracy.


----

## Evaluat metrics 

​In information retrieval, evaluating the effectiveness of search and recommendation systems is crucial. Two commonly used metrics are Precision and Normalized Discounted Cumulative Gain (NDCG).

### Precision
Precision measures the proportion of retrieved items that are relevant to the user's query. It is calculated as the number of relevant items retrieved divided by the total number of items retrieved. Precision focuses solely on the relevance of the retrieved items, not their order.​

For example, if a search system returns 10 documents, out of which 7 are relevant, the precision is 0.7 or 70%.​

### Normalized Discounted Cumulative Gain (NDCG)
NDCG evaluates the quality of the ranking of retrieved items by considering both the relevance and the position of each item in the result list. The premise is that highly relevant documents appearing earlier in the search results should be weighted more heavily than those appearing later.​


By utilizing these metrics, you can objectively assess and compare the performance of different information retrieval systems.


Reference: [Evaluation Metrics for Search and Recommendation Systems](https://weaviate.io/blog/retrieval-evaluation-metrics)

## Code 

The code below loads a benchmark dataset, applies an embedding model, computes cosine similarity, and evaluates the embeddings using NDCG and precision metrics. Let me know if you'd like assistance in running or modifying this code!


```python
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import ndcg_score, precision_score
from transformers import AutoTokenizer, AutoModel
import torch

# Load benchmark dataset
def load_dataset(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# Load embedding model
def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    return tokenizer, model

# Generate embeddings
def generate_embeddings(texts, tokenizer, model):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)  # Mean pooling
    return embeddings

# Evaluate embeddings
def evaluate_embeddings(benchmark_data, tokenizer, model):
    results = []

    for entry in benchmark_data:
        query = entry['query']
        documents = entry['documents']
        doc_texts = [doc['text'] for doc in documents]
        relevance_scores = [doc['relevance'] for doc in documents]

        # Generate embeddings for query and documents
        query_embedding = generate_embeddings([query], tokenizer, model).numpy()
        doc_embeddings = generate_embeddings(doc_texts, tokenizer, model).numpy()

        # Compute cosine similarity
        similarities = cosine_similarity(query_embedding, doc_embeddings).flatten()

        # Compute evaluation metrics
        ndcg = ndcg_score([relevance_scores], [similarities])
        precision = precision_score(
            [1 if score > 1 else 0 for score in relevance_scores],
            [1 if sim > 0.5 else 0 for sim in similarities]
        )

        results.append({
            'query': query,
            'ndcg': ndcg,
            'precision': precision
        })

    return results

# Main function
def main():
    # Load benchmark dataset
    benchmark_file = "benchmark_data.json"  # Replace with your dataset path
    benchmark_data = load_dataset(benchmark_file)

    # Load embedding model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"  # Replace with your model
    tokenizer, model = load_model(model_name)

    # Evaluate embeddings
    results = evaluate_embeddings(benchmark_data, tokenizer, model)

    # Output results
    for result in results:
        print(f"Query: {result['query']}")
        print(f"NDCG: {result['ndcg']:.4f}")
        print(f"Precision: {result['precision']:.4f}\n")

if __name__ == "__main__":
    main()

```
