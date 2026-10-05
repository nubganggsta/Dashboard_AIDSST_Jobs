"""
Job Market Demand Dataset Generator & Access Functions
Implements labor market demand, job titles, industry sectors, hiring enterprises,
seniority tiers, salary ranges, and in-demand technical competencies.
"""

import pandas as pd
import numpy as np

def generate_job_demand_df(n_samples: int = 250, seed: int = 42) -> pd.DataFrame:
    """Generates a realistic job demand dataset for Thailand & SEA tech ecosystem."""
    np.random.seed(seed)
    
    job_titles_config = [
        {"title": "Data Scientist", "weight": 0.28, "sector": ["Banking & FinTech", "Tech Platforms", "Consulting", "Retail & Conglomerate"]},
        {"title": "AI/ML Engineer", "weight": 0.24, "sector": ["Tech Platforms", "Banking & FinTech", "Telecommunications", "AI Research"]},
        {"title": "Data Analyst", "weight": 0.22, "sector": ["Retail & Conglomerate", "Banking & FinTech", "Tech Platforms", "Consulting"]},
        {"title": "Data Engineer", "weight": 0.16, "sector": ["Banking & FinTech", "Tech Platforms", "Telecommunications", "Consulting"]},
        {"title": "Statistician", "weight": 0.10, "sector": ["Consulting", "Healthcare & Pharma", "Banking & FinTech", "Market Research"]},
    ]
    
    titles = [cfg["title"] for cfg in job_titles_config]
    weights = [cfg["weight"] for cfg in job_titles_config]
    
    companies_by_sector = {
        "Banking & FinTech": ["SCBX", "KBTG", "Kasikornbank", "Krungsri Nimble", "Bitkub", "JPMorgan Chase"],
        "Tech Platforms": ["Agoda", "Grab", "LINE Thailand", "Shopee", "TikTok ByteDance", "Ascend Money"],
        "Telecommunications": ["True Corp", "AIS", "Dtac Enterprise"],
        "Retail & Conglomerate": ["Central Group", "CP All", "PTT Digital", "Siam Commercial Retails", "SCG"],
        "Consulting": ["McKinsey", "BCG", "Accenture", "Deloitte", "PwC", "Bain"],
        "AI Research": ["SCB 10X", "VISTEC Research", "National AI Hub"],
        "Healthcare & Pharma": ["BDMS Analytics", "Bumrungrad Data Lab", "Roche Thailand"],
        "Market Research": ["NielsenIQ", "Ipsos Thailand", "Kantar"]
    }
    
    skill_pool_by_title = {
        "Data Scientist": ["Python", "SQL", "Scikit-Learn", "Machine Learning", "A/B Testing", "Tableau", "Power BI", "AWS", "PyTorch", "Docker"],
        "AI/ML Engineer": ["Python", "PyTorch", "Deep Learning", "RAG", "Vector DBs", "Docker", "Kubernetes", "MLOps", "NLP", "C++", "AWS"],
        "Data Analyst": ["SQL", "Power BI", "Tableau", "Python", "Excel", "A/B Testing", "Business Intelligence", "Google BigQuery"],
        "Data Engineer": ["Python", "SQL", "Spark", "Docker", "Kubernetes", "AWS", "Google BigQuery", "PostgreSQL", "Snowflake", "Git"],
        "Statistician": ["R", "SAS", "Probability", "Regression Analysis", "Hypothesis Testing", "Time Series", "SQL", "A/B Testing", "Python"]
    }
    
    data = []
    
    for i in range(1, n_samples + 1):
        job_id = f"JOB_{i:04d}"
        job_title = np.random.choice(titles, p=weights)
        
        # Sector
        matched_cfg = next(c for c in job_titles_config if c["title"] == job_title)
        sector = np.random.choice(matched_cfg["sector"])
        
        # Company
        company_candidates = companies_by_sector.get(sector, ["Tech Solution Co."])
        company_name = np.random.choice(company_candidates)
        
        # Seniority
        seniority = np.random.choice(["Entry-Level", "Mid-Level", "Senior/Lead"], p=[0.42, 0.38, 0.20])
        
        # Salary calculation based on Seniority and Role (THB per month)
        if seniority == "Entry-Level":
            base_min = np.random.randint(28, 38) * 1000
            base_max = base_min + np.random.randint(8, 16) * 1000
            degree = np.random.choice(["Bachelor's", "Master's"], p=[0.75, 0.25])
        elif seniority == "Mid-Level":
            base_min = np.random.randint(55, 75) * 1000
            base_max = base_min + np.random.randint(20, 40) * 1000
            degree = np.random.choice(["Bachelor's", "Master's"], p=[0.55, 0.45])
        else: # Senior/Lead
            base_min = np.random.randint(110, 140) * 1000
            base_max = base_min + np.random.randint(40, 90) * 1000
            degree = np.random.choice(["Master's", "PhD / Doctorate", "Bachelor's"], p=[0.50, 0.20, 0.30])
            
        salary_avg = int((base_min + base_max) / 2)
        
        # Skills
        title_skills = skill_pool_by_title.get(job_title, ["Python", "SQL"])
        n_skills = np.random.randint(4, 7)
        chosen_skills = np.random.choice(title_skills, size=min(n_skills, len(title_skills)), replace=False).tolist()
        
        # Add market trend bonus skills with probability (RAG, Docker, Power BI, SQL, Python)
        trending = ["Docker", "RAG", "SQL", "Python", "Cloud Platforms"]
        for t in trending:
            if t not in chosen_skills and np.random.rand() < 0.25:
                chosen_skills.append(t)
                
        work_model = np.random.choice(["Hybrid", "On-site", "Remote"], p=[0.60, 0.25, 0.15])
        
        data.append({
            "job_id": job_id,
            "job_title": job_title,
            "company_name": company_name,
            "industry_sector": sector,
            "seniority_level": seniority,
            "salary_min_thb": base_min,
            "salary_max_thb": base_max,
            "salary_avg_thb": salary_avg,
            "required_skills": chosen_skills,
            "degree_required": degree,
            "work_model": work_model,
            "location": "Bangkok, Thailand" if work_model != "Remote" else "Remote (SEA)"
        })
        
    return pd.DataFrame(data)

def get_skill_demand_counts(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates frequency and demand percentage for each required skill."""
    total_jobs = len(df)
    skill_counter = {}
    
    for _, row in df.iterrows():
        for skill in set(row["required_skills"]):
            skill_counter[skill] = skill_counter.get(skill, 0) + 1
            
    records = []
    for skill, count in skill_counter.items():
        records.append({
            "skill": skill,
            "demand_count": count,
            "total_jobs": total_jobs,
            "demand_percentage": round((count / total_jobs) * 100, 1)
        })
        
    return pd.DataFrame(records).sort_values(by="demand_percentage", ascending=False)
