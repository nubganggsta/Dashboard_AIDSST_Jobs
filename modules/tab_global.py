"""
Global & Regional Market Ecosystem & Open Data References
Implements macro labor metrics, multi-region salary comparisons,
degree requirement distributions, categorized skill taxonomy, and open data citations.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.theme import (
    apply_dark_theme,
    COLOR_PRIMARY,
    COLOR_SECONDARY,
    COLOR_ACCENT,
    COLOR_WARNING,
    COLOR_INFO,
    PLOTLY_CHART_COLORS
)
from modules.components import render_kpi_card, render_section_header
from data.market_overview import (
    MARKET_OVERVIEW_STATS,
    get_salary_by_region_df,
    get_degree_requirements_df,
    SKILL_DEMAND_TAXONOMY,
    HIRING_COMPANIES_BY_SECTOR,
    OPEN_DATA_REPOSITORIES
)

def render_tab_global():
    """Renders Global & Regional Market Overview & Open Data Specifications."""
    render_section_header(
        title="Global & Regional Benchmark Ecosystem",
        subtitle="Comparing international talent pipelines, cross-regional compensation, minimum degree standards, and open data citations.",
        badge="Global Benchmarking & References"
    )

    # --- Macro Key Metric Cards ---
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            title="Total US Market Demand",
            value=f"{MARKET_OVERVIEW_STATS['us_open_positions']:,}",
            subtext="BLS 10-Yr Outlook",
            icon="🇺🇸",
            delta=f"+{MARKET_OVERVIEW_STATS['us_projected_growth_10yr']} 10-Yr",
            delta_type="positive"
        )
    with col2:
        render_kpi_card(
            title="Global Annual Grads",
            value=f"{MARKET_OVERVIEW_STATS['global_annual_graduates']:,}",
            subtext="Data Sci, Stats & ML",
            icon="🌐",
            delta="Worldwide",
            delta_type="neutral"
        )
    with col3:
        render_kpi_card(
            title="TH Annual Specialists",
            value=f"{MARKET_OVERVIEW_STATS['thailand_annual_graduates_datasci_stat']:,}",
            subtext=f"Out of {MARKET_OVERVIEW_STATS['thailand_annual_graduates_stem']:,} STEM",
            icon="🇹🇭",
            delta="MHESI Portal",
            delta_type="positive"
        )
    with col4:
        render_kpi_card(
            title="Primary Qualification",
            value="Bachelor's",
            subtext="58% of global job postings",
            icon="📜",
            delta="Entry Baseline",
            delta_type="neutral"
        )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # --- Row 1: Regional Salaries & Degree Distribution ---
    col_sal, col_deg = st.columns([3, 2])

    with col_sal:
        sal_df = get_salary_by_region_df()
        
        # Melt for visualization
        melted_sal = pd.melt(
            sal_df,
            id_vars=["region", "currency", "unit"],
            value_vars=["normalized_entry_usd_yr", "normalized_senior_usd_yr"],
            var_name="level_col",
            value_name="usd_per_year"
        )
        melted_sal["Experience Level"] = melted_sal["level_col"].map({
            "normalized_entry_usd_yr": "Entry-Level (0-2 Yrs)",
            "normalized_senior_usd_yr": "Senior / Lead (5+ Yrs)"
        })

        fig_reg_sal = px.bar(
            melted_sal,
            x="region",
            y="usd_per_year",
            color="Experience Level",
            barmode="group",
            title="International Salary Comparison (Normalized to USD / Year)",
            labels={"usd_per_year": "Annual Compensation (USD Equiv.)", "region": "Region"},
            color_discrete_map={
                "Entry-Level (0-2 Yrs)": COLOR_PRIMARY,
                "Senior / Lead (5+ Yrs)": COLOR_ACCENT
            }
        )
        fig_reg_sal.update_traces(
            hovertemplate="<b>%{x}</b> (%{data.name})<br>Normalized: $%{y:,.0f} USD/yr<extra></extra>"
        )
        fig_reg_sal.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5))
        apply_dark_theme(fig_reg_sal, height=430)
        st.plotly_chart(fig_reg_sal, use_container_width=True)

    with col_deg:
        deg_df = get_degree_requirements_df()
        fig_donut = px.pie(
            deg_df,
            names="degree",
            values="percentage",
            hole=0.55,
            title="Minimum Degree Requirements in Postings (%)",
            color="degree",
            color_discrete_map={
                "Bachelor's Degree": COLOR_PRIMARY,
                "Master's Degree": "#818cf8",
                "PhD / Doctorate": "#c084fc"
            }
        )
        fig_donut.update_traces(
            textinfo="percent+label",
            hovertemplate="<b>%{label}</b><br>Share: %{percent}<extra></extra>"
        )
        fig_donut.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5))
        apply_dark_theme(fig_donut, height=430)
        st.plotly_chart(fig_donut, use_container_width=True)

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # --- Row 2: Skill Taxonomy & Hiring Ecosystem Directory ---
    render_section_header(
        title="Categorized Skill Taxonomy & Global Hiring Ecosystem",
        subtitle="Standardized classification of competencies and key international & domestic employers.",
        badge="Market Landscape"
    )

    tax_col, comp_col = st.columns([1, 1])

    with tax_col:
        st.markdown("#### 🛠️ In-Demand Skill Taxonomy")
        for cat in SKILL_DEMAND_TAXONOMY:
            skill_badges = " ".join([f"<span style='background-color:#1e293b; border:1px solid #334155; border-radius:6px; padding:3px 8px; margin-right:4px; font-size:0.8rem; color:#38bdf8;'>{s}</span>" for s in cat["skills"]])
            st.markdown(
                f"""
                <div style="background-color: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px;">
                    <div style="font-weight: 600; color: #f8fafc; font-size: 0.95rem; margin-bottom: 6px;">
                        {cat['icon']} {cat['category']}
                    </div>
                    <div>{skill_badges}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    with comp_col:
        st.markdown("#### 🏢 Hiring Ecosystem by Sector")
        for sector, companies in HIRING_COMPANIES_BY_SECTOR.items():
            comp_badges = " ".join([f"<span style='background-color:#1e293b; border:1px solid #334155; border-radius:6px; padding:3px 8px; margin-right:4px; font-size:0.8rem; color:#34d399;'>{c}</span>" for c in companies])
            st.markdown(
                f"""
                <div style="background-color: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px;">
                    <div style="font-weight: 600; color: #f8fafc; font-size: 0.95rem; margin-bottom: 6px;">
                        {sector}
                    </div>
                    <div>{comp_badges}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # --- Section: Open Data Repositories & References ---
    render_section_header(
        title="Open Data Repositories & Citation Index",
        subtitle="Direct links and methodology descriptions for authoritative labor statistics and survey benchmarks.",
        badge="Official References"
    )

    data_cols = st.columns(2)
    for idx, repo in enumerate(OPEN_DATA_REPOSITORIES):
        col = data_cols[idx % 2]
        with col:
            st.markdown(
                f"""
                <div style="background-color: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 16px; margin-bottom: 14px;">
                    <h5 style="color: #38bdf8; margin: 0 0 4px 0;"><a href="{repo['url']}" target="_blank" style="color: #38bdf8; text-decoration: none;">{repo['name']} ↗</a></h5>
                    <div style="color: #94a3b8; font-size: 0.8rem; margin-bottom: 8px;"><strong>Source:</strong> {repo['source']}</div>
                    <div style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.4;">{repo['description']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
