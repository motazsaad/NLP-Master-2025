# Generate the benchmark data for RAG

You can generate benchmark data for KPI extraction in the ESG domain instead of collecting it manually. This is particularly useful if real ESG reports are scarce or if you want a controlled dataset for testing RAG models. Below are different approaches to generating such data.


## Approaches to Generating ESG KPI Benchmark Data
A. Synthetic Data Generation with LLMs (GPT, Llama, Claude)

* Use LLMs to create realistic ESG reports containing KPIs.
* Define company names, industries, and standard ESG KPIs.
* Ensure outputs follow real ESG reporting standards (GRI, ESRS, SASB, etc.).

Example Prompt for Generating ESG Reports

```Prompt
Generate a corporate ESG report for a technology company in 2023. 
Include sections on Environmental, Social, and Governance performance. 
Report at least five KPIs per section, specifying the metric, unit, and a brief analysis.
Ensure the report follows Global Reporting Initiative (GRI) standards.
```

Generated Output Example

```plaintext
Company: TechCorp  
Year: 2023  

**Environmental KPIs:**  
- Carbon Emissions: 4.2 metric tons CO₂ per employee  
- Energy Consumption: 12,500 MWh (100% renewable sources)  

**Social KPIs:**  
- Workforce Diversity: 40% female employees  
- Employee Training Hours: 35 hours per employee per year  

**Governance KPIs:**  
- Board Diversity: 30% women on the board  
- Data Privacy Incidents: 2 reported breaches  
```

#### improved prompt 

```Prompt
Generate a corporate ESG report for a company in the {SECTOR} sector for the year {YEAR}. The report should be approximately {WORD_COUNT} words and follow a structured format.

**Company Overview**  
Provide a brief introduction to the company, including its name, headquarters location, size, and key business operations. Mention the company’s ESG mission, sustainability goals, and any major achievements related to environmental, social, or governance initiatives.

**Report Date**  
The report should be dated in December {YEAR}. Choose a specific date within December to reflect the annual summary.

**ESG Performance Summary (Narrative + Table Format)**  
For each of the **Environmental, Social, and Governance (ESG)** categories, include a written summary followed by a structured table presenting key performance indicators (KPIs).

**Environmental Performance**  
Describe the company's efforts in sustainability, emissions reduction, energy efficiency, and resource management. Discuss major initiatives and challenges.  
Present at least **five** key environmental KPIs in a table with:  
- KPI name  
- Value  
- Unit of measurement  
- Brief explanation  

**Social Performance**  
Summarize the company’s impact on employees, communities, and stakeholders. Highlight diversity, equity, inclusion (DEI) efforts, employee well-being, and social responsibility programs.  
Include at least **five** social KPIs in a table.  

**Governance Performance**  
Outline the company’s governance structure, ethical practices, transparency policies, and compliance measures. Discuss board diversity, executive compensation, and regulatory adherence.  
Provide at least **five** governance KPIs in a table.  

**Future Outlook**  
Discuss the company’s ESG roadmap for the coming years. Highlight future goals, strategies for improvement, and commitments to sustainability. Mention planned initiatives, technology investments, or policy changes that will drive ESG performance forward.  

Ensure the report aligns with recognized **ESG frameworks** such as **GRI, SASB, and ESRS**. The writing should be **clear, concise, and professional**, formatted for business executives and investors.
```

B. ESG-Specific KPI Templates

* Create predefined templates for each industry (tech, finance, manufacturing).
* Randomly populate values to simulate real variations.


Example KPI Template for the Energy Sector

```json
{
  "company": "EnergyCorp",
  "year": 2023,
  "environmental": {
    "carbon_emissions": {
      "value": 3.5,
      "unit": "metric tons CO₂ per MWh"
    },
    "water_usage": {
      "value": 25000,
      "unit": "cubic meters"
    }
  },
  "social": {
    "workforce_diversity": {
      "value": 38,
      "unit": "percentage"
    }
  },
  "governance": {
    "board_diversity": {
      "value": 25,
      "unit": "percentage"
    }
  }
}
```

C. Data Augmentation (Expanding Existing Data)

If you have some ESG reports, apply augmentation techniques:

* Paraphrase KPI descriptions using NLP models.
* Randomly vary numerical values within realistic ranges.
* Shuffle KPI order to avoid pattern memorization

```python 
import random

kpi_templates = [
    {"name": "Carbon Emissions", "unit": "metric tons CO₂", "min": 2, "max": 10},
    {"name": "Workforce Diversity", "unit": "percentage", "min": 30, "max": 50},
    {"name": "Board Diversity", "unit": "percentage", "min": 20, "max": 40}
]

def generate_random_kpi():
    kpi = random.choice(kpi_templates)
    value = round(random.uniform(kpi["min"], kpi["max"]), 2)
    return {"kpi_name": kpi["name"], "value": value, "unit": kpi["unit"]}

# Generate 5 random KPIs
generated_kpis = [generate_random_kpi() for _ in range(5)]
print(generated_kpis)

```


D. Retrieval-Based Synthetic Generation

* Use a database of real ESG reports to retrieve sample KPI descriptions.
* Combine retrieved text + numerical variations to create a semi-synthetic dataset.

👉 This approach mimics real company reports while ensuring the dataset is varied.



## Validating the Synthetic Data
Before using generated benchmark data, validate it with: ✅ Domain Experts: Ensure realistic KPI values.
* ✅ Automated Checks: Verify format consistency.
* ✅ Diversity Checks: Cover multiple industries & KPI categories.

## Evaluating KPI Extraction on Generated Data
Once the dataset is ready, use it for RAG KPI extraction evaluation:

* Exact Match (EM): Compare extracted KPI with generated ground truth.
* F1 Score: Check if extracted text overlaps with correct KPIs.
* BLEU/ROUGE: Compare extracted vs. generated KPI text similarity.
* Hallucination Detection: Ensure extracted KPIs exist in source text.


--- 

## 🔹 Python Script for ESG KPI Data Generation

```python 
import json
import random

# Define KPI templates for different ESG categories
kpi_templates = {
    "environmental": [
        {"name": "Carbon Emissions", "unit": "metric tons CO₂", "min": 2, "max": 50},
        {"name": "Energy Consumption", "unit": "MWh", "min": 5000, "max": 50000},
        {"name": "Water Usage", "unit": "cubic meters", "min": 10000, "max": 200000}
    ],
    "social": [
        {"name": "Workforce Diversity", "unit": "percentage", "min": 30, "max": 60},
        {"name": "Employee Training Hours", "unit": "hours", "min": 10, "max": 50},
        {"name": "Health & Safety Incidents", "unit": "incidents", "min": 0, "max": 20}
    ],
    "governance": [
        {"name": "Board Diversity", "unit": "percentage", "min": 10, "max": 50},
        {"name": "Executive Compensation Ratio", "unit": "ratio", "min": 10, "max": 300},
        {"name": "Data Privacy Incidents", "unit": "incidents", "min": 0, "max": 10}
    ]
}

# List of sample companies and industries
companies = [
    {"name": "TechCorp", "industry": "Technology"},
    {"name": "GreenEnergy", "industry": "Energy"},
    {"name": "EcoFoods", "industry": "Food & Beverage"},
    {"name": "FinTrust", "industry": "Finance"},
    {"name": "HealthPlus", "industry": "Healthcare"}
]

# Function to generate random KPI values
def generate_random_kpi(category):
    kpi = random.choice(kpi_templates[category])
    value = round(random.uniform(kpi["min"], kpi["max"]), 2)
    return {"kpi_name": kpi["name"], "value": value, "unit": kpi["unit"]}

# Function to generate a synthetic ESG report
def generate_synthetic_esg_report(year):
    company = random.choice(companies)
    
    report = {
        "company": company["name"],
        "industry": company["industry"],
        "year": year,
        "environmental": [generate_random_kpi("environmental") for _ in range(3)],
        "social": [generate_random_kpi("social") for _ in range(2)],
        "governance": [generate_random_kpi("governance") for _ in range(2)]
    }
    return report

# Generate a dataset of 100 synthetic ESG reports
dataset = [generate_synthetic_esg_report(year=random.randint(2018, 2024)) for _ in range(100)]

# Save dataset as JSON
with open("synthetic_esg_kpi_dataset.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("✅ Synthetic ESG KPI dataset generated: synthetic_esg_kpi_dataset.json")

```


####🔹 Features of This Script
* ✔ Industry-Specific KPIs: Ensures relevance
* ✔ Randomized KPI Values: Mimics real-world variations
* ✔ Multi-Year Data: Generates reports from 2018-2024
* ✔ Scalable: Modify the range(100) to generate more reports
* ✔ JSON Format Output: Ready for ML evaluation & benchmarking



🔹 Sample Output (JSON Format)
```json
{
    "company": "GreenEnergy",
    "industry": "Energy",
    "year": 2023,
    "environmental": [
        {"kpi_name": "Carbon Emissions", "value": 23.45, "unit": "metric tons CO₂"},
        {"kpi_name": "Energy Consumption", "value": 15420.30, "unit": "MWh"},
        {"kpi_name": "Water Usage", "value": 134000.5, "unit": "cubic meters"}
    ],
    "social": [
        {"kpi_name": "Workforce Diversity", "value": 42.7, "unit": "percentage"},
        {"kpi_name": "Employee Training Hours", "value": 25.3, "unit": "hours"}
    ],
    "governance": [
        {"kpi_name": "Board Diversity", "value": 35.2, "unit": "percentage"},
        {"kpi_name": "Executive Compensation Ratio", "value": 85.6, "unit": "ratio"}
    ]
}
```



