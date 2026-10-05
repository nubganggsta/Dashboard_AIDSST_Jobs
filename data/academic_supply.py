"""
Academic Supply Dataset Generator & Access Functions
Implements curricula details, 5-year graduation output, tuition fees,
post-graduate employment rates, core courses, and credit-weighted skill matrices.
"""

import pandas as pd
import numpy as np

def get_academic_curricula_df() -> pd.DataFrame:
    """Returns the main dataframe of academic curricula."""
    data = [
        {
            "curriculum_id": "CURR01",
            "curriculum_name": "B.Sc. Data Science",
            "degree_level": "Bachelor's",
            "institution": "Chulalongkorn University",
            "duration_years": 4,
            "annual_graduates_2021": 95,
            "annual_graduates_2022": 110,
            "annual_graduates_2023": 125,
            "annual_graduates_2024": 140,
            "annual_graduates_2025": 160,
            "tuition_fee_per_term_thb": 30000,
            "tuition_fee_total_thb": 240000,
            "emp_rate_year_1": 0.88,
            "emp_rate_year_2": 0.94,
            "emp_rate_year_3": 0.96,
            "core_skills_taught": ["Python", "SQL", "Tableau", "Machine Learning", "A/B Testing", "Scikit-Learn", "Git"],
        },
        {
            "curriculum_id": "CURR02",
            "curriculum_name": "B.Sc. Applied Statistics",
            "degree_level": "Bachelor's",
            "institution": "Kasetsart University",
            "duration_years": 4,
            "annual_graduates_2021": 70,
            "annual_graduates_2022": 75,
            "annual_graduates_2023": 85,
            "annual_graduates_2024": 80,
            "annual_graduates_2025": 90,
            "tuition_fee_per_term_thb": 20000,
            "tuition_fee_total_thb": 160000,
            "emp_rate_year_1": 0.82,
            "emp_rate_year_2": 0.89,
            "emp_rate_year_3": 0.92,
            "core_skills_taught": ["R", "SAS", "Probability", "Regression Analysis", "SQL", "Hypothesis Testing", "Time Series"],
        },
        {
            "curriculum_id": "CURR03",
            "curriculum_name": "M.Sc. Artificial Intelligence",
            "degree_level": "Master's",
            "institution": "Sirindhorn International Institute (SIIT)",
            "duration_years": 2,
            "annual_graduates_2021": 30,
            "annual_graduates_2022": 38,
            "annual_graduates_2023": 45,
            "annual_graduates_2024": 50,
            "annual_graduates_2025": 65,
            "tuition_fee_per_term_thb": 80000,
            "tuition_fee_total_thb": 320000,
            "emp_rate_year_1": 0.95,
            "emp_rate_year_2": 0.98,
            "emp_rate_year_3": 0.99,
            "core_skills_taught": ["Python", "PyTorch", "Deep Learning", "NLP", "C++", "RAG", "Computer Vision", "TensorFlow"],
        },
        {
            "curriculum_id": "CURR04",
            "curriculum_name": "B.Sc. Computer Science (AI & Data)",
            "degree_level": "Bachelor's",
            "institution": "KMUTT",
            "duration_years": 4,
            "annual_graduates_2021": 130,
            "annual_graduates_2022": 140,
            "annual_graduates_2023": 150,
            "annual_graduates_2024": 165,
            "annual_graduates_2025": 185,
            "tuition_fee_per_term_thb": 27500,
            "tuition_fee_total_thb": 220000,
            "emp_rate_year_1": 0.90,
            "emp_rate_year_2": 0.95,
            "emp_rate_year_3": 0.97,
            "core_skills_taught": ["Python", "Java", "Data Structures", "SQL", "Scikit-Learn", "Docker", "Database Systems"],
        },
        {
            "curriculum_id": "CURR05",
            "curriculum_name": "M.Sc. Data Science & Business Analytics",
            "degree_level": "Master's",
            "institution": "NIDA",
            "duration_years": 2,
            "annual_graduates_2021": 40,
            "annual_graduates_2022": 52,
            "annual_graduates_2023": 60,
            "annual_graduates_2024": 72,
            "annual_graduates_2025": 85,
            "tuition_fee_per_term_thb": 70000,
            "tuition_fee_total_thb": 280000,
            "emp_rate_year_1": 0.93,
            "emp_rate_year_2": 0.97,
            "emp_rate_year_3": 0.98,
            "core_skills_taught": ["Python", "SQL", "Power BI", "A/B Testing", "Machine Learning", "Cloud Analytics", "Business Intelligence"],
        },
        {
            "curriculum_id": "CURR06",
            "curriculum_name": "B.Sc. Statistics & Big Data",
            "degree_level": "Bachelor's",
            "institution": "Khon Kaen University",
            "duration_years": 4,
            "annual_graduates_2021": 65,
            "annual_graduates_2022": 72,
            "annual_graduates_2023": 80,
            "annual_graduates_2024": 85,
            "annual_graduates_2025": 95,
            "tuition_fee_per_term_thb": 22500,
            "tuition_fee_total_thb": 180000,
            "emp_rate_year_1": 0.85,
            "emp_rate_year_2": 0.91,
            "emp_rate_year_3": 0.94,
            "core_skills_taught": ["R", "Python", "SQL", "Spark", "Regression Analysis", "Time Series", "Probability"],
        }
    ]
    df = pd.DataFrame(data)
    # Total graduates across tracked 5 years
    year_cols = ["annual_graduates_2021", "annual_graduates_2022", "annual_graduates_2023", "annual_graduates_2024", "annual_graduates_2025"]
    df["total_accumulated_graduates"] = df[year_cols].sum(axis=1)
    return df

def get_curriculum_timeline_df(curricula_df: pd.DataFrame = None) -> pd.DataFrame:
    """Melts the annual graduates into a tidy format for time-series charts."""
    if curricula_df is None:
        curricula_df = get_academic_curricula_df()
    
    id_vars = ["curriculum_id", "curriculum_name", "degree_level", "institution"]
    val_vars = ["annual_graduates_2021", "annual_graduates_2022", "annual_graduates_2023", "annual_graduates_2024", "annual_graduates_2025"]
    melted = pd.melt(curricula_df, id_vars=id_vars, value_vars=val_vars, var_name="year_col", value_name="graduates")
    melted["year"] = melted["year_col"].str.extract(r"(\d{4})").astype(int)
    return melted.sort_values(by=["year", "curriculum_name"])

def get_core_courses_matrix() -> pd.DataFrame:
    """Returns detailed core required courses and skill coverage per curriculum."""
    courses = [
        # CURR01: B.Sc. Data Science
        {"curriculum_id": "CURR01", "curriculum_name": "B.Sc. Data Science", "course_code": "DS101", "course_name": "Python for Data Science", "credits": 3, "category": "Programming", "skill": "Python"},
        {"curriculum_id": "CURR01", "curriculum_name": "B.Sc. Data Science", "course_code": "DS202", "course_name": "Relational Databases & SQL Analytics", "credits": 3, "category": "Data Management", "skill": "SQL"},
        {"curriculum_id": "CURR01", "curriculum_name": "B.Sc. Data Science", "course_code": "DS301", "course_name": "Applied Machine Learning", "credits": 4, "category": "AI/ML", "skill": "Machine Learning"},
        {"curriculum_id": "CURR01", "curriculum_name": "B.Sc. Data Science", "course_code": "DS304", "course_name": "Data Visualization & Storytelling", "credits": 3, "category": "Analytics", "skill": "Tableau"},
        {"curriculum_id": "CURR01", "curriculum_name": "B.Sc. Data Science", "course_code": "DS401", "course_name": "A/B Testing & Causal Inference", "credits": 3, "category": "Analytics", "skill": "A/B Testing"},
        
        # CURR02: B.Sc. Applied Statistics
        {"curriculum_id": "CURR02", "curriculum_name": "B.Sc. Applied Statistics", "course_code": "ST201", "course_name": "Probability Theory & Inference", "credits": 4, "category": "Mathematics/Stats", "skill": "Probability"},
        {"curriculum_id": "CURR02", "curriculum_name": "B.Sc. Applied Statistics", "course_code": "ST302", "course_name": "Applied Regression Analysis", "credits": 4, "category": "Mathematics/Stats", "skill": "Regression Analysis"},
        {"curriculum_id": "CURR02", "curriculum_name": "B.Sc. Applied Statistics", "course_code": "ST305", "course_name": "Statistical Programming in R & SAS", "credits": 3, "category": "Programming", "skill": "R"},
        {"curriculum_id": "CURR02", "curriculum_name": "B.Sc. Applied Statistics", "course_code": "ST305", "course_name": "Statistical Programming in R & SAS", "credits": 3, "category": "Programming", "skill": "SAS"},
        {"curriculum_id": "CURR02", "curriculum_name": "B.Sc. Applied Statistics", "course_code": "ST410", "course_name": "Time Series Modeling", "credits": 3, "category": "Mathematics/Stats", "skill": "Time Series"},

        # CURR03: M.Sc. Artificial Intelligence
        {"curriculum_id": "CURR03", "curriculum_name": "M.Sc. Artificial Intelligence", "course_code": "AI601", "course_name": "Deep Learning & Neural Architectures", "credits": 4, "category": "AI/ML", "skill": "Deep Learning"},
        {"curriculum_id": "CURR03", "curriculum_name": "M.Sc. Artificial Intelligence", "course_code": "AI602", "course_name": "Advanced PyTorch & Model Optimization", "credits": 3, "category": "AI/ML", "skill": "PyTorch"},
        {"curriculum_id": "CURR03", "curriculum_name": "M.Sc. Artificial Intelligence", "course_code": "AI703", "course_name": "Natural Language Processing & LLMs", "credits": 3, "category": "AI/ML", "skill": "NLP"},
        {"curriculum_id": "CURR03", "curriculum_name": "M.Sc. Artificial Intelligence", "course_code": "AI705", "course_name": "Retrieval-Augmented Generation (RAG)", "credits": 3, "category": "AI/ML", "skill": "RAG"},
        {"curriculum_id": "CURR03", "curriculum_name": "M.Sc. Artificial Intelligence", "course_code": "AI610", "course_name": "High Performance Computing in C++", "credits": 3, "category": "Programming", "skill": "C++"},

        # CURR04: B.Sc. Computer Science (AI & Data)
        {"curriculum_id": "CURR04", "curriculum_name": "B.Sc. Computer Science (AI & Data)", "course_code": "CS201", "course_name": "Data Structures & Algorithms", "credits": 4, "category": "Programming", "skill": "Data Structures"},
        {"curriculum_id": "CURR04", "curriculum_name": "B.Sc. Computer Science (AI & Data)", "course_code": "CS205", "course_name": "Object-Oriented Programming (Java/Python)", "credits": 3, "category": "Programming", "skill": "Java"},
        {"curriculum_id": "CURR04", "curriculum_name": "B.Sc. Computer Science (AI & Data)", "course_code": "CS312", "course_name": "Database Systems & SQL Optimization", "credits": 3, "category": "Data Management", "skill": "SQL"},
        {"curriculum_id": "CURR04", "curriculum_name": "B.Sc. Computer Science (AI & Data)", "course_code": "CS340", "course_name": "Introduction to AI & Scikit-Learn", "credits": 3, "category": "AI/ML", "skill": "Scikit-Learn"},
        {"curriculum_id": "CURR04", "curriculum_name": "B.Sc. Computer Science (AI & Data)", "course_code": "CS420", "course_name": "Cloud Deployment & Containerization", "credits": 3, "category": "Engineering", "skill": "Docker"},

        # CURR05: M.Sc. Data Science & Business Analytics
        {"curriculum_id": "CURR05", "curriculum_name": "M.Sc. Data Science & Business Analytics", "course_code": "BA601", "course_name": "Business Analytics & Power BI", "credits": 3, "category": "Analytics", "skill": "Power BI"},
        {"curriculum_id": "CURR05", "curriculum_name": "M.Sc. Data Science & Business Analytics", "course_code": "BA605", "course_name": "Predictive Modeling with Python", "credits": 4, "category": "AI/ML", "skill": "Python"},
        {"curriculum_id": "CURR05", "curriculum_name": "M.Sc. Data Science & Business Analytics", "course_code": "BA610", "course_name": "Advanced SQL & Data Warehousing", "credits": 3, "category": "Data Management", "skill": "SQL"},
        {"curriculum_id": "CURR05", "curriculum_name": "M.Sc. Data Science & Business Analytics", "course_code": "BA620", "course_name": "Enterprise Experimentation & A/B Testing", "credits": 3, "category": "Analytics", "skill": "A/B Testing"},

        # CURR06: B.Sc. Statistics & Big Data
        {"curriculum_id": "CURR06", "curriculum_name": "B.Sc. Statistics & Big Data", "course_code": "BD201", "course_name": "Statistical Computing with R", "credits": 3, "category": "Programming", "skill": "R"},
        {"curriculum_id": "CURR06", "curriculum_name": "B.Sc. Statistics & Big Data", "course_code": "BD302", "course_name": "Distributed Data Processing with Spark", "credits": 4, "category": "Engineering", "skill": "Spark"},
        {"curriculum_id": "CURR06", "curriculum_name": "B.Sc. Statistics & Big Data", "course_code": "BD305", "course_name": "Linear Models & Regression", "credits": 3, "category": "Mathematics/Stats", "skill": "Regression Analysis"},
        {"curriculum_id": "CURR06", "curriculum_name": "B.Sc. Statistics & Big Data", "course_code": "BD401", "course_name": "Database & Query Systems", "credits": 3, "category": "Data Management", "skill": "SQL"},
        {"curriculum_id": "CURR06", "curriculum_name": "B.Sc. Statistics & Big Data", "course_code": "BD410", "course_name": "Python for Data Analysis", "credits": 3, "category": "Programming", "skill": "Python"},
    ]
    return pd.DataFrame(courses)

def get_academic_skills_coverage(curricula_df: pd.DataFrame = None) -> pd.DataFrame:
    """
    Computes percentage of curricula teaching each skill.
    """
    if curricula_df is None:
        curricula_df = get_academic_curricula_df()
    
    total_curricula = len(curricula_df)
    skill_counts = {}
    
    for _, row in curricula_df.iterrows():
        skills = set(row["core_skills_taught"])
        for s in skills:
            skill_counts[s] = skill_counts.get(s, 0) + 1
            
    records = []
    for skill, count in skill_counts.items():
        records.append({
            "skill": skill,
            "curricula_count": count,
            "total_curricula": total_curricula,
            "academic_supply_pct": round((count / total_curricula) * 100, 1)
        })
    return pd.DataFrame(records).sort_values(by="academic_supply_pct", ascending=False)
