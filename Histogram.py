import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('vk.csv')
plt.hist(df['batsman_runs'],bins=[0,10,20,30,40,50,60,70,80,90,100])
plt.show()