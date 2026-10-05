"""
Tab 1: Academic Supply & Skills (Academic Supply Side)
Visualizes curriculum output, core courses & credit weights,
graduate employment timelines, and tuition fee structures with Crimson Soft Light aesthetics.
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
from data.academic_supply import (
    get_academic_curricula_df,
    get_curriculum_timeline_df,
    get_core_courses_matrix,
    get_academic_skills_coverage
)

def render_tab_academic(selected_curricula: list = None):
    """Renders Tab 1: Academic Supply Side Analytics."""
    # Load raw data
    curricula_df = get_academic_curricula_df()
    timeline_df = get_curriculum_timeline_df(curricula_df)
    courses_df = get_core_courses_matrix()
    
    # Filter data based on selected curricula
    if selected_curricula and len(selected_curricula) > 0:
        curricula_df = curricula_df[curricula_df["curriculum_name"].isin(selected_curricula)]
        timeline_df = timeline_df[timeline_df["curriculum_name"].isin(selected_curricula)]
        courses_df = courses_df[courses_df["curriculum_name"].isin(selected_curricula)]
        
    render_section_header(
        title="Academic Supply & University Talent Pipeline",
        subtitle="Tracking graduate volumes, curriculum competency structures, employment outcomes, and tuition costs.",
        badge="Supply Side Intelligence"
    )
    
    # --- Top KPI Metrics (Crimson Soft Light Accents) ---
    total_graduates = int(curricula_df["total_accumulated_graduates"].sum()) if not curricula_df.empty else 0
    avg_tuition = curricula_df["tuition_fee_total_thb"].mean() if not curricula_df.empty else 0
    avg_emp_y1 = (curricula_df["emp_rate_year_1"].mean() * 100) if not curricula_df.empty else 0
    total_programs = len(curricula_df)
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    with kpi_col1:
        render_kpi_card(
            title="Total Graduates (5-Yr)",
            value=f"{total_graduates:,}",
            subtext=f"Across {total_programs} tracked programs",
            icon="🎓",
            delta="+14.2% YoY",
            delta_type="positive",
            accent_color="crimson"
        )
    with kpi_col2:
        render_kpi_card(
            title="Avg Program Tuition",
            value=f"฿{avg_tuition:,.0f}",
            subtext="Total degree cost",
            icon="💰",
            delta="THB",
            delta_type="neutral",
            accent_color="yellow"
        )
    with kpi_col3:
        render_kpi_card(
            title="Avg Year-1 Employment",
            value=f"{avg_emp_y1:.1f}%",
            subtext="First year post-grad",
            icon="💼",
            delta="High Placement",
            delta_type="positive",
            accent_color="blue"
        )
    with kpi_col4:
        render_kpi_card(
            title="Active Programs",
            value=f"{total_programs}",
            subtext="B.Sc. & M.Sc. degrees",
            icon="🏫",
            delta="Accredited",
            delta_type="neutral",
            accent_color="pink"
        )

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    
    # --- Row 1: Graph 1.1 & Graph 1.2 ---
    col1, col2 = st.columns(2)
    
    with col1:
        # Graph 1.1: Curriculum Output
        if not timeline_df.empty:
            source_g1 = "MHESI Higher Education Information Center & University Registrars (2021–2025)"
            fig_output = px.bar(
                timeline_df,
                x="year",
                y="graduates",
                color="curriculum_name",
                title="Graph 1.1: 5-Year Curriculum Graduate Output",
                labels={"graduates": "Number of Graduates", "year": "Academic Year", "curriculum_name": "Program"},
                barmode="stack",
                color_discrete_sequence=PLOTLY_CHART_COLORS
            )
            fig_output.update_layout(
                xaxis=dict(type='category'),
                legend=dict(orientation="h", yanchor="bottom", y=-0.35, xanchor="center", x=0.5)
            )
            apply_crimson_theme(fig_output, source=source_g1, height=440)
            st.plotly_chart(fig_output, use_container_width=True)
            render_source_caption(source_g1)
        else:
            st.info("No curriculum selected.")
            
    with col2:
        # Graph 1.2: Core Required Courses & Skill Matrix
        if not courses_df.empty:
            source_g2 = "Thai University Curriculum Handbooks & TQF Course Specifications"
            skill_credits = courses_df.groupby("skill")["credits"].sum().reset_index().sort_values(by="credits", ascending=True)
            fig_skills = px.bar(
                skill_credits,
                x="credits",
                y="skill",
                orientation="h",
                title="Graph 1.2: Learned Skill Weight (Aggregated Credits)",
                labels={"credits": "Total Credit Hours Taught", "skill": "Core Skill Competency"},
                color="credits",
                color_continuous_scale=["#FFDEEB", "#C9184A", "#801235"]
            )
            fig_skills.update_coloraxes(showscale=False)
            fig_skills.update_traces(hovertemplate="<b>%{y}</b><br>Credit Weight: %{x} hrs<extra></extra>")
            apply_crimson_theme(fig_skills, source=source_g2, height=440)
            st.plotly_chart(fig_skills, use_container_width=True)
            render_source_caption(source_g2)
        else:
            st.info("No course data available.")

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # --- Row 2: Graph 1.3 & Graph 1.4 ---
    col3, col4 = st.columns(2)
    
    with col3:
        # Graph 1.3: Graduate Employment Timeline
        if not curricula_df.empty:
            source_g3 = "MHESI Graduate Employment Status Survey & University Alumni Tracer Reports"
            emp_records = []
            for _, row in curricula_df.iterrows():
                emp_records.append({"curriculum_name": row["curriculum_name"], "Timeline": "Year 1", "Employment_Rate": row["emp_rate_year_1"] * 100})
                emp_records.append({"curriculum_name": row["curriculum_name"], "Timeline": "Year 2", "Employment_Rate": row["emp_rate_year_2"] * 100})
                emp_records.append({"curriculum_name": row["curriculum_name"], "Timeline": "Year 3", "Employment_Rate": row["emp_rate_year_3"] * 100})
            emp_df = pd.DataFrame(emp_records)
            
            fig_emp = px.line(
                emp_df,
                x="Timeline",
                y="Employment_Rate",
                color="curriculum_name",
                markers=True,
                title="Graph 1.3: Post-Graduation Employment Timeline (% Employed)",
                labels={"Employment_Rate": "Employment Rate (%)", "Timeline": "Years Post-Graduation", "curriculum_name": "Program"},
                color_discrete_sequence=PLOTLY_CHART_COLORS
            )
            fig_emp.update_yaxes(range=[70, 102])
            fig_emp.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.35, xanchor="center", x=0.5))
            apply_crimson_theme(fig_emp, source=source_g3, height=440)
            st.plotly_chart(fig_emp, use_container_width=True)
            render_source_caption(source_g3)
        else:
            st.info("No employment data available.")

    with col4:
        # Graph 1.4: Tuition Fee Structure Comparison
        if not curricula_df.empty:
            source_g4 = "University Official Tuition Fee Announcements & Academic Regulations"
            fig_tuition = px.bar(
                curricula_df.sort_values(by="tuition_fee_total_thb", ascending=True),
                x="tuition_fee_total_thb",
                y="curriculum_name",
                orientation="h",
                title="Graph 1.4: Program Tuition Fee Comparison (THB)",
                labels={"tuition_fee_total_thb": "Total Degree Cost (THB)", "curriculum_name": "Program"},
                color="degree_level",
                color_discrete_map={"Bachelor's": COLOR_PRIMARY_CRIMSON, "Master's": COLOR_ACCENT_ROSE}
            )
            fig_tuition.update_traces(
                hovertemplate="<b>%{y}</b><br>Total Cost: ฿%{x:,.0f}<br>Institution: %{customdata[0]}<extra></extra>",
                customdata=curricula_df.sort_values(by="tuition_fee_total_thb", ascending=True)[["institution"]]
            )
            fig_tuition.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5))
            apply_crimson_theme(fig_tuition, source=source_g4, height=440)
            st.plotly_chart(fig_tuition, use_container_width=True)
            render_source_caption(source_g4)
        else:
            st.info("No tuition data available.")

    # --- Interactive Curriculum Course Drilldown Table ---
    with st.expander("🔍 View Detailed Curriculum Course Syllabus & Skills Breakdown", expanded=False):
        st.dataframe(
            courses_df[["curriculum_name", "course_code", "course_name", "category", "credits", "skill"]].rename(
                columns={
                    "curriculum_name": "Academic Program",
                    "course_code": "Course Code",
                    "course_name": "Course Title",
                    "category": "Academic Domain",
                    "credits": "Credit Hours",
                    "skill": "Mapped Competency"
                }
            ),
            use_container_width=True,
            hide_index=True
        )
        render_source_caption("Official TQF-2 Program Documentation & University Course Catalogs")
