import matplotlib.pyplot as plt
import seaborn as sns

# Visualize the top skills
plt.figure(figsize=(10, 6))
sns.barplot(x=top_skills.values, y=top_skills.index)
plt.title('Top 10 In-Demand Skills')
plt.xlabel('Number of Job Listings')
plt.ylabel('Skills')
plt.show()
