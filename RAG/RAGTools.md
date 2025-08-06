# RAG tools 

There are open-source RAG tools that you can use without heavy coding, or even no coding at all!. Here are the best options you can start with:

## LlamaIndex / LlamaParse
LlamaIndex provides a no-code interface (with LlamaParse) to upload documents and query them using LLMs with RAG.

Good for: Uploading PDFs or Word files, automatically parsing them, building a RAG app easily.

### How:

1. Go to LlamaParse
2. Upload your documents.
3. Ask questions like: "Extract all .........", and get answers.

Note: LlamaParse is free up to a certain limit. You can integrate it later with your own LLM if you want full control.

https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/

https://docs.cloud.llamaindex.ai/llamacloud/getting_started/quick_start


--- 

## Flowise AI
Flowise is a visual builder for LLM apps, including RAG. It’s drag-and-drop, no real coding needed.

Good for: Build customized RAG workflows visually (like building a flowchart).

### How:
1. Install Flowise locally or use a hosted version.
2. Connect document loaders, embeddings, LLMs, all visually.

https://github.com/FlowiseAI/Flowise 

### 2024 YT flowise AI playlist 
https://youtube.com/playlist?list=PL4HikwTaYE0H7wBxhvQqxYcKOkZ4O3zXh&si=zxsZs8oFEdp42oHk

### 2025 YT flowise AI playlist 
https://www.youtube.com/playlist?list=PL4HikwTaYE0Gi60Xkc1VAZV6u1vrJiZLr

--- 

### N8N 

Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. 

https://github.com/n8n-io/n8n


---


# Vector databases that offer free tiers

## 🟢 Qdrant

- **Free Tier**: 1GB free cluster, no credit card required.
- **Features**:
  - Fully managed cloud service
  - Supports horizontal and vertical scaling
  - High availability with auto-healing
  - Backup and disaster recovery
- **Use Cases**: Semantic search, recommendation systems, AI-driven search functionalities
- **Reference**: [qdrant.tech](https://qdrant.tech/pricing/)

---

## 🟡 Weaviate

- **Free Tier**: 14-day sandbox access for learning and prototyping.
- **Features**:
  - Serverless SaaS deployment
  - Hybrid search (vector + keyword)
  - Schema-less data ingestion
  - Built-in machine learning modules
- **Use Cases**: Semantic search engines, contextual understanding applications
- **Reference**: [weaviate.io](https://weaviate.io/deployment/serverless)

---

## 🔵 Pinecone

- **Free Tier**: Includes community support and documentation access.
- **Features**:
  - Fully managed with automatic scaling
  - Low-latency vector search
  - Up to 2M write units and 1M read units/month
- **Use Cases**: Managed vector similarity search without infrastructure overhead
- **Reference**: [pinecone.io](https://www.pinecone.io/pricing/)

---

## 🟣 Chroma

- **Free Tier**: Open-source under Apache 2.0 License. Chroma Cloud provides $5 free credits.
- **Features**:
  - Optimized for LLM-based applications
  - Supports embedding storage and RAG
- **Use Cases**: Embedding storage and retrieval for LLM-based apps
- **Reference**: [trychroma.com](https://www.trychroma.com/)

---

## 🔴 Milvus

- **Free Tier**: Open-source and free to use.
- **Features**:
  - Handles billion-scale vector data
  - GPU acceleration
  - Multiple indexing options
- **Use Cases**: High-performance similarity search at large scale
- **Reference**: [milvus.io](https://milvus.io/)


