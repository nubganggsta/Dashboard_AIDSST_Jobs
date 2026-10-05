"""
Tab 3: Skill Mismatch Analysis (Supply vs. Demand Gap)
Synthesizes academic curriculum outputs with commercial job market requirements.
Features the Skill Alignment Index, Diverging Supply-Demand Bar,
2x2 Mismatch Matrix, and Automated Curriculum Recommendations with Crimson Soft Light aesthetics.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from utils.theme import (
    apply_crimson_theme,
    COLOR_PRIMARY_CRIMSON,
    COLOR_ACCENT_ROSE,
    COLOR_TEXT_PRIMARY,
    COLOR_TEXT_SECONDARY,
    COLOR_NEUTRAL_GRID
)
from modules.components import render_kpi_card, render_section_header, render_source_caption
from data.academic_supply import get_academic_curricula_df, get_academic_skills_coverage
from data.job_demand import generate_job_demand_df, get_skill_demand_counts
from utils.calculations import compute_skill_mismatch_metrics, calculate_scorecard_summary

def render_tab_mismatch(
    selected_curricula: list = None,
    selected_roles: list = None,
    selected_seniority: list = None,
    selected_sectors: list = None
):
    """Renders Tab 3: Skill Mismatch Analytics & Matrix."""
    # Retrieve filtered academic data
    curricula_df = get_academic_curricula_df()
    if selected_curricula and len(selected_curricula) > 0:
        curricula_df = curricula_df[curricula_df["curriculum_name"].isin(selected_curricula)]
    academic_skills_df = get_academic_skills_coverage(curricula_df)

    # Retrieve filtered demand data
    demand_df = generate_job_demand_df()
    if selected_roles and len(selected_roles) > 0:
        demand_df = demand_df[demand_df["job_title"].isin(selected_roles)]
    if selected_seniority and len(selected_seniority) > 0:
        demand_df = demand_df[demand_df["seniority_level"].isin(selected_seniority)]
    if selected_sectors and len(selected_sectors) > 0:
        demand_df = demand_df[demand_df["industry_sector"].isin(selected_sectors)]
    demand_skills_df = get_skill_demand_counts(demand_df)

    # Merge and calculate mismatch metrics
    mismatch_df = compute_skill_mismatch_metrics(academic_skills_df, demand_skills_df)
    scorecard = calculate_scorecard_summary(mismatch_df)

    render_section_header(
        title="Skill Mismatch & Higher Education Alignment Matrix",
        subtitle="Comparing academic curriculum coverage against employer technical requirements to identify critical curriculum gaps.",
        badge="Supply vs Demand Gap Analytics"
    )

    # --- Top Metric Scorecards (Crimson Soft Light Accents) ---
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        render_kpi_card(
            title="Skill Alignment Index",
            value=f"{scorecard['alignment_index_pct']}%",
            subtext="Curriculum-to-Market match",
            icon="🎯",
            delta="Target: 70%",
            delta_type="positive" if scorecard['alignment_index_pct'] >= 70 else "negative",
            accent_color="crimson"
        )
    with kpi2:
        render_kpi_card(
            title="Critical Deficit Skills",
            value=f"{scorecard['critical_deficit_count']}",
            subtext="High market demand, low supply",
            icon="🚨",
            delta="Urgent Action Required",
            delta_type="negative" if scorecard['critical_deficit_count'] > 0 else "positive",
            accent_color="pink"
        )
    with kpi3:
        render_kpi_card(
            title="Oversupplied / Niche",
            value=f"{scorecard['oversupplied_count']}",
            subtext="Taught > commercial demand",
            icon="⚠️",
            delta="Rebalance to Electives",
            delta_type="neutral",
            accent_color="yellow"
        )
    with kpi4:
        render_kpi_card(
            title="Top Deficit Skill",
            value=f"{scorecard['top_deficit_skill']}",
            subtext="Largest unmet talent demand",
            icon="🔥",
            delta="Largest Gap",
            delta_type="negative",
            accent_color="blue"
        )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # --- Row 1: Graph 3.1 & Graph 3.2 ---
    col1, col2 = st.columns(2)

    with col1:
        # Graph 3.1: Supply vs. Demand Skill Comparison (Grouped Bar Chart)
        source_g31 = "Cross-Analysis: MHESI University Curricula Coverage vs. Active Tech Job Market Postings"
        sorted_mismatch = mismatch_df.sort_values(by="demand_percentage", ascending=True).tail(12)
        
        fig_comp = go.Figure()
        
        # Academic Supply Bars (Deep Navy)
        fig_comp.add_trace(go.Bar(
            y=sorted_mismatch["skill"],
            x=sorted_mismatch["academic_supply_pct"],
            name="Academic Supply (% Curricula)",
            orientation="h",
            marker=dict(color="#1D3557", opacity=0.90),
            hovertemplate="<b>%{y}</b><br>Academic Coverage: %{x:.1f}%<extra></extra>"
        ))
        
        # Job Market Demand Bars (Primary Crimson)
        fig_comp.add_trace(go.Bar(
            y=sorted_mismatch["skill"],
            x=sorted_mismatch["demand_percentage"],
            name="Job Market Demand (% Postings)",
            orientation="h",
            marker=dict(color="#801235", opacity=0.90),
            hovertemplate="<b>%{y}</b><br>Market Demand: %{x:.1f}%<extra></extra>"
        ))

        fig_comp.update_layout(
            title="Graph 3.1: Supply vs. Demand Skill Overlay (% Comparison)",
            barmode="group",
            xaxis_title="Coverage / Demand Percentage (%)",
            yaxis_title="Technical Skill",
            legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
        )
        apply_crimson_theme(fig_comp, source=source_g31, height=480)
        st.plotly_chart(fig_comp, use_container_width=True)
        render_source_caption(source_g31)

    with col2:
        # Graph 3.2: Skill Mismatch Matrix (2x2 Matrix Scatter)
        source_g32 = "Supply-Demand Gap Synthesis Model (Academic Syllabus vs. Commercial Hiring Demand)"
        fig_scatter = px.scatter(
            mismatch_df,
            x="academic_supply_pct",
            y="demand_percentage",
            text="skill",
            color="quadrant",
            size=[18] * len(mismatch_df),
            title="Graph 3.2: 2×2 Skill Mismatch Matrix (Supply vs. Demand)",
            labels={
                "academic_supply_pct": "Academic Coverage Supply (%)",
                "demand_percentage": "Job Market Demand (%)",
                "quadrant": "Classification"
            },
            color_discrete_map={
                "Core Essentials (High Supply / High Demand)": "#2A9D8F",
                "Urgent Curriculum Gap (Low Supply / High Demand)": "#801235",
                "Niche / Academic Focus (High Supply / Low Demand)": "#D4A373",
                "Specialized / Low Volume (Low Supply / Low Demand)": "#6C757D"
            }
        )

        # Add quadrant threshold reference lines (at 30%)
        fig_scatter.add_vline(x=30, line_dash="dash", line_color="#CED4DA", line_width=1.5)
        fig_scatter.add_hline(y=30, line_dash="dash", line_color="#CED4DA", line_width=1.5)

        # Quadrant background annotation labels with soft badges
        fig_scatter.add_annotation(x=15, y=75, text="🚨 <b>URGENT GAPS</b><br>(High Demand / Low Supply)", showarrow=False, font=dict(color="#801235", size=10), bgcolor="rgba(255, 222, 235, 0.75)", bordercolor="#E63946", borderwidth=1, borderpad=4)
        fig_scatter.add_annotation(x=75, y=75, text="✅ <b>CORE ESSENTIALS</b><br>(High Demand / High Supply)", showarrow=False, font=dict(color="#2A9D8F", size=10), bgcolor="rgba(208, 235, 255, 0.75)", bordercolor="#2A9D8F", borderwidth=1, borderpad=4)
        fig_scatter.add_annotation(x=75, y=12, text="⚠️ <b>NICHE / ACADEMIC</b><br>(Low Demand / High Supply)", showarrow=False, font=dict(color="#B45309", size=10), bgcolor="rgba(254, 243, 199, 0.75)", bordercolor="#F59E0B", borderwidth=1, borderpad=4)
        fig_scatter.add_annotation(x=15, y=12, text="ℹ️ <b>SPECIALIZED</b><br>(Low Demand / Low Supply)", showarrow=False, font=dict(color="#6C757D", size=10), bgcolor="rgba(233, 236, 239, 0.75)", bordercolor="#CED4DA", borderwidth=1, borderpad=4)

        fig_scatter.update_traces(
            textposition="top center",
            textfont=dict(size=10, color="#2B2B2B"),
            hovertemplate="<b>%{text}</b><br>Academic Supply: %{x:.1f}%<br>Market Demand: %{y:.1f}%<br>Quadrant: %{customdata[0]}<extra></extra>",
            customdata=mismatch_df[["quadrant"]]
        )
        fig_scatter.update_layout(
            xaxis=dict(range=[-5, 105]),
            yaxis=dict(range=[-5, 105]),
            legend=dict(orientation="h", yanchor="bottom", y=-0.35, xanchor="center", x=0.5)
        )
        apply_crimson_theme(fig_scatter, source=source_g32, height=480)
        st.plotly_chart(fig_scatter, use_container_width=True)
        render_source_caption(source_g32)

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # --- Section: Actionable Recommendations Table ---
    render_section_header(
        title="Actionable Curriculum Recommendations for Universities",
        subtitle="Data-driven suggestions for curriculum revision, faculty training, and student upskilling programs.",
        badge="Strategic Curriculum Guidance"
    )

    # Filter controls for recommendation table
    rec_col1, rec_col2 = st.columns([1, 3])
    with rec_col1:
        status_filter = st.selectbox(
            "Filter by Gap Classification:",
            options=["All Statuses", "Critical Deficit", "Well-Aligned", "Over-Supplied / Niche", "Moderate Gap"],
            index=0
        )
        
    filtered_recs = mismatch_df.copy()
    if status_filter != "All Statuses":
        filtered_recs = filtered_recs[filtered_recs["status"] == status_filter]

    # Present formatted recommendations
    display_recs = filtered_recs[[
        "skill", "status", "academic_supply_pct", "demand_percentage", "gap_delta", "recommendation"
    ]].rename(
        columns={
            "skill": "Skill / Technology",
            "status": "Mismatch Status",
            "academic_supply_pct": "Academic Coverage (%)",
            "demand_percentage": "Market Demand (%)",
            "gap_delta": "Gap Delta (+Deficit / -Surplus)",
            "recommendation": "Strategic Curriculum Action Plan"
        }
    )

    st.dataframe(
        display_recs,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Gap Delta (+Deficit / -Surplus)": st.column_config.NumberColumn(
                format="%+.1f%%"
            ),
            "Academic Coverage (%)": st.column_config.NumberColumn(
                format="%.1f%%"
            ),
            "Market Demand (%)": st.column_config.NumberColumn(
                format="%.1f%%"
            ),
        }
    )
    render_source_caption("Automated Skill Gap Algorithmic Model & Curriculum Optimization Framework")
    
    return mismatch_df
