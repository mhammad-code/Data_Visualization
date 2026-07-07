import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
children=[10,20,40,10,30]
colrs=['red','orange','yellow','green','blue']
plt.barh(colrs,children,color='Blue')
plt.show()
df = pd.read_csv('batsman_season_record.csv')

# 2. Set 'batsman' as the index so it automatically becomes the X-axis labels
# Then select the columns/years you want to compare (e.g., '2015' and '2016')
df.set_index('batsman')[['2015', '2016','2017']].plot(kind='bar', width=0.6, color=['blue', 'orange','red'])
plt.show()

# 3. Add titles and labels
plt.title('Season Comparison of Batsmen')
plt.xlabel('Batsman')
plt.ylabel('Runs')

# Rotate names so they don't overlap if they are long
plt.xticks(rotation=45)
plt.tight_layout() # Ensures everything fits nicely in the window

# 4. Display the plot
plt.show()