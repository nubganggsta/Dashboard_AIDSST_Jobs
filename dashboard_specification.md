# 📄 Dashboard Refactoring & Styling Specification

**Target Developer Agent:** Antigravity  
**Task Domain:** Python Web Application Development / Data Visualization & UX Redesign  
**Technology Stack:** Python 3.10+ (Dash / Streamlit), Plotly Express & Graph Objects, Pandas  
**Document Version:** 2.0.0  

---

## 1. Project Overview & Objective

Refactor and redesign the existing dashboard into an interactive **3-Tab Analytics System** with a **Crimson Soft Light (Burgundy)** aesthetic inspired by modern enterprise UI design. 

The application measures and compares:
1. **Academic Supply:** Graduates, core curriculum skills, tuition fees, and employment timelines.
2. **Labor Market Demand:** Job vacancies, requested skills, top hiring companies, and salary distributions across seniority levels.
3. **Skill Mismatch Analysis:** Algorithmic gap analysis evaluating oversupplied and undersupplied skills.

---

## 2. Core Technical Requirements & Interactivity Rules

1. **Framework:** Python (Dash by Plotly or Streamlit with Session State).
2. **Chart Engine:** Plotly Express and Plotly Graph Objects.
3. **Mandatory Cross-Filtering (Linked Callbacks):**
   * All charts within the same tab **must be cross-linked**.
   * Selecting or filtering a category on any chart (e.g., clicking a degree program or a skill tag) must dynamically update all other charts, KPI cards, and data tables in that tab in real-time.
4. **Tab Data Synchronization:** Filters selected in Tab 1 and Tab 2 must flow seamlessly into Tab 3 to compute the Skill Mismatch index.

---

## 3. Functional Requirements by Tab

```
+-----------------------------------------------------------------------------------+
|                        AI & DATA SCIENCE MARKET DASHBOARD                         |
+-----------------------------------------------------------------------------------+
| [Tab 1: Academic Supply & Skills] | [Tab 2: Job Demand & Salary] | [Tab 3: Skill Mismatch] |
+-----------------------------------------------------------------------------------+
```

### 📌 Tab 1: Academic Supply & Learned Skills (ปริมาณคนที่จบและ Skills ที่เรียนมา)

* **Top KPI Metric Cards:**
  * Total Accumulated Graduates
  * Number of Active Degree Programs
  * Average Total Tuition Fee
  * Average Year-1 Employment Rate (%)
* **Visualizations:**
  1. **Graph 1.1 (Graduate Production Trend):** Stacked Bar / Line Chart showing graduate counts per curriculum per year (AI, Data Science, Statistics).
  2. **Graph 1.2 (Core Required Courses & Skills):** Horizontal Bar Chart / Heatmap displaying mandatory courses aligned with technical domains.
  3. **Graph 1.3 (Graduate Employment Timeline):** Grouped Bar Chart displaying employment rates at **Year 1, Year 2, and Year 3** post-graduation.
  4. **Graph 1.4 (Tuition Fee Comparison):** Box Plot / Bar Chart comparing tuition costs across programs and universities.

---

### 📌 Tab 2: Job Market Demand & Hiring Specs (ปริมาณงานที่จ้างและ Skills ที่ต้องการ)

* **Top KPI Metric Cards:**
  * Total Active Job Vacancies
  * Average Entry-Level Starting Salary
  * #1 In-Demand Technical Skill
* **Visualizations:**
  1. **Graph 2.1 (Job Openings Volume):** Donut / Treemap Chart categorizing job openings by role (Data Scientist, AI/ML Engineer, Statistician, Data Analyst).
  2. **Graph 2.2 (In-Demand Skill Breakdown):** Horizontal Bar Chart displaying frequency of requested skills in job postings (Python, SQL, RAG, MLOps, Power BI, AWS).
  3. **Graph 2.3 (Top Hiring Organizations):** Top-N Bar Chart / Interactive Table highlighting top hiring companies.
  4. **Graph 2.4 (Salary Range by Seniority Level):** Box Plot / Range Bar Chart displaying compensation across:
     * **Entry-Level (เริ่มต้น):** 0–2 years
     * **Mid-Level (ปานกลาง):** 2–5 years
     * **Senior/Lead (เชี่ยวชาญ):** 5+ years

---

### 📌 Tab 3: Skill Mismatch Analysis (การวิเคราะห์ Skill Mismatch)

* **Top Metric Scorecards:**
  * Skill Alignment Index (%)
  * Critical Deficit Skills Count (High Demand / Low Supply)
  * Oversupplied Skills Count (Low Demand / High Supply)
* **Visualizations & Output:**
  1. **Graph 3.1 (Supply vs. Demand Skill Overlay):** Diverging Bar Chart / Radar Chart overlaying curriculum coverage % against job market demand %.
  2. **Graph 3.2 (Skill Gap Matrix - 2x2 Grid):** Scatter Plot Matrix plotting Academic Coverage vs. Industry Demand:
     * *Quadrant 1: Core Essentials* (High Supply / High Demand)
     * *Quadrant 2: Urgent Curriculum Gaps* (Low Supply / High Demand)
     * *Quadrant 3: Niche / Academic Focus* (High Supply / Low Demand)
     * *Quadrant 4: Low Priority* (Low Supply / Low Demand)
  3. **Actionable Recommendations Table:** Automated summary suggesting specific course additions and reskilling paths for curriculum planners.

---

## 4. UI/UX & Styling Requirements (Crimson Soft Light System)

Apply the following design system across the application based on the Crimson/Burgundy dashboard reference:

### 🎨 Color Palette Configuration

```python
COLOR_PALETTE = {
    # Layout Elements
    "sidebar_bg": "#800020",         # Deep Crimson / Burgundy (Navigation & Filters)
    "canvas_bg": "#F8F9FA",          # Soft Cream / Light Off-White (Main Background)
    "card_bg": "#FFFFFF",            # Pure White (Chart Containers & Cards)
    
    # Typography
    "text_primary": "#2B2B2B",       # Dark Charcoal
    "text_secondary": "#6C757D",     # Soft Muted Gray
    "sidebar_text": "#FFFFFF",       # Pure White for Sidebar
    
    # Data Visualization & KPI Accent Tokens
    "primary_crimson": "#801235",    # Main Chart Color / Active Controls
    "accent_rose": "#E63946",       # Highlighting / Alert Elements
    "pastel_yellow": "#FFF3BF",     # KPI Card Accent 1
    "pastel_blue": "#D0EBFF",       # KPI Card Accent 2
    "pastel_pink": "#FFDEEB",       # KPI Card Accent 3
    "neutral_grid": "#E9ECEF"        # Plotly Chart Gridlines
}
```

### 📐 Visual Layout Rules
1. **Left Sidebar Navigation:**
   * Solid `#800020` background with clean white typography.
   * Houses logo/branding, tab selection switches, and global filter dropdowns (e.g., Year, Region, Degree Level).
2. **Main Content Canvas:**
   * Light `#F8F9FA` background.
   * Every chart and metric must be wrapped inside a **White Card Container** (`#FFFFFF`) featuring:
     * Rounded corners: `border-radius: 12px;`
     * Subtle drop shadow: `box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);`
     * Padding: `20px;`
3. **Plotly Chart Styling Constraints:**
   * Transparent paper & plot backgrounds (`paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'`).
   * Clean, modern typography (sans-serif fonts such as *Inter*, *Prompt*, or *Sarabun*).
   * Soft, light-gray grid lines (`#E9ECEF`).

---

## 5. Open Data References & Citations

The dashboard must include direct links or a footer references modal pointing to these open datasets:

1. **MHESI Open Data Thailand:** Thai Higher Education graduate statistics and tuition fees. ([data.mhesi.go.th](https://data.mhesi.go.th/))
2. **U.S. Bureau of Labor Statistics (BLS):** Data Scientists occupational outlook, wages, and job counts. ([bls.gov/ooh](https://www.bls.gov/ooh/math/data-scientists.htm))
3. **Global AI & Data Science Job Salaries Dataset (Kaggle):** Job positions, seniority tiers, and global salaries. ([Kaggle Open Dataset](https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries))
4. **Stack Overflow Developer Survey:** Skill ecosystem, framework usage, and developer demographics. ([Stack Overflow Insights](https://insights.stackoverflow.com/survey))

---

## 6. Execution Directive for Antigravity

> **Prompt for Antigravity:**
> *"Act as a Lead Python Data Visualization Developer. Refactor the existing dashboard using Python (Dash or Streamlit) and Plotly based on `dashboard_refactoring_spec.md`. Implement the 3-Tab structure, configure cross-linked callbacks for interactive filtering within each tab, apply the Crimson Soft Light palette (`#800020` sidebar, white rounded cards on off-white canvas), and calculate the Tab 3 Skill Mismatch metrics."*
