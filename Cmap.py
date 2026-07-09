import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

iris = px.data.iris()
print(iris)
sns.clustermap(iris.iloc[:,[0,1,2,3]])
plt.show()