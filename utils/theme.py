"""
Crimson Soft Light Theme Utilities & Plotly Styling Configuration
Implements the Burgundy / Crimson Soft Light enterprise UI styling system.
"""

import plotly.graph_objects as go
import plotly.express as px

# Specification Color Palette
COLOR_SIDEBAR_BG = "#800020"       # Deep Crimson / Burgundy
COLOR_CANVAS_BG = "#F8F9FA"        # Soft Cream / Light Off-White
COLOR_CARD_BG = "#FFFFFF"          # Pure White
COLOR_TEXT_PRIMARY = "#2B2B2B"     # Dark Charcoal
COLOR_TEXT_SECONDARY = "#6C757D"   # Soft Muted Gray
COLOR_SIDEBAR_TEXT = "#FFFFFF"     # Pure White

# Accent & Data Viz Tokens
COLOR_PRIMARY_CRIMSON = "#801235"  # Main Chart Color / Active Controls
COLOR_ACCENT_ROSE = "#E63946"      # Highlighting / Alert Elements
COLOR_PASTEL_YELLOW = "#FFF3BF"    # KPI Accent 1
COLOR_PASTEL_BLUE = "#D0EBFF"      # KPI Accent 2
COLOR_PASTEL_PINK = "#FFDEEB"      # KPI Accent 3
COLOR_NEUTRAL_GRID = "#E9ECEF"     # Plotly Chart Gridlines
COLOR_BORDER = "#E9ECEF"

# Rich Crimson / Burgundy Palette for charts
PLOTLY_CHART_COLORS = [
    "#801235",  # Primary Crimson
    "#E63946",  # Rose Accent
    "#1D3557",  # Deep Navy Contrast
    "#2A9D8F",  # Sage Teal
    "#D4A373",  # Warm Sand Gold
    "#B23A48",  # Medium Crimson
    "#C9184A",  # Berry Pink
    "#4A1525",  # Deep Burgundy
]

def apply_crimson_theme(fig: go.Figure, title: str = "", source: str = "", height: int = 420) -> go.Figure:
    """Applies modern Crimson Soft Light styling to a Plotly figure."""
    current_title = title or (fig.layout.title.text if fig.layout.title and fig.layout.title.text else "")
    
    title_dict = {}
    if current_title:
        clean_title = current_title if current_title.startswith("<b>") else f"<b>{current_title}</b>"
        title_dict["text"] = clean_title
        title_dict["font"] = {"size": 15, "color": COLOR_TEXT_PRIMARY, "family": "Inter, Prompt, sans-serif"}
        title_dict["x"] = 0.02
        title_dict["xanchor"] = "left"
        if source:
            title_dict["subtitle"] = {
                "text": f"📌 Data Source: {source}",
                "font": {"size": 11, "color": COLOR_TEXT_SECONDARY, "family": "Inter, Prompt, sans-serif"}
            }
    elif source:
        title_dict = {
            "subtitle": {
                "text": f"📌 Data Source: {source}",
                "font": {"size": 11, "color": COLOR_TEXT_SECONDARY, "family": "Inter, Prompt, sans-serif"}
            },
            "x": 0.02,
            "xanchor": "left"
        }

    top_margin = 72 if (current_title and source) else (50 if current_title else (35 if source else 25))

    layout_kwargs = {
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font": {"color": COLOR_TEXT_PRIMARY, "family": "Inter, Prompt, sans-serif", "size": 12},
        "height": height,
        "margin": {"l": 40, "r": 25, "t": top_margin, "b": 35},
        "legend": {
            "font": {"color": COLOR_TEXT_SECONDARY, "size": 11},
            "bgcolor": "rgba(255, 255, 255, 0.85)",
            "bordercolor": COLOR_NEUTRAL_GRID,
            "borderwidth": 1
        },
        "hoverlabel": {
            "bgcolor": COLOR_CARD_BG,
            "bordercolor": COLOR_PRIMARY_CRIMSON,
            "font": {"color": COLOR_TEXT_PRIMARY, "size": 12, "family": "Inter, sans-serif"}
        },
        "xaxis": {
            "gridcolor": COLOR_NEUTRAL_GRID,
            "zerolinecolor": COLOR_NEUTRAL_GRID,
            "linecolor": COLOR_NEUTRAL_GRID,
            "tickfont": {"color": COLOR_TEXT_SECONDARY},
            "title_font": {"color": COLOR_TEXT_PRIMARY, "size": 12}
        },
        "yaxis": {
            "gridcolor": COLOR_NEUTRAL_GRID,
            "zerolinecolor": COLOR_NEUTRAL_GRID,
            "linecolor": COLOR_NEUTRAL_GRID,
            "tickfont": {"color": COLOR_TEXT_SECONDARY},
            "title_font": {"color": COLOR_TEXT_PRIMARY, "size": 12}
        }
    }
    
    if title_dict:
        layout_kwargs["title"] = title_dict

    fig.update_layout(**layout_kwargs)
    return fig

# Alias for backwards compatibility
apply_dark_theme = apply_crimson_theme
