import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
price = [33000, 27000, 32000, 35000, 41000]
year = [2018, 2019, 2021, 2023, 2026]

# 1. Choose a cleaner layout style from Seaborn
sns.set_theme(style="darkgrid")

# 2. Plot the line with a marker on each data point
plt.plot(year, price, marker='o', color='b', linewidth=2)

# 3. Add labels and a title
plt.xlabel("Year")
plt.ylabel("Price (in USD)")
plt.title("Price Trends Over Time")

# 4. Show the updated chart
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
batsman = pd.read_csv("sharma-kohli.csv")

# 2. Set a clean, modern aesthetic style using Seaborn
sns.set_theme(style="darkgrid")

# 3. Plot Virat Kohli (Using RCB Red, solid line, diamond markers)
plt.plot(batsman['index'], batsman['V Kohli'],
         color='#ff6119', linestyle='-', linewidth=2.5,
         marker='D', markersize=7, label='Virat Kohli')

# 4. Plot Rohit Sharma (Using MI Blue, dashed line, circle markers)
plt.plot(batsman['index'], batsman['RG Sharma'],
         color='#242324', linestyle='--', linewidth=2.5,
         marker='o', markersize=7, label='Rohit Sharma')

# 5. Add clear, descriptive typography
plt.title("Rohit Sharma vs. Virat Kohli: Career IPL Runs Comparison",
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel("IPL Season (Year)", fontsize=11, fontweight='semibold')
plt.ylabel("Total Runs Scored", fontsize=11, fontweight='semibold')

# 6. Ensure every single year shows up clearly on the X-axis
plt.xticks(batsman['index'], rotation=45)

# 7. Add a clear legend to identify who is who
plt.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='none')

# 8. Adjust spacing so labels don't get cut off, then open the window
plt.tight_layout()
plt.show()