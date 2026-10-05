"""
Main Streamlit Application:
AI, Data Science & Statistics Supply-Demand & Skill Mismatch Dashboard
"""

import streamlit as st
import pandas as pd
import io

# Page configuration
st.set_page_config(
    page_title="AI & Data Science Supply-Demand Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import custom styling and modules
from modules.components import inject_custom_css
from modules.tab_academic import render_tab_academic
from modules.tab_demand import render_tab_demand
from modules.tab_mismatch import render_tab_mismatch
from modules.tab_global import render_tab_global

from data.academic_supply import get_academic_curricula_df, get_academic_skills_coverage
from data.job_demand import generate_job_demand_df, get_skill_demand_counts
from utils.calculations import compute_skill_mismatch_metrics

# Inject high-end dark styling
inject_custom_css()

# --- Initialize Base Reference Data ---
@st.cache_data
def load_base_data():
    acad_df = get_academic_curricula_df()
    job_df = generate_job_demand_df()
    return acad_df, job_df

base_acad_df, base_job_df = load_base_data()

# --- Sidebar Controls & Cross-Filtering ---
st.sidebar.markdown(
    """
    <div style="padding: 10px 0 15px 0;">
        <h2 style="color: #38bdf8; margin: 0; font-size: 1.35rem; font-weight: 700;">📊 AIDSST Analytics</h2>
        <p style="color: #94a3b8; font-size: 0.8rem; margin: 2px 0 0 0;">Interactive Cross-Filtering Engine</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("### 🎓 Academic Supply Filters")
all_curricula = sorted(base_acad_df["curriculum_name"].unique().tolist())
selected_curricula = st.sidebar.multiselect(
    "Select Academic Programs:",
    options=all_curricula,
    default=all_curricula,
    help="Filters academic output trends and curriculum course matrices across all tabs."
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
    "🔍 Filter Postings by Skill Keyword:",
    placeholder="e.g. PyTorch, SQL, RAG",
    help="Filter postings containing specific keywords."
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
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 20px; line-height: 1.4;">
        Data Sources: MHESI Open Data Portal, US BLS, Kaggle Global Salaries, Stack Overflow Survey.<br>
        Version: 1.0.0 • Tech Dark Theme
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Application Header ---
st.markdown(
    """
    <div style="margin-bottom: 25px;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 2.2rem;">📊</span>
            <div>
                <h1 style="color: #f8fafc; margin: 0; font-size: 2.0rem; font-weight: 800; letter-spacing: -0.02em;">
                    AI, Data Science & Statistics Supply-Demand & Skill Mismatch Dashboard
                </h1>
                <p style="color: #94a3b8; margin: 4px 0 0 0; font-size: 1.0rem;">
                    Empowering higher education curriculum modernization, industrial recruitment strategy, and workforce upskilling.
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- 4 Interactive Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🎓 Tab 1: Academic Supply & Skills",
    "💼 Tab 2: Job Demand & Salary",
    "⚖️ Tab 3: Skill Mismatch Analysis",
    "🌐 Tab 4: Global Ecosystem & References"
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

with tab4:
    render_tab_global()
