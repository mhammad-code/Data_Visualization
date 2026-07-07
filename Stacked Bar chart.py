import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('batsman_season_record.csv')

# 2. Set 'batsman' as the index so it's on the X-axis
# Select the columns you want to stack (e.g., '2015' and '2016')
df.set_index('batsman')[['2015', '2016']].plot(kind='bar', stacked=True, color=['blue', 'orange'])

# 3. Add labels and formatting
plt.title('Total Runs Scored (Stacked by Season)')
plt.xlabel('Batsman')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.tight_layout()

# 4. Display
plt.show()