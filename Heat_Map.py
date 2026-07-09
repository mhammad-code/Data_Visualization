import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

gap = px.data.gapminder()
temp_df = gap.pivot(index='country', columns='year', values='lifeExp')

# Make the figure explicitly tall (e.g., 30 inches tall) to accommodate 142 rows
plt.figure(figsize=(15, 10))

# Set annot=False because 142 rows of numbers cannot fit cleanly
sns.heatmap(temp_df, annot=False, cmap='YlGnBu')

plt.title('Global Life Expectancy Heatmap', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

temp_df = gap[gap['continent'] == 'Europe'].pivot(index='country',columns='year',values='lifeExp')

plt.figure(figsize=(15,15))
sns.heatmap(temp_df,annot=True,linewidth=0.5, cmap='summer')
plt.show()