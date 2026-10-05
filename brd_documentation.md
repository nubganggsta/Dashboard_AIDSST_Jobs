# 📄 Business Requirement Document (BRD)
## Project: AI, Data Science & Statistics Supply-Demand & Skill Mismatch Dashboard

**Target Developer Agent:** Antigravity  
**Document Version:** 1.0.0  
**Technology Stack:** Python (Dash / Streamlit), Plotly (Plotly Express / Graph Objects), Pandas  
**Primary Goal:** Build an interactive 3-Tab analytics dashboard measuring academic graduate supply, industry job market demand, and skill mismatch analysis.

---

## 1. Executive Summary & Objective

 dashboard นี้มีจุดประสงค์เพื่อวิเคราะห์ความสอดคล้องระหว่าง **การผลิตกำลังคนทางวิชาการ (Supply Side)** และ **ความต้องการของตลาดแรงงานจริง (Demand Side)** ในสายงาน AI, Data Science และ Statistics 

ระบบจะช่วยให้นักวางแผนหลักสูตร, ผู้ประกอบการ และนักศึกษาสามารถมองเห็นภาพรวมของ:
1. ปริมาณผู้สำเร็จการศึกษา หลักสูตร และทักษะที่ถ่ายทอดในรั้วมหาวิทยาลัย
2. ปริมาณตำแหน่งงานว่าง ทักษะที่ตลาดต้องการจริง และผลตอบแทน (เงินเดือน)
3. ช่องว่างทางทักษะ (Skill Mismatch Index) เพื่อนำไปสู่การปรับปรุงหลักสูตรและการพัฒนาทักษะ (Reskill/Upskill)

---

## 2. Technical Stack & Architectural Constraints

1. **Backend Framework:** Python 3.10+ (ใช้ **Dash by Plotly** หรือ **Streamlit** พร้อม Session State)
2. **Visualization Engine:** **Plotly Express / Plotly Graph Objects**
3. **Data Handling:** Pandas / Polars
4. **Interactivity Standard (Mandatory):**
   * **Cross-Filtering / Linked Callbacks:** ทุกกราฟใน Tab เดียวกันต้องเชื่อมโยงกัน (Cross-linked) เมื่อผู้ใช้คลิกเลือก Filter บนกราฟใด กราฟอื่นใน Tab นั้นจะต้องอัปเดตข้อมูลตาม Selection ทันที
   * **Tab Synchronization:** ตัวแปรสเกล (เช่น เลือกเฉพาะสาขา Data Science หรือเลือกช่วงระดับประสบการณ์) ต้องถูกส่งต่อเข้าสู่ Tab 3 สำหรับประมวลผล Mismatch

---

## 3. Functional Requirements by Module (Tab Specification)

```
+-----------------------------------------------------------------------------------+
|                            AI & DATA SCIENCE DASHBOARD                            |
+-----------------------------------------------------------------------------------+
| [Tab 1: Academic Supply & Skills] | [Tab 2: Job Demand & Salary] | [Tab 3: Mismatch Analysis] |
+-----------------------------------------------------------------------------------+
```

---

### 3.1 TAB 1: ปริมาณคนที่จบและ Skills ที่เรียนมา (Academic Supply Side)

**Core Objective:** วิเคราะห์ศักยภาพการผลิตบัณฑิต โครงสร้างหลักสูตร อัตราการได้งานทำ และค่าใช้จ่ายในการศึกษา

#### **Components & Visualizations:**
1. **KPI Metric Summary Cards (Top Row):**
   * ปริมาณบัณฑิตสะสมรวมทุกปี (Total Graduates)
   * ค่าเทอมเฉลี่ยตลอดหลักสูตร (Avg Tuition Fee)
   * อัตราการได้งานทำเฉลี่ยปีที่ 1 (Avg Year-1 Employment Rate %)

2. **Graph 1.1: ปริมาณผู้สำเร็จการศึกษาแยกตามหลักสูตรและรายปี (Curriculum Output)**
   * **Type:** Stacked Bar Chart / Interactive Line Chart
   * **Data:** จำนวนบัณฑิตย้อนหลัง 5 ปี แยกตามชื่อหลักสูตร (เช่น สถิติประยุกต์, วิทยาการข้อมูล, ปัญญาประดิษฐ์)
   * **Interactivity:** คลิกที่แท่งหลักสูตรเพื่อกรองข้อมูลใน Graph 1.2, 1.3 และ 1.4

3. **Graph 1.2: รายวิชาบังคับและ Skill Matrix ของแต่ละหลักสูตร (Core Required Courses & Learned Skills)**
   * **Type:** Horizontal Bar Chart / Heatmap Matrix
   * **Data:** แสดงรายวิชาบังคับที่ตรงกับสายงาน (เช่น Python for Data Sci, Mathematical Statistics, Machine Learning, Applied Regression, SQL) และน้ำหนักหน่วยกิต

4. **Graph 1.3: ติดตามการได้งานทำของบัณฑิต (Graduate Employment Timeline)**
   * **Type:** Grouped Bar / Multi-line Trend Chart
   * **Data:** ร้อยละหรือจำนวนบัณฑิตที่ได้ทำงานใน **ปีที่ 1, ปีที่ 2 และ ปีที่ 3** หลังสำเร็จการศึกษา

5. **Graph 1.4: เปรียบเทียบค่าธรรมเนียมการศึกษา (Tuition Fee Structure)**
   * **Type:** Box Plot หรือ Bar Chart
   * **Data:** ค่าเทอมต่อเทอม / ค่าใช้จ่ายรวมตลอดหลักสูตร เปรียบเทียบระหว่างหลักสูตรและสถาบัน

---

### 3.2 TAB 2: ปริมาณงานที่จ้าง และ Skills ที่ต้องการ (Labor Market Demand Side)

**Core Objective:** สำรวจความต้องการในตลาดแรงงานจริง สกิลที่ถูกระบุในใบสมัครงาน บริษัทที่เปิดรับ และโครงสร้างเงินเดือน

#### **Components & Visualizations:**
1. **KPI Metric Summary Cards (Top Row):**
   * ปริมาณตำแหน่งงานว่างทั้งหมด (Total Vacancies)
   * เงินเดือนเริ่มต้นเฉลี่ย (Avg Entry-Level Salary)
   * ทักษะอันดับ 1 ที่ถูกระบุในประกาศรับสมัครงาน (Top Demanded Skill)

2. **Graph 2.1: ปริมาณตำแหน่งงานว่างตามประเภทสายงานและอุตสาหกรรม (Job Openings Volume)**
   * **Type:** Donut Chart / Treemap Chart
   * **Data:** จำนวนประกาศรับสมัครงานแยกตามประเภทตำแหน่ง (Data Scientist, AI Engineer, Statistician, Data Engineer) และกลุ่มอุตสาหกรรม
   * **Interactivity:** คลิกที่กลุ่มตำแหน่งเพื่อ Filter ข้อมูลสกิล เงินเดือน และบริษัทในกราฟอื่น

3. **Graph 2.2: ทักษะที่ตลาดต้องการสูงสุด (In-Demand Skill Breakdown)**
   * **Type:** Horizontal Bar Chart (Sorted Frequency)
   * **Data:** สัดส่วนเปอร์เซ็นต์ที่ประกาศรับสมัครงานระบุสกิลนั้นๆ (เช่น SQL, Python, PyTorch, RAG, Power BI, Cloud Platforms)

4. **Graph 2.3: บริษัทและองค์กรที่เปิดรับสมัครงาน (Hiring Companies & Volume)**
   * **Type:** Top-N Bar Chart / Interactive Data Table
   * **Data:** รายชื่อบริษัท/องค์กร พร้อมจำนวนตำแหน่งที่เปิดรับ และระดับ Seniority ที่ต้องการ

5. **Graph 2.4: โครงสร้างเงินเดือนตามระดับประสบการณ์ (Salary Range by Seniority Level)**
   * **Type:** Box Plot / Range Bar Chart / Violin Plot
   * **Data:** กระจายตัวของเงินเดือน (Base Salary) จำแนกตามระดับงาน:
     * **เริ่มต้น (Entry-Level / Junior):** 0-2 ปี
     * **ปานกลาง (Mid-Level):** 2-5 ปี
     * **เชี่ยวชาญ / นำทีม (Senior / Lead):** 5+ ปีขึ้นไป

---

### 3.3 TAB 3: การวิเคราะห์ความไม่สอดคล้องทางทักษะ (Skill Mismatch Analysis)

**Core Objective:** สังเคราะห์ข้อมูลจาก Tab 1 (สิ่งที่เรียน) และ Tab 2 (สิ่งที่ตลาดต้องการ) เพื่อหา Skill Gap และเสนอข้อเสนอแนะ

#### **Components & Visualizations:**
1. **Skill Gap Scorecard (Key Metrics):**
   * **Skill Alignment Index (%):** ดัชนีความสอดคล้องของหลักสูตรกับตลาด
   * **Critical Deficit Skills Count:** จำนวนทักษะขาดแคลนวิกฤต (ตลาดต้องการสูง แต่หลักสูตรสอนน้อย)
   * **Over-supplied Skills Count:** ทักษะที่สอนเยอะ แต่ตลาดต้องการน้อย

2. **Graph 3.1: Supply vs. Demand Skill Comparison (Diverging Bar / Radar Chart)**
   * **Type:** Overlay Bar Chart หรือ Radar Chart
   * **Data Axis:**
     * **Supply Bar (%):** สัดส่วนหลักสูตรที่เปิดสอนทักษะนี้ (จาก Tab 1)
     * **Demand Bar (%):** สัดส่วนประกาศงานที่ต้องการทักษะนี้ (จาก Tab 2)
   * **Visual Coding:**
     * **Red Highlight:** High Demand / Low Supply (Skill Deficit - ขาดแคลน)
     * **Green Highlight:** Balanced Supply / Demand (สอดคล้อง)
     * **Yellow Highlight:** High Supply / Low Demand (Over-taught)

3. **Graph 3.2: Skill Mismatch Matrix (2x2 Matrix Grid)**
   * **Type:** Scatter Plot Matrix (X-axis = Academic Coverage %, Y-axis = Job Market Demand %)
   * **4 Quadrants:**
     1. *Core Essentials (High Demand / High Supply)* -> รักษาไว้
     2. *Urgent Curriculum Gaps (High Demand / Low Supply)* -> **ต้องรีบเพิ่มในหลักสูตร**
     3. *Niche / Academic Focus (Low Demand / High Supply)* -> ปรับลดหรือเปลี่ยนเป็นวิชาเลือก
     4. *Low Priority (Low Demand / Low Supply)*

4. **Actionable Recommendations Table:**
   * ตารางสรุปคำแนะนำอัตโนมัติสำหรับสถาบันการศึกษา (เช่น "ควรเพิ่มรายวิชา MLOps & Vector Databases ในหลักสูตร Data Science เนื่องจากตลาดต้องการสูงถึง 42% แต่มีสอนในหลักสูตรเพียง 10%")

---

## 4. Data Schema & Mock Dataset Guide (For Immediate Prototyping)

Antigravity สามารถสร้าง Mock Data Frame ตาม Schema ด้านล่างนี้เพื่อใช้ในการ พัฒนา Dashboard ได้ทันที:

```python
import pandas as pd
import numpy as np

# Mock Tab 1: Academic Supply
academic_df = pd.DataFrame({
    "curriculum_id": ["CURR01", "CURR02", "CURR03", "CURR04"],
    "curriculum_name": ["B.Sc. Data Science", "B.Sc. Applied Statistics", "M.Sc. Artificial Intelligence", "B.Sc. Computer Science (AI)"],
    "annual_graduates_2023": [120, 85, 45, 150],
    "annual_graduates_2024": [140, 80, 50, 165],
    "annual_graduates_2025": [160, 90, 60, 180],
    "tuition_fee_total_thb": [240000, 160000, 320000, 220000],
    "emp_rate_year_1": [0.88, 0.82, 0.95, 0.90],
    "emp_rate_year_2": [0.94, 0.89, 0.98, 0.95],
    "emp_rate_year_3": [0.96, 0.92, 0.99, 0.97],
    "core_skills_taught": [
        ["Python", "SQL", "Tableau", "Machine Learning", "A/B Testing"],
        ["R", "SAS", "Probability", "Regression Analysis", "SQL"],
        ["Python", "PyTorch", "Deep Learning", "NLP", "C++", "RAG"],
        ["Python", "Java", "Data Structures", "SQL", "Scikit-Learn"]
    ]
})

# Mock Tab 2: Job Market Demand
job_demand_df = pd.DataFrame({
    "job_id": [f"JOB_{i:03d}" for i in range(1, 101)],
    "job_title": np.random.choice(["Data Scientist", "AI/ML Engineer", "Statistician", "Data Analyst"], 100),
    "company_name": np.random.choice(["SCBX", "KBTG", "Agoda", "Grab", "Central Group", "True Corp", "LINE Thailand"], 100),
    "seniority_level": np.random.choice(["Entry-Level", "Mid-Level", "Senior/Expert"], 100, p=[0.4, 0.4, 0.2]),
    "salary_min_thb": [28000 if s=="Entry-Level" else 55000 if s=="Mid-Level" else 110000 for s in np.random.choice(["Entry-Level", "Mid-Level", "Senior/Expert"], 100)],
    "salary_max_thb": [45000 if s=="Entry-Level" else 95000 if s=="Mid-Level" else 200000 for s in np.random.choice(["Entry-Level", "Mid-Level", "Senior/Expert"], 100)],
    "required_skills": [
        np.random.choice(["Python", "SQL", "PyTorch", "RAG", "Docker", "Power BI", "A/B Testing", "Spark", "AWS"], size=np.random.randint(3, 6), replace=False).tolist()
        for _ in range(100)
    ]
})
```

---

## 5. Non-Functional & UI/UX Requirements

1. **Theme:** Modern Tech Dark Mode (Background: `#0f172a`, Card BG: `#1e293b`, Text: `#f8fafc`, Accent: `#38bdf8` / `#34d399`).
2. **Layout Responsiveness:** Responsive Grid (CSS Flexbox/Grid or Dash Bootstrap Components `dbc.Container`).
3. **Chart Tooltips:** ต้องแสดงข้อมูลแบบละเอียดเมื่อ Hover (เช่น ชื่อวิชา, สถาบัน, เงินเดือนช่วง Min-Max, จำนวนคน).
4. **Export Capabilities:** มีปุ่ม Export Data/Charts เป็นภาพ PNG หรือไฟล์ CSV สรุปผล.

---

## 6. Execution Directive for Antigravity

> **Instruction for Antigravity:**  
> *"Please act as a Lead Python Data Visualization Engineer. Implement the Dashboard defined in this BRD (`brd_dashboard_antigravity.md`) using Python (Plotly + Dash or Streamlit). Ensure all 3 tabs are built with linked callbacks for interactive cross-filtering, dark-mode visual aesthetics, and precise mathematical alignment for the Tab 3 Skill Mismatch calculations."*
```

---

เอกสาร BRD ฉบับนี้พร้อมส่งต่อให้ **Antigravity** นำไปสร้างโปรเจกต์และเขียนโค้ด Dashboard ได้ทันทีครับ หากคุณต้องการปรับเปลี่ยน หรือเพิ่ม Metric ใดๆ ใน BRD สามารถแจ้งเพิ่มเติมได้เลยนะครับ!