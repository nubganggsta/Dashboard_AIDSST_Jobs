# 📊 AI, Data Science & Statistics Supply-Demand & Skill Mismatch Dashboard

An interactive, responsive analytics dashboard designed to bridge the gap between **Academic Graduate Supply** and **Real-World Labor Market Demand** in the fields of Artificial Intelligence (AI), Data Science, and Statistics.

---

## 📌 Executive Summary & Objective

In the rapidly evolving AI and data analytics era, higher education curricula often struggle to match the fast-changing demands of the industry. This dashboard provides university curriculum designers, industry recruiters, policymakers, and students with actionable, data-driven insights into:

1. **Academic Supply Side:** Annual graduate production, academic curriculum structures, core skill coverage, graduate employment rates (Years 1–3), and tuition costs.
2. **Labor Market Demand Side:** Real-time job vacancies, required technical skill frequencies, hiring enterprise landscapes, and salary distributions across seniority tiers.
3. **Skill Mismatch & Alignment Analysis:** Quantitative mismatch indices, diverging supply vs. demand metrics, a 2×2 curriculum gap matrix, and automated, actionable recommendations for upskilling and curriculum enhancements.
4. **Global & Regional Ecosystem:** Regional benchmark comparisons across Thailand (SEA), the United States, Singapore, and Europe, incorporating open datasets from international labor bureaus and surveys.

---

## 🛠️ Technology Stack & Architecture

- **Core Application Framework:** Python 3.10+ & [Streamlit](https://streamlit.io/)
- **Data Visualization Engine:** [Plotly](https://plotly.com/python/) (Plotly Express & Plotly Graph Objects)
- **Data Manipulation & Analysis:** [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **Styling & Theme:** Modern Tech Dark Mode (`#0f172a` background, `#1e293b` card surfaces, `#38bdf8` cyan & `#34d399` emerald accents)
- **Data Export & Interactivity:** Interactive cross-filtering, linked callbacks/session state synchronization, CSV summary export, and high-resolution chart downloads.

```
+-----------------------------------------------------------------------------------------------------+
|                     AI, DATA SCIENCE & STATISTICS SUPPLY-DEMAND DASHBOARD                           |
+-----------------------------------------------------------------------------------------------------+
| [Tab 1: Academic Supply & Skills] | [Tab 2: Job Demand & Salary] | [Tab 3: Skill Mismatch Analysis] |
| --------------------------------- | ---------------------------- | -------------------------------- |
| • Total Graduates & Tuition KPIs  | • Total Vacancies & Salaries | • Skill Alignment Index (%)      |
| • Curriculum Production Trends    | • Job Roles & Sector Treemap | • Diverging Supply vs. Demand    |
| • Core Courses & Skills Matrix    | • Top In-Demand Skills       | • 2x2 Skill Mismatch Matrix      |
| • Employment Rate Timeline        | • Hiring Ecosystem Directory | • Automated Action Plan Table    |
| • Tuition Fee Comparisons         | • Salary by Experience Level | • Global & Regional Benchmarks   |
+-----------------------------------------------------------------------------------------------------+
```

---

## 📑 Functional Modules & Tab Specifications

### 🎓 Tab 1: Academic Supply & Skills (Academic Supply Side)
- **KPI Summary Cards:**
  - Total Accumulated Graduates across tracked programs
  - Average Program Tuition Fee (THB)
  - Average Year-1 Graduate Employment Rate (%)
- **Graph 1.1: Curriculum Output Trend:** Historical 5-year graduate volume by curriculum (e.g., B.Sc. Data Science, B.Sc. Applied Statistics, M.Sc. Artificial Intelligence, B.Sc. Computer Science AI).
- **Graph 1.2: Core Required Courses & Learned Skills:** Course breakdown, credit weights, and mapped competencies.
- **Graph 1.3: Graduate Employment Timeline:** Longitudinal employment rate tracking across Year 1, Year 2, and Year 3 post-graduation.
- **Graph 1.4: Tuition Fee Structure:** Comparative tuition fees per term and total program cost across academic curricula.

### 💼 Tab 2: Job Demand & Salary (Labor Market Demand Side)
- **KPI Summary Cards:**
  - Total Active Vacancies
  - Average Entry-Level Salary (THB/Month)
  - Top Demanded Skill in Postings
- **Graph 2.1: Job Openings by Role & Sector:** Breakdown of positions (Data Scientist, AI/ML Engineer, Statistician, Data Analyst, Data Engineer) across industries (Fintech, Tech Platforms, Consulting, Retail/Corporate).
- **Graph 2.2: In-Demand Skill Breakdown:** Frequency and prevalence percentage of critical technologies (SQL, Python, PyTorch, RAG, Docker, Power BI, Spark, AWS, etc.).
- **Graph 2.3: Hiring Companies & Volume:** Key hiring organizations (SCBX, KBTG, Agoda, Grab, Central Group, LINE Thailand, etc.) with vacancy counts and required seniority levels.
- **Graph 2.4: Salary Structure by Seniority Level:** Box plot and distribution ranges across Entry-Level (0–2 yrs), Mid-Level (2–5 yrs), and Senior/Lead (5+ yrs).

### ⚖️ Tab 3: Skill Mismatch Analysis (Supply-Demand Gap)
- **Skill Gap Scorecard:**
  - **Skill Alignment Index (%):** Overall alignment score between academic outputs and market needs.
  - **Critical Deficit Skills Count:** High demand in industry, low coverage in universities.
  - **Over-supplied Skills Count:** High academic coverage, low commercial demand.
- **Graph 3.1: Supply vs. Demand Skill Comparison:** Diverging overlay bar chart with visual alerts (Red = Skill Deficit, Green = Balanced, Amber = Over-taught).
- **Graph 3.2: 2×2 Skill Mismatch Matrix:**
  1. *Core Essentials (High Demand / High Supply)* — Maintain and strengthen.
  2. *Urgent Curriculum Gaps (High Demand / Low Supply)* — Critical priority for curriculum revisions.
  3. *Niche / Academic Focus (Low Demand / High Supply)* — Rebalance into elective tracks.
  4. *Low Priority (Low Demand / Low Supply)* — Monitor.
- **Actionable Curriculum Recommendations:** Dynamic table generating clear, prioritized action points for educational institutions.

### 🌐 Global & Regional Market Ecosystem (Handoff Specifications)
- **Macro Market Indicators:** US Open Positions (`245,900`, +34% 10-Yr growth), Thailand STEM Graduates (`65,000`), Thailand Data Science & Statistics Graduates (`4,200`), Global Annual Graduates (`~280,000`).
- **Degree Requirement Distribution:** Bachelor's (58%), Master's (34%), PhD (8%).
- **Multi-Region Salary Benchmarking:** Cross-regional comparisons (USA, Singapore, EU/UK, Thailand).
- **Categorized Skill Taxonomy:** Programming & Databases, Machine Learning & AI, Generative AI & LLMs, Analytics & Visualization, Engineering & MLOps.

---

## 🌐 Open Data Repositories & References

The dashboard integrates and cites official open data benchmarks:
1. **Global Data Science & AI Job Salaries (2020–2026):** [Kaggle Dataset](https://www.kaggle.com/datasets/saurabhshahane/data-science-jobs-salaries)
2. **U.S. Bureau of Labor Statistics (BLS):** [Data Scientists Occupational Outlook](https://www.bls.gov/ooh/math/data-scientists.htm)
3. **Ministry of Higher Education, Science, Research and Innovation (MHESI Thailand):** [MHESI Open Data Portal](https://data.mhesi.go.th/)
4. **Stack Overflow Annual Developer Survey:** [Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey)

---

## 🚀 Getting Started & Local Installation

### Prerequisites
- Python 3.10 or higher
- `pip` package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/nubgangsta/Dashboard_AIDSST_Jobs.git
cd Dashboard_AIDSST_Jobs

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
streamlit run app.py
```
The application will launch automatically at `http://localhost:8501`.

---

## 📁 Project Structure

```
Dashboard_AIDSST_Jobs/
├── .streamlit/
│   └── config.toml             # Streamlit dark theme configuration
├── data/
│   ├── academic_supply.py      # Academic curricula & supply dataset generator
│   ├── job_demand.py           # Job market vacancies & demand dataset generator
│   └── market_overview.py      # Regional benchmarks & global statistics
├── modules/
│   ├── components.py           # Metric cards, headers, styling helpers
│   ├── tab_academic.py         # Tab 1: Academic supply & skills visual modules
│   ├── tab_demand.py           # Tab 2: Job market demand & salary visual modules
│   ├── tab_mismatch.py         # Tab 3: Skill mismatch analytics & matrix
│   └── tab_global.py           # Global & regional ecosystem benchmarks
├── utils/
│   ├── calculations.py         # Skill alignment & mismatch index algorithms
│   └── theme.py                # Plotly dark theme templates and color palettes
├── app.py                      # Main Streamlit dashboard application
├── requirements.txt            # Python dependencies
├── brd_documentation.md        # Original Business Requirement Document
├── handoff_documentation.md    # Original Handoff Specification Document
├── PROJECT_STATUS.md           # Step-by-step progress tracking
└── README.md                   # Project documentation (this file)
```

---

## 📄 License & Attribution

Designed and maintained for education planning, workforce intelligence, and curriculum modernizations in AI, Data Science, and Statistics. Developed with reference to MHESI, BLS, and global industry benchmarks.
