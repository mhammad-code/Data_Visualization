import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
tips=sns.load_dataset('tips')
sns.displot(data=tips, x='total_bill', y='tip',kind='hist')
plt.show()


sns.kdeplot(data=tips, x='total_bill', y='tip')
plt.show()

