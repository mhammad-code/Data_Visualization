import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('batter.csv')
fig=plt.figure()
x=[0,1,2,45]
y=[4,8,9,34]
z=[5,6,7,12]
ax=plt.subplot(projection='3d')
ax.scatter3D(x,y,z,s=[100,100,100,100])
ax.plot3D(x,y,z,color='red')
plt.show()