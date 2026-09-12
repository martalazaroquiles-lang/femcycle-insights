# 🩸 FemCycle Insights

A data analytics portfolio project analyzing menstrual cycle patterns, symptoms, and lifestyle factors — built to demonstrate SQL, Python, and statistical analysis skills relevant to FemTech and digital health products.

**[Live Dashboard](#)** | **[Notebooks](notebooks/)** | **[SQL Queries](sql/)**

## Business Problem

FemTech products (like Flo, Clue) often assume that lifestyle factors — stress, sleep, diet, exercise — predict which symptoms a user will experience during their cycle, and personalize content accordingly. This project tests that assumption directly using real data, rather than taking it for granted.

## Dataset

895 menstrual cycles from 100 users, sourced from [Kaggle: Menstrual Cycle Data with Factors](https://www.kaggle.com/datasets/akshayas02/menstrual-cycle-data-with-factors-dataset). Includes age, BMI, stress level, sleep hours, diet, exercise frequency, cycle/period length, and predominant symptom per cycle.

## Methodology

1. **Data exploration & cleaning (SQL + Python):** identified that the traditional clinical cycle-length range (21-35 days) excluded 56% of this population — adjusted to a percentile-based (P5-P95) outlier detection approach instead.
2. **Cycle phase calculation (SQL):** computed proportional date ranges for menstrual, follicular, ovulation, and luteal phases per cycle, based on each user's actual cycle length rather than a fixed 28-day assumption.
3. **Statistical testing (Python):** ran ANOVA and Chi-square tests to check whether stress, sleep, age, BMI, diet, or exercise individually predict predominant symptom.
4. **Clustering (K-means):** grouped users by combined lifestyle profiles (two approaches: mixed variables and numeric-only) to test whether *combinations* of factors, rather than single variables, revealed a pattern.
5. **Dashboard (Streamlit + Plotly):** built an interactive dashboard summarizing findings for a non-technical audience.

## Key Findings

- No individual lifestyle factor showed a statistically significant relationship with predominant symptom (all p > 0.05, ANOVA/Chi-square)
- K-means clustering (both mixed and numeric-only approaches) also showed no significant relationship (p = 0.159 and p = 0.614)
- This suggests symptom presentation is more likely driven by day-level hormonal dynamics — not captured in this dataset — rather than by demographic or lifestyle factors

## Product Implication

Personalization strategies for FemTech products should prioritize **cycle-phase tracking** over **lifestyle-based segmentation** when it comes to symptom-related features — this dataset does not support the common assumption that stress/sleep/diet alone predict symptoms.

## Tech Stack

- **SQL** (SQLite) — data cleaning, outlier detection, phase calculation
- **Python** — pandas, scikit-learn (K-means), scipy (statistical testing)
- **Streamlit + Plotly** — interactive dashboard
- **Git/GitHub** — version control

## Project Structure
femcycle-insights/
├── data/ # Raw dataset (CSV)
├── notebooks/ # Exploration, cleaning, and analysis (Jupyter)
├── sql/ # Documented SQL queries
├── dashboard/ # Streamlit dashboard app
├── femcycle.db # SQLite database
└── requirements.txt # Python dependencies

## How to Run

```bash
python -m venv venv
.\venv\Scripts\Activate  # Windows
pip install -r requirements.txt
cd dashboard
streamlit run app.py
```

## Author

Marta Lázaro Quiles — [LinkedIn](https://www.linkedin.com/in/marta-l%C3%A1zaro-828b13392/) | [GitHub](https://github.com/martalazaroquiles-lang)