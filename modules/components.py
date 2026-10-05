"""
Reusable UI Components, Metric KPI Cards, and Custom CSS Injection
"""

import streamlit as st

def inject_custom_css():
    """Injects high-end modern tech dark mode CSS styling."""
    st.markdown(
        """
        <style>
        /* General App Theme Overrides */
        .stApp {
            background-color: #0f172a;
            color: #f8fafc;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        
        /* Metric KPI Card */
        .kpi-card {
            background: linear-gradient(135deg, #1e293b 0%, #172033 100%);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px 22px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
            transition: transform 0.2s ease, border-color 0.2s ease;
            margin-bottom: 15px;
        }
        .kpi-card:hover {
            transform: translateY(-2px);
            border-color: #38bdf8;
        }
        .kpi-title {
            color: #94a3b8;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 600;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .kpi-value {
            color: #f8fafc;
            font-size: 1.85rem;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 4px;
        }
        .kpi-subtext {
            color: #64748b;
            font-size: 0.80rem;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .kpi-delta-positive {
            color: #34d399;
            font-weight: 600;
        }
        .kpi-delta-negative {
            color: #f87171;
            font-weight: 600;
        }
        .kpi-delta-neutral {
            color: #38bdf8;
            font-weight: 600;
        }

        /* Section Title Badge */
        .section-badge {
            background-color: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
            border-radius: 6px;
            padding: 3px 10px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: inline-block;
            margin-bottom: 8px;
        }
        
        /* Table and Chart Containers */
        .chart-box {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 20px;
        }
        
        /* Custom alert box */
        .info-callout {
            background-color: rgba(30, 41, 59, 0.8);
            border-left: 4px solid #38bdf8;
            border-radius: 0 8px 8px 0;
            padding: 12px 18px;
            margin: 15px 0;
            font-size: 0.9rem;
            color: #e2e8f0;
        }
        
        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #0b1120;
            border-right: 1px solid #1e293b;
        }
        
        /* Tab styling */
        button[data-baseweb="tab"] {
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            color: #94a3b8 !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #38bdf8 !important;
            border-bottom-color: #38bdf8 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def render_kpi_card(title: str, value: str, subtext: str = "", icon: str = "📊", delta: str = None, delta_type: str = "neutral"):
    """Renders a sleek HTML KPI metric card."""
    delta_class = f"kpi-delta-{delta_type}"
    delta_html = f'<span class="{delta_class}">{delta}</span> • ' if delta else ""
    
    html = f"""
    <div class="kpi-card">
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
    """Renders section header with an optional category badge."""
    badge_html = f'<div class="section-badge">{badge}</div><br>' if badge else ""
    st.markdown(
        f"""
        <div style="margin-top: 10px; margin-bottom: 18px;">
            {badge_html}
            <h3 style="color: #f8fafc; margin: 0 0 6px 0; font-weight: 700; font-size: 1.35rem;">{title}</h3>
            <p style="color: #94a3b8; margin: 0; font-size: 0.90rem;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_source_caption(source: str):
    """Renders a sleek HTML/Streamlit data source caption below charts or tables."""
    st.markdown(
        f"<div style='font-size: 0.78rem; color: #94a3b8; margin-top: -10px; margin-bottom: 14px;'>"
        f"📌 <b>Data Source:</b> <i>{source}</i></div>",
        unsafe_allow_html=True
    )

