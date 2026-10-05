"""
Reusable UI Components, Metric KPI Cards, and Crimson Soft Light CSS
"""

import streamlit as st

def inject_custom_css():
    """Injects Crimson Soft Light (Burgundy) enterprise design system CSS."""
    st.markdown(
        """
        <style>
        /* Base App Canvas */
        .stApp {
            background-color: #F8F9FA;
            color: #2B2B2B;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Prompt', 'Sarabun', 'Segoe UI', Roboto, sans-serif;
        }

        /* Sidebar Styling (Deep Crimson / Burgundy) */
        section[data-testid="stSidebar"] {
            background-color: #800020 !important;
            border-right: 1px solid rgba(0, 0, 0, 0.1);
        }
        section[data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }
        section[data-testid="stSidebar"] .stSelectbox label,
        section[data-testid="stSidebar"] .stMultiSelect label,
        section[data-testid="stSidebar"] .stTextInput label {
            color: #FFFFFF !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
        }
        section[data-testid="stSidebar"] .stDownloadButton button {
            background-color: #FFFFFF !important;
            color: #800020 !important;
            border: none !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15) !important;
            transition: all 0.2s ease !important;
        }
        section[data-testid="stSidebar"] .stDownloadButton button:hover {
            background-color: #FFDEEB !important;
            color: #801235 !important;
            transform: translateY(-1px) !important;
        }

        /* Dropdown input fields inside sidebar */
        section[data-testid="stSidebar"] div[data-baseweb="select"] {
            background-color: rgba(255, 255, 255, 0.12) !important;
            border-radius: 8px !important;
            border: 1px solid rgba(255, 255, 255, 0.25) !important;
        }
        section[data-testid="stSidebar"] div[data-baseweb="select"] * {
            color: #FFFFFF !important;
        }
        section[data-testid="stSidebar"] div[data-baseweb="tag"] {
            background-color: rgba(255, 255, 255, 0.25) !important;
            border: none !important;
        }
        section[data-testid="stSidebar"] div[data-baseweb="tag"] * {
            color: #FFFFFF !important;
        }

        /* White Card Container */
        .white-card {
            background-color: #FFFFFF;
            border: 1px solid #E9ECEF;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
        }

        /* KPI Metric Cards */
        .kpi-card {
            background-color: #FFFFFF;
            border: 1px solid #E9ECEF;
            border-radius: 12px;
            padding: 18px 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            margin-bottom: 15px;
            position: relative;
            overflow: hidden;
        }
        .kpi-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(128, 18, 53, 0.08);
            border-color: #801235;
        }
        .kpi-accent-yellow {
            border-top: 4px solid #F59E0B;
        }
        .kpi-accent-blue {
            border-top: 4px solid #3B82F6;
        }
        .kpi-accent-pink {
            border-top: 4px solid #EC4899;
        }
        .kpi-accent-crimson {
            border-top: 4px solid #801235;
        }
        
        .kpi-title {
            color: #6C757D;
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 600;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .kpi-value {
            color: #2B2B2B;
            font-size: 1.85rem;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 4px;
        }
        .kpi-subtext {
            color: #6C757D;
            font-size: 0.80rem;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .kpi-delta-positive {
            color: #10B981;
            font-weight: 600;
        }
        .kpi-delta-negative {
            color: #E63946;
            font-weight: 600;
        }
        .kpi-delta-neutral {
            color: #801235;
            font-weight: 600;
        }

        /* Section Badges */
        .section-badge {
            background-color: rgba(128, 18, 53, 0.08);
            color: #801235;
            border: 1px solid rgba(128, 18, 53, 0.22);
            border-radius: 6px;
            padding: 3px 10px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: inline-block;
            margin-bottom: 8px;
        }

        /* Tab Navigation Bar */
        button[data-baseweb="tab"] {
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            color: #6C757D !important;
            padding: 10px 18px !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #801235 !important;
            border-bottom-color: #801235 !important;
        }

        /* Data table container styling */
        .stDataFrame {
            border: 1px solid #E9ECEF;
            border-radius: 8px;
            overflow: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def render_kpi_card(
    title: str,
    value: str,
    subtext: str = "",
    icon: str = "📊",
    delta: str = None,
    delta_type: str = "neutral",
    accent_color: str = "crimson"
):
    """Renders a modern Crimson Soft Light KPI card."""
    delta_class = f"kpi-delta-{delta_type}"
    delta_html = f'<span class="{delta_class}">{delta}</span> • ' if delta else ""
    accent_class = f"kpi-accent-{accent_color}"
    
    html = f"""
    <div class="kpi-card {accent_class}">
        <div class="kpi-title">
            <span>{title}</span>
            <span>{icon}</span>
        </div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-subtext">{delta_html}{subtext}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_section_header(title: str, subtitle: str = "", badge: str = ""):
    """Renders section header with Crimson Soft Light typography."""
    badge_html = f'<div class="section-badge">{badge}</div><br>' if badge else ""
    st.markdown(
        f"""
        <div style="margin-top: 10px; margin-bottom: 18px;">
            {badge_html}
            <h3 style="color: #2B2B2B; margin: 0 0 6px 0; font-weight: 700; font-size: 1.35rem;">{title}</h3>
            <p style="color: #6C757D; margin: 0; font-size: 0.90rem;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_source_caption(source: str):
    """Renders a clean data source caption below charts or tables."""
    st.markdown(
        f"<div style='font-size: 0.78rem; color: #6C757D; margin-top: -10px; margin-bottom: 14px;'>"
        f"📌 <b>Data Source:</b> <i>{source}</i></div>",
        unsafe_allow_html=True
    )
