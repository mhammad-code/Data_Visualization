import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
'''tips=sns.load_dataset('tips')
print(tips)
# scatter plot -> axes level function
sns.scatterplot(data=tips, x='total_bill', y='tip',hue='sex',style='time',size='size')
plt.show()
# relplot -> figure level -> square shape
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter',hue='sex',style='time',size='size')
plt.show()
gap=px.data.gapminder()
pak_data=gap[gap['country'] == 'Pakistan']
print(pak_data)

sns.lineplot(data=pak_data, x='year', y='lifeExp', hue='continent')
plt.show()




temp_df=gap[gap['country'].isin (['Pakistan','India','China'])]
sns.relplot(kind='line', data=temp_df, x='year', y='lifeExp', hue='country', style='continent', size='continent')
plt.show()


gap=px.data.gapminder()
temp_df=gap[gap['country'].isin (['Pakistan','Brazil','Poland'])]
sns.relplot(kind='line', data=temp_df, x='year', y='lifeExp', hue='country', style='continent', size='continent')
plt.show()


tips=sns.load_dataset('tips')
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter',col='smoker',row='sex',size='size')
plt.show()
# facet plot -> figure level function -> work with relplot
# it will not work with scatterplot and lineplot
sns.relplot(data=tips, x='total_bill', y='tip', kind='line', col='sex', row='day')'''

gap=px.data.gapminder()
sns.relplot(data=gap, x='lifeExp', y='gdpPercap', kind='scatter', col='year', col_wrap=3)
plt.show()