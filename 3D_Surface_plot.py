import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
xx,yy=np.meshgrid(x,y)
z=xx**2+yy**2
fig = plt.figure(figsize=(8,8))
ax=plt.subplot(111, projection='3d')
ax.plot_surface(xx,yy,z,cmap=plt.cm.jet)
plt.show()'''

x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
xx,yy=np.meshgrid(x,y)
z=np.tan(xx)+np.cos(yy)
fig = plt.figure(figsize=(8,8))
ax=plt.subplot(111, projection='3d')
ax.plot_surface(xx,yy,z,cmap=plt.cm.jet)
plt.show()

