import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''fig,ax=plt.subplots(nrows=2,ncols=1,sharex=True)
df = pd.read_csv('batter.csv')
ax[0].scatter(df['avg'],df['strike_rate'],color='red')
ax[0].set_title('Avg Vs Strike_Rate')
ax[0].set_ylabel('Strike Rate')

ax[1].scatter(df['avg'],df['runs'],color='blue')
ax[1].set_title('Avg Vs Runs')
ax[1].set_ylabel('Runs')
ax[1].set_xlabel('Average')
plt.show()'''


fig,ax=plt.subplots(nrows=2,ncols=2,figsize=(10,10))
df = pd.read_csv('batter.csv')
ax[0,0].scatter(df['avg'],df['strike_rate'],color='red')
ax[0,1].scatter(df['avg'],df['strike_rate'])
ax[1,0].hist(df['avg'])
ax[1,1].hist(df['strike_rate'])

plt.show()