import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample Data
data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam_Score': [45, 51, 52, 60, 68, 70, 80, 81, 89, 95]
}
df = pd.DataFrame(data)

# Set a beautiful default theme
sns.set_theme(style="darkgrid")

# Create a regression plot (scatter + OLS regression line + confidence interval)
sns.lmplot(data=df, x="Study_Hours", y="Exam_Score", height=5, aspect=1.5)

# Add title (We still use Matplotlib's plt behind the scenes to customize!)
plt.title("Seaborn: OLS Regression with 95% Confidence Interval")

plt.show()