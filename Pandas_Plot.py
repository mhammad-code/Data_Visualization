import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s=pd.Series([1,2,3,4,5])
s.plot(kind='line')
plt.show()


s=pd.Series([7,5,33,67,1])
s.plot(kind='bar')
plt.show()
s=pd.Series([7,5,33,67,1])
s.plot(kind='pie')
plt.show()