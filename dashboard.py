import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('job_listings.csv')

# Create interactive visualizations
st.title('Job Market Trends Dashboard')

top_skills = df['skills'].value_counts().head(10)
fig = px.bar(top_skills, x=top_skills.values, y=top_skills.index, orientation='h', title='Top 10 In-Demand Skills')
st.plotly_chart(fig)
