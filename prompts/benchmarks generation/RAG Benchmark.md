# Evaluating a Retrieval-Augmented Generation (RAG) system

Evaluating a Retrieval-Augmented Generation (RAG) system for KPI extraction in the ESG (Environmental, Social, and Governance) domain requires a mix of retrieval, generation, and domain-specific metrics. Here’s a structured approach to evaluating such a system:

## Evaluation Framework

A RAG-based KPI extraction system consists of two major components:

1. Retriever: Finds relevant documents or passages containing ESG KPIs.
2. Generator (LLM): Extracts and generates structured KPI information.

To evaluate the system, we need to assess both retrieval and generation performance.

## Metrics for Evaluation

### Retrieval Evaluation Metrics

These metrics measure how well the retriever finds relevant ESG-related text that contains KPI information.

* Recall@K: Measures whether the relevant document is retrieved in the top K results.
* Mean Reciprocal Rank (MRR): Evaluates the rank of the first relevant document.
* Normalized Discounted Cumulative Gain (nDCG): Measures ranking quality, giving higher weight to relevant documents appearing earlier in the ranking.
* Precision@K: Measures how many of the top K retrieved documents are relevant.

### KPI Extraction (Generation) Evaluation Metrics

These metrics assess how well the system extracts ESG KPIs from retrieved texts.

* Exact Match (EM) Score: Measures whether the extracted KPI exactly matches the ground truth.
* F1 Score: Measures the overlap between extracted and ground-truth KPIs.
* BLEU Score: Measures how closely the extracted KPI text matches the reference text.
* ROUGE Score: Evaluates how much of the ground truth KPI is present in the extracted text.
* Mean Average Precision (MAP): Measures ranking quality for extracted KPIs.

### Domain-Specific ESG Evaluation Metrics

Since KPI extraction is domain-sensitive, additional ESG-specific validation is needed.
* Coverage of ESG Frameworks: Measures whether extracted KPIs align with standard ESG frameworks (e.g., GRI, ESRS, SASB, TCFD).
* Consistency Score: Evaluates whether the extracted KPIs are logically consistent with previous reports or regulatory guidelines.
* Relevance Score (Human Evaluation): Experts rate the extracted KPIs on a scale (e.g., 1-5 based on relevance to ESG reporting).
* Accuracy of Numerical Values: If extracting numerical KPIs (e.g., carbon emissions, workforce diversity %), check against ground truth.

### Hallucination Detection
* Faithfulness Score: Measures whether the extracted KPI is grounded in the retrieved text (e.g., using QA-F1 or LlamaIndex FactScore).
* Contradiction Detection: Ensures the extracted KPI does not contradict known ESG facts.

## Automated vs. Human Evaluation
* Automated Metrics: Use retrieval and generation metrics to measure system performance quantitatively.
* Human Evaluation: Experts validate whether extracted KPIs are relevant, consistent, and complete.

## Benchmarking

Compare your RAG system’s performance against:
* Rule-based ESG KPI extractors
* Traditional NLP pipelines (NER, Regex)
* Fully supervised deep learning models

## Conclusion

To evaluate a RAG-based KPI extraction system in ESG, focus on:

1. Retrieval Performance (Recall@K, nDCG, MRR)
2. Extraction Accuracy (F1, BLEU, ROUGE)
3. Domain-Specific Validation (ESG framework coverage, numerical accuracy)
4. Hallucination Detection (Faithfulness, Contradiction Checks)
5. Human Assessment (Relevance, Completeness)

---

## Creating a benchmark dataset for evaluating KPI extraction (generation)

Creating a benchmark dataset for evaluating KPI extraction (generation) in the ESG domain involves several key steps. The goal is to build a high-quality dataset with annotated ground truth KPIs extracted from ESG reports, sustainability disclosures, and regulatory documents.

### Define Benchmarking Objectives

Your benchmark dataset should:
* Contain text passages from ESG reports where KPIs are explicitly mentioned.
* Include ground truth KPI values and their categories (e.g., environmental, social, governance).
* Support evaluation using automatic metrics (F1, BLEU, ROUGE, etc.) and human review.
* Align with established ESG standards (GRI, ESRS, SASB, TCFD, IFRS).

### Data Collection

#### Source ESG Reports
* Download public ESG reports from:
* Corporate Websites (e.g., Tesla, Unilever, Microsoft)
* Regulatory Bodies (e.g., GRI Database, SEC Filings)
* Sustainability Databases (e.g., CDP, Refinitiv, MSCI)

#### Select KPI Categories

Define which KPI categories you want to extract:
* Environmental: CO₂ emissions, energy consumption, waste reduction.
* Social: Workforce diversity, employee turnover, community investments.
* Governance: Board diversity, executive compensation, audit independence.

#### Extract Text Passages
* Identify paragraphs or tables containing KPIs.
* Store the raw text along with metadata (company name, year, report section).

### Annotate KPI Ground Truth

To evaluate KPI extraction, you need ground truth annotations.

#### Manual Annotation
* Have ESG experts or trained annotators label KPI mentions in reports.
* Annotate:
 * KPI Name (e.g., “Carbon Emissions”)
 * KPI Value (e.g., “2.3 metric tons per employee”)
 * Unit of Measurement (e.g., “metric tons”)
 * Source Sentence (text snippet where KPI appears)
 * KPI Category (E, S, or G)

Example Annotation Format

| ID  | Company | Year | KPI Name            | KPI Value | Unit        | Source Text Snippet                                    | Category |
|-----|---------|------|---------------------|-----------|-------------|-------------------------------------------------------|----------|
| 001 | Tesla   | 2023 | Carbon Emissions    | 2.3       | metric tons | "Tesla reported 2.3 metric tons per employee."        | E        |
| 002 | Unilever| 2022 | Workforce Diversity | 45%       | percentage  | "Unilever's workforce is 45% female."                 | S        |


#### Automated Pre-Annotation (Optional)

To speed up manual labeling:
* Use NER models (e.g., spaCy, Hugging Face transformers) to detect KPI mentions.
* Apply regex patterns for numbers and units.
* Use LLMs (GPT, Llama, Claude) to pre-extract KPIs and refine them manually.

### Data Structuring & Formatting

A. JSON Format (for NLP Pipelines)

Structure data in JSON for easy ingestion into RAG models.

```JSON
{
  "id": "001",
  "company": "Tesla",
  "year": 2023,
  "kpi_name": "Carbon Emissions",
  "kpi_value": 2.3,
  "unit": "metric tons",
  "source_text": "Tesla reported 2.3 metric tons per employee.",
  "category": "E"
}
```

B. Table Format (for Evaluation Pipelines)

For comparing extracted vs. ground truth values.

| Model Output                         | Ground Truth                       | Match?        |
|--------------------------------------|------------------------------------|---------------|
| 2.3 metric tons per employee         | 2.3 metric tons per employee       | ✔️ Exact Match |
| Tesla's emissions are 2.3 tons       | 2.3 metric tons per employee       | ❌ Partial Match |

---

### Evaluation Strategy

Once the dataset is created, use it to benchmark KPI extraction.

A. Automatic Metrics
* Exact Match (EM): Checks if extracted KPI matches ground truth exactly.
* F1 Score: Measures overlap between extracted and true KPI values.
* BLEU / ROUGE: Evaluates text similarity between extracted and reference KPI text.

B. Human Evaluation
* Relevance Score (1-5 scale): Does the extracted KPI match ESG context?
* Completeness Score: Is any important KPI missing?
* Faithfulness Check: Is extracted KPI grounded in source text?

### Benchmark Dataset Release

Once validated, release the dataset as:
* Public dataset on Hugging Face Datasets / Kaggle.
* Benchmark leaderboard for KPI extraction models.

---

