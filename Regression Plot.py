import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: Hours studied vs. Exam Score
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [45, 50, 55, 60, 68, 70, 78, 85, 88, 95]

# Create the regression plot
sns.regplot(x=hours, y=scores, scatter_kws={"s": 50}, line_kws={"color": "red"})

plt.title("Simple Linear Regression: Hours vs. Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()