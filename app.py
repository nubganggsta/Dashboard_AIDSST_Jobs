"""
Main Streamlit Application:
AI & Data Science Market Dashboard — Crimson Soft Light System
"""

import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="AI & Data Science Market Dashboard",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import styling and visual modules
from modules.components import inject_custom_css
from modules.tab_academic import render_tab_academic
from modules.tab_demand import render_tab_demand
from modules.tab_mismatch import render_tab_mismatch
from modules.tab_global import render_tab_global, render_open_data_footer

from data.academic_supply import get_academic_curricula_df, get_academic_skills_coverage
from data.job_demand import generate_job_demand_df, get_skill_demand_counts
from utils.calculations import compute_skill_mismatch_metrics

# Inject Crimson Soft Light styling
inject_custom_css()

# --- Initialize Base Reference Data ---
@st.cache_data
def load_base_data():
    acad_df = get_academic_curricula_df()
    job_df = generate_job_demand_df()
    return acad_df, job_df

base_acad_df, base_job_df = load_base_data()

# --- Left Sidebar Navigation & Filters (Solid Burgundy #800020) ---
st.sidebar.markdown(
    """
    <div style="padding: 10px 0 18px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.2); margin-bottom: 15px;">
        <h2 style="color: #FFFFFF !important; margin: 0; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.01em;">
            🍷 AI & DATA SCIENCE
        </h2>
        <p style="color: rgba(255, 255, 255, 0.8) !important; font-size: 0.82rem; margin: 3px 0 0 0;">
            Supply-Demand & Skill Mismatch
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("### 🎓 Academic Supply Filters")
all_curricula = sorted(base_acad_df["curriculum_name"].unique().tolist())
selected_curricula = st.sidebar.multiselect(
    "Select Degree Programs:",
    options=all_curricula,
    default=all_curricula,
    help="Filters academic output trends and curriculum course matrices across tabs."
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💼 Labor Demand Filters")
all_roles = sorted(base_job_df["job_title"].unique().tolist())
selected_roles = st.sidebar.multiselect(
    "Select Job Titles:",
    options=all_roles,
    default=all_roles,
    help="Filter active job vacancies by profession."
)

all_seniorities = ["Entry-Level", "Mid-Level", "Senior/Lead"]
selected_seniority = st.sidebar.multiselect(
    "Seniority Level:",
    options=all_seniorities,
    default=all_seniorities,
    help="Filter compensation and openings by career stage."
)

all_sectors = sorted(base_job_df["industry_sector"].unique().tolist())
selected_sectors = st.sidebar.multiselect(
    "Industry Sector:",
    options=all_sectors,
    default=all_sectors,
    help="Filter vacancies by industrial domain."
)

skill_query = st.sidebar.text_input(
    "🔍 Search Required Skill:",
    placeholder="e.g. PyTorch, SQL, RAG",
    help="Filter job postings by specific technical skill keyword."
)

# Export Data Section in Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 📥 Export Processed Data")

# Compute current snapshot for export
acad_filtered = base_acad_df[base_acad_df["curriculum_name"].isin(selected_curricula)] if selected_curricula else base_acad_df
job_filtered = base_job_df[
    (base_job_df["job_title"].isin(selected_roles if selected_roles else all_roles)) &
    (base_job_df["seniority_level"].isin(selected_seniority if selected_seniority else all_seniorities)) &
    (base_job_df["industry_sector"].isin(selected_sectors if selected_sectors else all_sectors))
]
acad_skills = get_academic_skills_coverage(acad_filtered)
job_skills = get_skill_demand_counts(job_filtered)
mismatch_export = compute_skill_mismatch_metrics(acad_skills, job_skills)

csv_acad = acad_filtered.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="📄 Download Academic Data (CSV)",
    data=csv_acad,
    file_name="academic_supply_data.csv",
    mime="text/csv",
    use_container_width=True
)

csv_job = job_filtered.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="📄 Download Job Demand Data (CSV)",
    data=csv_job,
    file_name="job_demand_data.csv",
    mime="text/csv",
    use_container_width=True
)

csv_mismatch = mismatch_export.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="⚖️ Download Mismatch Matrix (CSV)",
    data=csv_mismatch,
    file_name="skill_mismatch_analysis.csv",
    mime="text/csv",
    use_container_width=True
)

st.sidebar.markdown(
    """
    <div style="font-size: 0.75rem; color: rgba(255, 255, 255, 0.7) !important; margin-top: 25px; line-height: 1.4;">
        Design System: Crimson Soft Light<br>
        Version: 2.0.0 Enterprise UI
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Content Canvas Header ---
st.markdown(
    """
    <div style="margin-bottom: 22px;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <div style="background-color: #801235; color: #FFFFFF; border-radius: 10px; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold;">
                🍷
            </div>
            <div>
                <h1 style="color: #2B2B2B; margin: 0; font-size: 1.95rem; font-weight: 800; letter-spacing: -0.02em;">
                    AI & Data Science Market Dashboard
                </h1>
                <p style="color: #6C757D; margin: 3px 0 0 0; font-size: 0.95rem;">
                    Measuring academic supply, labor market demand, and skill mismatch with Crimson Soft Light analytics.
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Interactive 3-Tab System ---
tab1, tab2, tab3 = st.tabs([
    "🎓 Tab 1: Academic Supply & Skills",
    "💼 Tab 2: Job Demand & Salary",
    "⚖️ Tab 3: Skill Mismatch"
])

with tab1:
    render_tab_academic(selected_curricula=selected_curricula)

with tab2:
    render_tab_demand(
        selected_roles=selected_roles,
        selected_seniority=selected_seniority,
        selected_sectors=selected_sectors,
        skill_search=skill_query
    )

with tab3:
    render_tab_mismatch(
        selected_curricula=selected_curricula,
        selected_roles=selected_roles,
        selected_seniority=selected_seniority,
        selected_sectors=selected_sectors
    )

# --- Open Data Citations & International Ecosystem Reference Expander ---
st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
with st.expander("📚 Open Data Repositories, Citations & International Benchmarks", expanded=False):
    render_tab_global()
