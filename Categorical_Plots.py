import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

tips=sns.load_dataset('tips')
iris = px.data.iris()
sns.stripplot(data=tips,x='day',y='total_bill')
plt.show()
# using catplot
# figure level function
sns.catplot(data=tips, x='day',y='total_bill',kind='strip',hue='sex')
plt.show()



sns.catplot(data=tips, x='day',y='total_bill',kind='swarm',hue='sex')
plt.show()

