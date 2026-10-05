"""
Market Overview & Regional Benchmark Data
Derived from Handoff Specification and International Labor Statistics.
"""

import pandas as pd

MARKET_OVERVIEW_STATS = {
    "us_open_positions": 245900,
    "us_projected_growth_10yr": "34%",
    "thailand_annual_graduates_stem": 65000,
    "thailand_annual_graduates_datasci_stat": 4200,
    "global_annual_graduates": 280000,
    "top_entry_qualification": "Bachelor's Degree (58%)"
}

SALARY_BY_REGION_RAW = [
    {
        "region": "USA",
        "currency": "USD",
        "unit": "Yearly",
        "entry_min": 75000,
        "entry_max": 95000,
        "senior_min": 112590,
        "senior_max": 190000,
        "normalized_entry_usd_yr": 85000,
        "normalized_senior_usd_yr": 151295
    },
    {
        "region": "Singapore",
        "currency": "SGD",
        "unit": "Monthly",
        "entry_min": 4500,
        "entry_max": 6500,
        "senior_min": 7500,
        "senior_max": 14000,
        # 1 SGD approx 0.75 USD, yearly = * 12
        "normalized_entry_usd_yr": int(((4500 + 6500) / 2) * 12 * 0.75),
        "normalized_senior_usd_yr": int(((7500 + 14000) / 2) * 12 * 0.75)
    },
    {
        "region": "EU/UK",
        "currency": "EUR",
        "unit": "Yearly",
        "entry_min": 45000,
        "entry_max": 60000,
        "senior_min": 65000,
        "senior_max": 110000,
        # 1 EUR approx 1.08 USD
        "normalized_entry_usd_yr": int(((45000 + 60000) / 2) * 1.08),
        "normalized_senior_usd_yr": int(((65000 + 110000) / 2) * 1.08)
    },
    {
        "region": "Thailand",
        "currency": "THB",
        "unit": "Monthly",
        "entry_min": 28000,
        "entry_max": 45000,
        "senior_min": 55000,
        "senior_max": 180000,
        # 1 USD approx 36 THB, yearly = * 12 / 36
        "normalized_entry_usd_yr": int(((28000 + 45000) / 2) * 12 / 36),
        "normalized_senior_usd_yr": int(((55000 + 180000) / 2) * 12 / 36)
    }
]

DEGREE_REQUIREMENTS_DATA = [
    {"degree": "Bachelor's Degree", "percentage": 58, "color": "#38bdf8"},
    {"degree": "Master's Degree", "percentage": 34, "color": "#818cf8"},
    {"degree": "PhD / Doctorate", "percentage": 8, "color": "#c084fc"}
]

SKILL_DEMAND_TAXONOMY = [
    {
        "category": "Programming & Databases",
        "skills": ["Python", "SQL", "PostgreSQL", "Snowflake", "BigQuery"],
        "icon": "💻"
    },
    {
        "category": "Machine Learning & AI",
        "skills": ["PyTorch", "TensorFlow", "Scikit-Learn", "XGBoost"],
        "icon": "🤖"
    },
    {
        "category": "Generative AI & LLMs",
        "skills": ["LangChain", "LlamaIndex", "Vector DBs (Pinecone/Chroma)", "RAG", "Prompting/Fine-tuning"],
        "icon": "✨"
    },
    {
        "category": "Analytics & Visualization",
        "skills": ["Tableau", "Power BI", "Streamlit", "A/B Testing"],
        "icon": "📊"
    },
    {
        "category": "Engineering & MLOps",
        "skills": ["Docker", "Kubernetes", "Git", "MLflow", "AWS/GCP"],
        "icon": "⚙️"
    }
]

HIRING_COMPANIES_BY_SECTOR = {
    "Big Tech & AI Leaders": ["OpenAI", "Anthropic", "Google DeepMind", "Microsoft", "Meta", "NVIDIA", "AWS"],
    "Strategic & Tech Consulting": ["McKinsey", "BCG", "Bain", "Accenture", "Deloitte", "PwC"],
    "Finance & Commercial Banking": ["JPMorgan Chase", "Goldman Sachs", "SCBX", "KBTG", "Krungsri Nimble"],
    "Regional Tech Platforms & Retail": ["Agoda", "Grab", "Shopee", "LINE Thailand", "Central Group"]
}

OPEN_DATA_REPOSITORIES = [
    {
        "name": "Global Data Science & AI Job Salaries (2020–2026)",
        "source": "Kaggle Open Datasets (CC0 Public Domain)",
        "url": "https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries",
        "description": "Comprehensive dataset covering salaries, job titles, experience levels, employment types, and company sizes worldwide."
    },
    {
        "name": "U.S. Bureau of Labor Statistics (BLS) — Data Scientists",
        "source": "U.S. Department of Labor (Open Gov Data)",
        "url": "https://www.bls.gov/ooh/math/data-scientists.htm",
        "description": "Official government labor statistics for US market size, median annual wage, education levels, and 10-year job outlook (+34% growth)."
    },
    {
        "name": "MHESI Open Data Portal (Thailand)",
        "source": "Ministry of Higher Education, Science, Research and Innovation",
        "url": "https://data.mhesi.go.th/",
        "description": "Official Thai higher education database detailing annual graduation volumes across STEM, Statistics, Data Science, and IT disciplines."
    },
    {
        "name": "Stack Overflow Annual Developer Survey",
        "source": "Stack Overflow Insights (Open Data Commons)",
        "url": "https://insights.stackoverflow.com/survey",
        "description": "Global survey responses on developer tech stacks, programming languages, salaries, and framework adoption trends."
    }
]

def get_salary_by_region_df() -> pd.DataFrame:
    return pd.DataFrame(SALARY_BY_REGION_RAW)

def get_degree_requirements_df() -> pd.DataFrame:
    return pd.DataFrame(DEGREE_REQUIREMENTS_DATA)
