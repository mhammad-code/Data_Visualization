import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IPL_Ball_by_Ball_2008_2022 (1).csv')

temp_df = df[df['ballnumber'].isin([1, 2, 3, 4, 5, 6]) & (df['batsman_run'] == 6)]
grid = temp_df.pivot_table(index='overs', columns='ballnumber', values='batsman_run', aggfunc='count')

# Plot the matrix
plt.imshow(grid, cmap=plt.cm.Blues, aspect='auto')
plt.colorbar()

# FIX: Set the tick positions and replace them with actual ball/over labels
plt.xticks(ticks=np.arange(len(grid.columns)), labels=grid.columns)
plt.yticks(ticks=np.arange(len(grid.index)), labels=grid.index)

# Add titles and labels
plt.title('Count of Sixes per Ball/Over')
plt.xlabel('Ball Number')
plt.ylabel('Over Number')

plt.show()