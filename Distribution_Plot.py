import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
tips=sns.load_dataset('tips')
'''sns.histplot(data=tips, x='total_bill')
plt.show()

sns.histplot(data=tips, x='day')
plt.show()
sns.histplot(data=tips, x='tip',hue='sex')
plt.show()
titanic = pd.read_csv('titanic.csv')
sns.displot(data=titanic, x='age', kind='hist',element='step',hue='sex')
plt.show()
sns.displot(data=tips, x='tip', kind='hist',col='sex',element='step')

sns.kdeplot(data=tips, x='tip',hue='sex')
plt.show()'''
sns.kdeplot(data=tips,x='total_bill')
sns.rugplot(data=tips,x='total_bill')
plt.show()