import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=[10,20,30,40,50]
subject=['eng','math','physics','computer','chemistry']
plt.pie(data,labels=subject,autopct='%1.1f%%',explode=[0.1,0,0,0,0.1])
plt.style.use('dark_background')
plt.show()
