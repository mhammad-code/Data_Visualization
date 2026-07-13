import seaborn as sns
import matplotlib.pyplot as plt

# Using the built-in 'tips' dataset
tips = sns.load_dataset("tips")

# Joint plot showing the relationship between total bill and tip
sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg", color="teal")

plt.show()