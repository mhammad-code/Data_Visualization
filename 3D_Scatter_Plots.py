import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('batter.csv')
fig=plt.figure()
ax=plt.subplot(projection='3d')
ax.scatter(df['avg'], df['runs'], df['strike_rate'])
ax.set_title('Batting Analysis')
ax.set_xlabel('runs')
ax.set_zlabel('strike_rate')
ax.set_ylabel('avg')
plt.show()