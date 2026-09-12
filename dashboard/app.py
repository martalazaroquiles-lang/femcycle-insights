import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Page configuration
st.set_page_config(page_title="FemCycle Insights", layout="wide")

# Custom color theme for FemTech branding
px.defaults.color_discrete_sequence = ['#E63971', '#9C6ADE', '#4C6FFF', '#FF9F7D', '#5EC8C7']

# Load data
conn = sqlite3.connect('../femcycle.db')
df = pd.read_sql("SELECT * FROM ciclos", conn)
conn.close()

# Title
st.title("🩸 FemCycle Insights")
st.markdown("**A data-driven look at menstrual cycle patterns, symptoms, and lifestyle factors**")

st.markdown("---")
st.subheader("📋 Executive Summary")
st.markdown(f"""
This project analyzes **{df.shape[0]} menstrual cycles from {df['User ID'].nunique()} users** 
to test whether lifestyle factors (stress, sleep, diet, exercise, age, BMI) predict symptom 
occurrence — a common assumption in FemTech product design.

**Key takeaways:**
- 🔍 The traditional 21-35 day "clinical standard" cycle range excluded 56% of this population — 
  a percentile-based approach was used instead to correctly identify true outliers (7.4%)
- 📊 No individual lifestyle factor showed a statistically significant relationship with 
  predominant symptom (all p > 0.05)
- 🧩 Even combining factors via clustering (K-means) did not reveal a significant pattern, 
  suggesting symptoms are more likely driven by hormonal cycle-phase dynamics than 
  lifestyle alone

**Product implication:** personalization strategies should prioritize cycle-phase tracking 
over lifestyle-based segmentation for symptom-related features.
""")
st.markdown("---")

# Show basic info
st.write(f"Dataset: {df.shape[0]} cycles from {df['User ID'].nunique()} users")

# Section 1: Population overview
st.header("📊 Population Overview")

col1, col2, col3 = st.columns(3)

with col1:
    fig_age = px.histogram(df.drop_duplicates('User ID'), x='Age', 
                             title='Age Distribution', nbins=15)
    st.plotly_chart(fig_age, use_container_width=True)

with col2:
    fig_diet = px.pie(df.drop_duplicates('User ID'), names='Diet', 
                        title='Diet Type Distribution')
    st.plotly_chart(fig_diet, use_container_width=True)

with col3:
    fig_exercise = px.pie(df.drop_duplicates('User ID'), names='Exercise Frequency', 
                            title='Exercise Frequency Distribution')
    st.plotly_chart(fig_exercise, use_container_width=True)

# Section 2: Cycle Length Analysis
st.header("📈 Cycle Length: Challenging the Clinical Standard")

col1, col2 = st.columns([2, 1])

with col1:
    fig_cycle = px.histogram(df, x='Cycle Length', nbins=30,
                               title='Cycle Length Distribution (all 895 cycles)')
    fig_cycle.add_vline(x=21, line_dash="dash", line_color="red", 
                         annotation_text="Clinical min (21)")
    fig_cycle.add_vline(x=35, line_dash="dash", line_color="red", 
                         annotation_text="Clinical max (35)")
    st.plotly_chart(fig_cycle, use_container_width=True)

with col2:
    st.metric("Mean Cycle Length", f"{df['Cycle Length'].mean():.1f} days")
    st.metric("Cycles outside clinical range (21-35)", 
              f"{(df['Cycle Length'] < 21).sum() + (df['Cycle Length'] > 35).sum()} ({((df['Cycle Length'] < 21).sum() + (df['Cycle Length'] > 35).sum())/len(df)*100:.0f}%)")
    st.info("**Insight:** 56% of cycles fall outside the traditional 21-35 day range. We used a percentile-based approach (P5-P95) instead, identifying 66 true outliers (7.4%).")

# Section 3: Symptoms Overview
st.header("🔍 Symptom Patterns")

col1, col2 = st.columns(2)

with col1:
    fig_symptoms = px.bar(df['Symptoms'].value_counts().reset_index(), 
                            x='Symptoms', y='count',
                            title='Predominant Symptom per Cycle (895 total)',
                            labels={'count': 'Number of Cycles'})
    st.plotly_chart(fig_symptoms, use_container_width=True)

with col2:
    unique_users = df.groupby('Symptoms')['User ID'].nunique().reset_index()
    unique_users.columns = ['Symptoms', 'Unique Users']
    fig_unique = px.bar(unique_users, x='Symptoms', y='Unique Users',
                          title='Users Reporting Each Symptom (out of 100)')
    st.plotly_chart(fig_unique, use_container_width=True)

st.warning("""
**Key Finding:** No statistically significant relationship was found between 
predominant symptom and stress level, sleep, age, BMI, diet, or exercise 
frequency — tested individually (ANOVA/Chi-square, all p > 0.05) and in 
combination via K-means clustering (p = 0.159 and p = 0.614 across two 
approaches). This suggests symptom presentation is more likely driven by 
hormonal cycle-phase dynamics not captured at this dataset's granularity, 
rather than lifestyle factors.
""")