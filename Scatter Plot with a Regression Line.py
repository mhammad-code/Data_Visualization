import plotly.express as px
import pandas as pd

# Sample data: Study Hours vs. Exam Scores
data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam_Score': [45, 51, 52, 60, 68, 70, 80, 81, 89, 95]
}
df = pd.DataFrame(data)

# Create scatter plot with an OLS regression line
fig = px.scatter(
    df,
    x="Study_Hours",
    y="Exam_Score",
    trendline="ols",  # Automatically fits a regression line
    title="Simple Linear Regression: Study Hours vs. Exam Score",
    labels={"Study_Hours": "Hours Studied", "Exam_Score": "Exam Score (%)"}
)

fig.show()