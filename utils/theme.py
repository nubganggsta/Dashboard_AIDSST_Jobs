"""
Dark Mode Theme Utilities & Plotly Styling Configuration
Ensures cohesive modern tech aesthetics across all charts and UI components.
"""

import plotly.graph_objects as go
import plotly.express as px

# Color Palette Constants
COLOR_BG_DARK = "#0f172a"        # Slate 900
COLOR_SURFACE_DARK = "#1e293b"   # Slate 800
COLOR_SURFACE_HOVER = "#334155"  # Slate 700
COLOR_TEXT_LIGHT = "#f8fafc"     # Slate 50
COLOR_TEXT_MUTED = "#94a3b8"     # Slate 400
COLOR_BORDER = "#334155"         # Slate 700

COLOR_PRIMARY = "#38bdf8"        # Sky 400
COLOR_SECONDARY = "#34d399"      # Emerald 400
COLOR_ACCENT = "#a855f7"         # Purple 500
COLOR_WARNING = "#fbbf24"        # Amber 400
COLOR_DANGER = "#f87171"         # Rose 400
COLOR_INFO = "#60a5fa"           # Blue 400

PLOTLY_CHART_COLORS = [
    COLOR_PRIMARY,
    COLOR_SECONDARY,
    COLOR_ACCENT,
    COLOR_WARNING,
    COLOR_INFO,
    "#ec4899", # Pink
    "#f97316", # Orange
    "#14b8a6", # Teal
]

def apply_dark_theme(fig: go.Figure, title: str = "", source: str = "", height: int = 420) -> go.Figure:
    """Applies modern tech dark styling to a Plotly figure with optional title and data source subtitle."""
    current_title = title or (fig.layout.title.text if fig.layout.title and fig.layout.title.text else "")
    
    title_dict = {}
    if current_title:
        clean_title = current_title if current_title.startswith("<b>") else f"<b>{current_title}</b>"
        title_dict["text"] = clean_title
        title_dict["font"] = {"size": 15, "color": COLOR_TEXT_LIGHT, "family": "Inter, sans-serif"}
        title_dict["x"] = 0.02
        title_dict["xanchor"] = "left"
        if source:
            title_dict["subtitle"] = {
                "text": f"📌 Data Source: {source}",
                "font": {"size": 11, "color": COLOR_TEXT_MUTED, "family": "Inter, sans-serif"}
            }
    elif source:
        title_dict = {
            "subtitle": {
                "text": f"📌 Data Source: {source}",
                "font": {"size": 11, "color": COLOR_TEXT_MUTED, "family": "Inter, sans-serif"}
            },
            "x": 0.02,
            "xanchor": "left"
        }

    top_margin = 75 if (current_title and source) else (55 if current_title else (40 if source else 30))

    layout_kwargs = {
        "paper_bgcolor": COLOR_SURFACE_DARK,
        "plot_bgcolor": COLOR_SURFACE_DARK,
        "font": {"color": COLOR_TEXT_LIGHT, "family": "Inter, system-ui, sans-serif", "size": 12},
        "height": height,
        "margin": {"l": 40, "r": 30, "t": top_margin, "b": 40},
        "legend": {
            "font": {"color": COLOR_TEXT_MUTED, "size": 11},
            "bgcolor": "rgba(15, 23, 42, 0.6)",
            "bordercolor": COLOR_BORDER,
            "borderwidth": 1
        },
        "hoverlabel": {
            "bgcolor": COLOR_BG_DARK,
            "bordercolor": COLOR_PRIMARY,
            "font": {"color": COLOR_TEXT_LIGHT, "size": 12, "family": "Inter, sans-serif"}
        },
        "xaxis": {
            "gridcolor": "#26354a",
            "zerolinecolor": "#26354a",
            "linecolor": COLOR_BORDER,
            "tickfont": {"color": COLOR_TEXT_MUTED},
            "title_font": {"color": COLOR_TEXT_LIGHT, "size": 13}
        },
        "yaxis": {
            "gridcolor": "#26354a",
            "zerolinecolor": "#26354a",
            "linecolor": COLOR_BORDER,
            "tickfont": {"color": COLOR_TEXT_MUTED},
            "title_font": {"color": COLOR_TEXT_LIGHT, "size": 13}
        }
    }
    
    if title_dict:
        layout_kwargs["title"] = title_dict

    fig.update_layout(**layout_kwargs)
    return fig
