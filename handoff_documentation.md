# 🚀 AI & Data Science Market Dashboard — Handoff Specification

**Target AI Agent:** Antigravity

**Task Domain:** Frontend Web Development / Data Visualization / Interactive Dashboard

**Status:** Ready for Execution

## 1. Project Overview & Objective

This document serves as the handoff specification for **Antigravity** to generate an interactive, responsive Data Visualization Dashboard. The dashboard synthesizes global and regional (Thailand/SEA) statistics regarding AI, Data Science, and Statistics graduates, employment rates, entry-level salaries, required skills, and key hiring organizations.

## 2. Core Data Payload (Structured JSON Schema)

Antigravity must ingest and render the following dataset into dynamic visualizations:

```json
{
  "market_overview": {
    "us_open_positions": 245900,
    "us_projected_growth_10yr": "34%",
    "thailand_annual_graduates_stem": 65000,
    "thailand_annual_graduates_datasci_stat": 4200,
    "global_annual_graduates": 280000
  },
  "salary_by_region": [
    { "region": "USA", "currency": "USD", "unit": "Yearly", "entry_min": 75000, "entry_max": 95000, "senior_min": 112590, "senior_max": 190000 },
    { "region": "Singapore", "currency": "SGD", "unit": "Monthly", "entry_min": 45000, "entry_max": 6500, "senior_min": 7500, "senior_max": 14000 },
    { "region": "EU/UK", "currency": "EUR", "unit": "Yearly", "entry_min": 45000, "entry_max": 60000, "senior_min": 65000, "senior_max": 110000 },
    { "region": "Thailand", "currency": "THB", "unit": "Monthly", "entry_min": 28000, "entry_max": 45000, "senior_min": 55000, "senior_max": 180000 }
  ],
  "degree_requirements_percent": [
    { "degree": "Bachelor's Degree", "percentage": 58 },
    { "degree": "Master's Degree", "percentage": 34 },
    { "degree": "PhD / Doctorate", "percentage": 8 }
  ],
  "skill_demands": [
    { "category": "Programming & Databases", "skills": ["Python", "SQL", "PostgreSQL", "Snowflake", "BigQuery"] },
    { "category": "Machine Learning & AI", "skills": ["PyTorch", "TensorFlow", "Scikit-Learn", "XGBoost"] },
    { "category": "Generative AI & LLMs", "skills": ["LangChain", "LlamaIndex", "Vector DBs (Pinecone/Chroma)", "RAG", "Prompting/Fine-tuning"] },
    { "category": "Analytics & Visualization", "skills": ["Tableau", "Power BI", "Streamlit", "A/B Testing"] },
    { "category": "Engineering & MLOps", "skills": ["Docker", "Kubernetes", "Git", "MLflow", "AWS/GCP"] }
  ],
  "hiring_companies_by_sector": {
    "big_tech_ai": ["OpenAI", "Anthropic", "Google DeepMind", "Microsoft", "Meta", "NVIDIA", "AWS"],
    "consulting": ["McKinsey", "BCG", "Bain", "Accenture", "Deloitte", "PwC"],
    "finance_banking": ["JPMorgan Chase", "Goldman Sachs", "SCBX", "KBTG", "Krungsri Nimble"],
    "tech_platforms": ["Agoda", "Grab", "Shopee", "LINE Thailand", "Central Group"]
  }
}
```

## 3. Dashboard Design & Layout Requirements

Antigravity should construct the user interface with the following component hierarchy:

### 📊 Component 1: Key Metric Cards (KPI Summary)

* **Total US Market Demand:** `245,900` positions (+34% 10-Yr Growth)
* **Global Annual Graduates:** `~280,000` (Data Sci, Stats, ML)
* **TH Annual Specialists:** `~3,500 – 5,000` graduates/year
* **Top Entry Qualification:** Bachelor's Degree (58% of postings)

### 📈 Component 2: Visualizations

1. **Salary Comparison Chart (Bar / Grouped Bar Chart):**
   * Compare Entry-Level vs. Mid-Senior salaries across USA, Singapore, EU, and Thailand (normalized to USD or shown with regional units).

2. **Degree Requirement Distribution (Donut / Pie Chart):**
   * Visual Breakdown: Bachelor's (58%), Master's (34%), PhD (8%).

3. **In-Demand Skill Matrix (Interactive Tags / Skill Density Bar Chart):**
   * Filterable categories: *Programming*, *GenAI/LLMs*, *ML/Stats*, *MLOps*.

4. **Hiring Ecosystem Directory (Searchable / Filterable Cards):**
   * Categorized tabs: Big Tech, Consulting, Financial Services, Regional E-Commerce.

5. **Open Data Repository Footer / References Section:**
   * Direct links and modal descriptions for all open datasets used.

## 4. Open Data Sources & Reference Links

Antigravity should embed or link these Open Data sources within the dashboard interface (e.g., in a "Data Sources & Methodology" footer or sidebar panel):

1. **Global Data Science & AI Job Salaries (2020–2026)**
   * **Description:** Comprehensive dataset covering salaries, job titles, experience levels, employment types, and company sizes worldwide.
   * **Format:** CSV (CC0 / Public Domain)
   * **URL:** [Kaggle Global Data Science Jobs & Salaries Dataset](https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries)

2. **U.S. Bureau of Labor Statistics (BLS) — Data Scientists Data**
   * **Description:** Official government labor statistics for US market size, median annual wage, education levels, and 10-year job outlook.
   * **Format:** CSV / HTML Open Data
   * **URL:** [U.S. BLS Data Scientists Occupational Outlook](https://www.bls.gov/ooh/math/data-scientists.htm)

3. **MHESI Open Data Portal (MHESI Thailand)**
   * **Description:** Official Thai higher education database detailing graduation rates across STEM, Statistics, Data Science, and IT disciplines.
   * **Format:** CSV / JSON / REST API
   * **URL:** [MHESI Open Data Portal Thailand](https://data.mhesi.go.th/)

4. **Stack Overflow Annual Developer Survey (Data Science & AI Focus)**
   * **Description:** Anonymized survey responses on tech stacks, programming languages, salaries, and framework adoption globally.
   * **Format:** CSV (Open Data Commons License)
   * **URL:** [Stack Overflow Developer Survey Download](https://insights.stackoverflow.com/survey)

## 5. Technical Constraints for Antigravity

1. **Format:** Single self-contained HTML file (including Tailwind CSS + Chart.js / Recharts / Lucide icons) OR a Streamlit Python App.
2. **Theme:** Modern Dark Mode (`bg-slate-900`, `text-slate-100`, `accent-cyan-400`).
3. **Interactivity:**
   * Dynamic filtering by region (Global vs. Thailand).
   * Interactive tooltips on all chart elements.
   * Search box for filtering required skills and companies.
   * Clickable external links to open data sources.

## 6. Execution Directive for Antigravity

> **Prompt for Antigravity:**
> *"Using the JSON data payload, open data source citations, and design requirements specified in `handoff_antigravity_dashboard.md`, build a production-ready, interactive single-file Dashboard web application. Ensure responsive chart layouts, dark-mode styling, open data references, and functional search/filter controls."*