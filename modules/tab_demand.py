"""
Tab 2: Job Market Demand & Salary (Labor Market Demand Side)
Visualizes active job vacancies, hiring enterprise distributions,
in-demand technical competencies, and salary ranges across seniority levels in Crimson Soft Light.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.theme import (
    apply_crimson_theme,
    COLOR_PRIMARY_CRIMSON,
    COLOR_ACCENT_ROSE,
    PLOTLY_CHART_COLORS
)
from modules.components import render_kpi_card, render_section_header, render_source_caption
from data.job_demand import generate_job_demand_df, get_skill_demand_counts

def render_tab_demand(
    selected_roles: list = None,
    selected_seniority: list = None,
    selected_sectors: list = None,
    skill_search: str = ""
):
    """Renders Tab 2: Labor Market Demand Analytics."""
    # Base dataset
    raw_df = generate_job_demand_df()
    df = raw_df.copy()
    
    # Apply filters
    if selected_roles and len(selected_roles) > 0:
        df = df[df["job_title"].isin(selected_roles)]
    if selected_seniority and len(selected_seniority) > 0:
        df = df[df["seniority_level"].isin(selected_seniority)]
    if selected_sectors and len(selected_sectors) > 0:
        df = df[df["industry_sector"].isin(selected_sectors)]
    if skill_search:
        search_term = skill_search.strip().lower()
        df = df[df["required_skills"].apply(lambda skills: any(search_term in s.lower() for s in skills))]

    render_section_header(
        title="Labor Market Demand & Commercial Hiring Trends",
        subtitle="Exploring open vacancies, compensation structures, top hiring organizations, and real-world tech requirements.",
        badge="Demand Side Intelligence"
    )

    # --- Top KPI Metrics (Crimson Soft Light Accents) ---
    total_vacancies = len(df)
    entry_df = df[df["seniority_level"] == "Entry-Level"]
    avg_entry_salary = entry_df["salary_avg_thb"].mean() if not entry_df.empty else 0
    
    skill_demand_df = get_skill_demand_counts(df) if not df.empty else pd.DataFrame()
    top_skill = skill_demand_df.iloc[0]["skill"] if not skill_demand_df.empty else "N/A"
    top_skill_pct = skill_demand_df.iloc[0]["demand_percentage"] if not skill_demand_df.empty else 0
    top_company = df["company_name"].value_counts().idxmax() if not df.empty else "N/A"

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        render_kpi_card(
            title="Active Job Vacancies",
            value=f"{total_vacancies:,}",
            subtext=f"Sample postings",
            icon="💼",
            delta="Hiring Surge",
            delta_type="positive",
            accent_color="crimson"
        )
    with kpi2:
        render_kpi_card(
            title="Avg Entry Salary",
            value=f"฿{avg_entry_salary:,.0f}",
            subtext="Per month (0-2 Yrs exp)",
            icon="💵",
            delta="THB / Month",
            delta_type="neutral",
            accent_color="yellow"
        )
    with kpi3:
        render_kpi_card(
            title="#1 In-Demand Skill",
            value=f"{top_skill}",
            subtext=f"Found in {top_skill_pct:.1f}% of job postings",
            icon="⚡",
            delta="Most Requested",
            delta_type="positive",
            accent_color="pink"
        )
    with kpi4:
        render_kpi_card(
            title="Lead Employer",
            value=f"{top_company}",
            subtext="Most active hiring listings",
            icon="🏢",
            delta="Top Recruiter",
            delta_type="neutral",
            accent_color="blue"
        )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    if df.empty:
        st.warning("No job postings match the selected filter criteria. Try adjusting the sidebar filters.")
        return

    # --- Row 1: Graph 2.1 & Graph 2.2 ---
    col1, col2 = st.columns(2)
    
    with col1:
        # Graph 2.1: Job Openings Volume by Title & Industry
        source_g21 = "Thailand & SEA Tech Job Portals & Company Career Sites (Sample n=250 active postings)"
        treemap_df = df.groupby(["industry_sector", "job_title"]).size().reset_index(name="openings")
        fig_treemap = px.treemap(
            treemap_df,
            path=["industry_sector", "job_title"],
            values="openings",
            title="Graph 2.1: Vacancy Distribution by Industry & Job Title",
            color="openings",
            color_continuous_scale=["#FFF0F3", "#FF758F", "#C9184A", "#801235", "#4A1525"]
        )
        fig_treemap.update_coloraxes(showscale=False)
        fig_treemap.update_traces(
            hovertemplate="<b>%{label}</b><br>Active Openings: %{value}<br>Sector/Parent: %{parent}<extra></extra>"
        )
        apply_crimson_theme(fig_treemap, source=source_g21, height=440)
        st.plotly_chart(fig_treemap, use_container_width=True)
        render_source_caption(source_g21)

    with col2:
        # Graph 2.2: In-Demand Skill Breakdown (Horizontal Bar)
        source_g22 = "Employer Job Descriptions NLP Extraction & Industry Demand Analytics (2024–2026)"
        top_skills_df = skill_demand_df.head(12).sort_values(by="demand_percentage", ascending=True)
        fig_skills = px.bar(
            top_skills_df,
            x="demand_percentage",
            y="skill",
            orientation="h",
            title="Graph 2.2: Top In-Demand Technical Skills (% Postings)",
            labels={"demand_percentage": "% of Job Postings Requiring Skill", "skill": "Technical Competency"},
            color="demand_percentage",
            color_continuous_scale=["#FFDEEB", "#C9184A", "#801235"]
        )
        fig_skills.update_coloraxes(showscale=False)
        fig_skills.update_traces(
            hovertemplate="<b>%{y}</b><br>Demand Frequency: %{x:.1f}%<extra></extra>"
        )
        apply_crimson_theme(fig_skills, source=source_g22, height=440)
        st.plotly_chart(fig_skills, use_container_width=True)
        render_source_caption(source_g22)

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # --- Row 2: Graph 2.3 & Graph 2.4 ---
    col3, col4 = st.columns(2)
    
    with col3:
        # Graph 2.3: Hiring Companies & Volume by Seniority Level
        source_g23 = "Corporate Recruitment Data & LinkedIn Talent Insights Thailand"
        company_counts = df.groupby(["company_name", "seniority_level"]).size().reset_index(name="openings")
        top_companies = df["company_name"].value_counts().head(10).index.tolist()
        company_counts = company_counts[company_counts["company_name"].isin(top_companies)]
        
        fig_companies = px.bar(
            company_counts,
            x="openings",
            y="company_name",
            color="seniority_level",
            orientation="h",
            title="Graph 2.3: Top Hiring Enterprises by Seniority Level",
            labels={"openings": "Job Vacancies", "company_name": "Company", "seniority_level": "Seniority"},
            barmode="stack",
            color_discrete_map={
                "Entry-Level": COLOR_PRIMARY_CRIMSON,
                "Mid-Level": COLOR_ACCENT_ROSE,
                "Senior/Lead": "#1D3557"
            },
            category_orders={"company_name": top_companies[::-1]}
        )
        fig_companies.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5))
        apply_crimson_theme(fig_companies, source=source_g23, height=440)
        st.plotly_chart(fig_companies, use_container_width=True)
        render_source_caption(source_g23)

    with col4:
        # Graph 2.4: Salary Structure by Seniority Level (Box Plot)
        source_g24 = "Kaggle Global Data Science Salaries Dataset & Regional Tech Salary Surveys"
        fig_salary = px.box(
            df,
            x="seniority_level",
            y="salary_avg_thb",
            color="seniority_level",
            title="Graph 2.4: Monthly Salary Distribution by Seniority (THB)",
            labels={"salary_avg_thb": "Monthly Salary (THB)", "seniority_level": "Seniority Level"},
            color_discrete_map={
                "Entry-Level": COLOR_PRIMARY_CRIMSON,
                "Mid-Level": COLOR_ACCENT_ROSE,
                "Senior/Lead": "#1D3557"
            },
            category_orders={"seniority_level": ["Entry-Level", "Mid-Level", "Senior/Lead"]}
        )
        fig_salary.update_layout(showlegend=False)
        fig_salary.update_traces(
            hovertemplate="Seniority: %{x}<br>Avg Salary: ฿%{y:,.0f}<extra></extra>"
        )
        apply_crimson_theme(fig_salary, source=source_g24, height=440)
        st.plotly_chart(fig_salary, use_container_width=True)
        render_source_caption(source_g24)

    # --- Interactive Job Postings Data Explorer ---
    with st.expander("🔎 Browse Live Job Openings Repository", expanded=False):
        display_cols = ["job_id", "job_title", "company_name", "industry_sector", "seniority_level", "salary_min_thb", "salary_max_thb", "degree_required", "work_model"]
        preview_df = df[display_cols].copy()
        preview_df["salary_range_thb"] = preview_df.apply(lambda r: f"฿{r['salary_min_thb']:,} - ฿{r['salary_max_thb']:,}", axis=1)
        preview_df = preview_df.drop(columns=["salary_min_thb", "salary_max_thb"]).rename(
            columns={
                "job_id": "Job ID",
                "job_title": "Position",
                "company_name": "Company",
                "industry_sector": "Industry",
                "seniority_level": "Seniority",
                "salary_range_thb": "Salary (THB/mo)",
                "degree_required": "Education Required",
                "work_model": "Workplace Mode"
            }
        )
        st.dataframe(preview_df, use_container_width=True, hide_index=True)
        render_source_caption("Aggregated Tech Job Board Data Feeds & Enterprise Career Listings")
