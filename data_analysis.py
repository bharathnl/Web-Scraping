import pandas as pd

# Load the scraped data
df = pd.read_csv('job_listings.csv')

# Data cleaning
df.drop_duplicates(inplace=True)
df.dropna(subset=['title', 'company'], inplace=True)

# Analysis
top_skills = df['skills'].value_counts().head(10)
average_salary = df['salary'].mean()

print(f"Top Skills:\n{top_skills}")
print(f"Average Salary: ${average_salary:.2f}")
