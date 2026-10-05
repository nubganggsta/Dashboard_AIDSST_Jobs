"""
Skill Mismatch Analytics & Recommendation Algorithms
Computes alignment indices, 2x2 matrix classifications, deficit/surplus metrics,
and generates actionable curriculum recommendations.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, List

def compute_skill_mismatch_metrics(
    academic_skills_df: pd.DataFrame, 
    demand_skills_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Merges academic supply and job market demand skill percentages and calculates
    mismatch indices, gap categories, and priority classifications.
    """
    # Merge on skill name
    merged = pd.merge(
        academic_skills_df[["skill", "academic_supply_pct"]],
        demand_skills_df[["skill", "demand_percentage"]],
        on="skill",
        how="outer"
    ).fillna(0.0)
    
    # Calculate Gap Delta: Demand % - Supply %
    # Positive delta means market demands more than universities supply (Deficit)
    # Negative delta means universities supply more than market currently demands (Surplus/Niche)
    merged["gap_delta"] = merged["demand_percentage"] - merged["academic_supply_pct"]
    
    def classify_quadrant(row):
        supply = row["academic_supply_pct"]
        demand = row["demand_percentage"]
        threshold = 30.0
        
        if demand >= threshold and supply >= threshold:
            return "Core Essentials (High Supply / High Demand)"
        elif demand >= threshold and supply < threshold:
            return "Urgent Curriculum Gap (Low Supply / High Demand)"
        elif demand < threshold and supply >= threshold:
            return "Niche / Academic Focus (High Supply / Low Demand)"
        else:
            return "Specialized / Low Volume (Low Supply / Low Demand)"
            
    def classify_status(row):
        delta = row["gap_delta"]
        demand = row["demand_percentage"]
        supply = row["academic_supply_pct"]
        
        if delta >= 20.0 or (demand >= 35.0 and supply < 25.0):
            return "Critical Deficit"
        elif delta <= -25.0:
            return "Over-Supplied / Niche"
        elif abs(delta) <= 15.0 and (demand >= 20.0 or supply >= 20.0):
            return "Well-Aligned"
        else:
            return "Moderate Gap"

    def generate_recommendation(row):
        skill = row["skill"]
        status = row["status"]
        supply = row["academic_supply_pct"]
        demand = row["demand_percentage"]
        
        if status == "Critical Deficit":
            return f"🚨 Urgent Curriculum Gap: Industry demand ({demand:.1f}%) significantly outpaces academic training ({supply:.1f}%). Prioritize establishing dedicated course modules or industry micro-credentials."
        elif status == "Over-Supplied / Niche":
            return f"⚠️ Academic Surplus / Legacy Focus: Course coverage is high ({supply:.1f}%), yet direct industry demand is modest ({demand:.1f}%). Consider restructuring into specialized elective tracks."
        elif status == "Well-Aligned":
            return f"✅ Balanced Alignment: Academic instruction ({supply:.1f}%) aligns closely with market demand ({demand:.1f}%). Maintain and periodically refresh modern best practices."
        else:
            return f"ℹ️ Emerging / Secondary Priority: Monitor market trajectory. Encourage student capstone projects and extracurricular workshops in {skill}."

    merged["quadrant"] = merged.apply(classify_quadrant, axis=1)
    merged["status"] = merged.apply(classify_status, axis=1)
    merged["recommendation"] = merged.apply(generate_recommendation, axis=1)
    
    # Priority sorting
    priority_map = {"Critical Deficit": 1, "Moderate Gap": 2, "Over-Supplied / Niche": 3, "Well-Aligned": 4}
    merged["priority_rank"] = merged["status"].map(priority_map).fillna(5)
    
    return merged.sort_values(by=["priority_rank", "demand_percentage"], ascending=[True, False]).reset_index(drop=True)

def calculate_scorecard_summary(mismatch_df: pd.DataFrame) -> Dict[str, Any]:
    """
    Computes top-level scorecard summary:
    - Skill Alignment Index (%)
    - Critical Deficit Skills Count
    - Over-supplied Skills Count
    - Top Deficit Skill
    """
    if mismatch_df.empty:
        return {
            "alignment_index_pct": 0.0,
            "critical_deficit_count": 0,
            "oversupplied_count": 0,
            "top_deficit_skill": "None"
        }
        
    # Alignment Index: 100 - Mean Absolute Difference (bounded between 0 and 100)
    mad = np.mean(np.abs(mismatch_df["demand_percentage"] - mismatch_df["academic_supply_pct"]))
    alignment_index = max(0.0, min(100.0, 100.0 - mad))
    
    critical_deficits = mismatch_df[mismatch_df["status"] == "Critical Deficit"]
    oversupplied = mismatch_df[mismatch_df["status"] == "Over-Supplied / Niche"]
    
    top_deficit = critical_deficits.iloc[0]["skill"] if not critical_deficits.empty else "None"
    
    return {
        "alignment_index_pct": round(alignment_index, 1),
        "critical_deficit_count": int(len(critical_deficits)),
        "oversupplied_count": int(len(oversupplied)),
        "top_deficit_skill": top_deficit
    }
