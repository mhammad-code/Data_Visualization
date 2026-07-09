import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips=sns.load_dataset('tips')
iris = px.data.iris()
sns.boxplot(data=tips,x='day',y='total_bill')
plt.show()
sns.boxplot(data=tips,x='day',y='total_bill',hue='sex')
plt.show()

sns.violinplot(data=tips,x='day',y='total_bill')
plt.show()


sns.catplot(data=tips,x='day',y='total_bill',kind='violin',hue='sex',split=True)
plt.show()

sns.countplot(data=tips,x='sex',hue='day')
plt.show()

# axes level
# hue parameter is not available
sns.regplot(data=tips,x='total_bill',y='tip')
plt.show()
sns.lmplot(data=tips,x='total_bill',y='tip',hue='sex')
plt.show()

sns.pairplot(iris,hue='species')
plt.show()

g = sns.JointGrid(data=tips,x='total_bill',y='tip')
g.plot(sns.kdeplot,sns.violinplot)
plt.show()