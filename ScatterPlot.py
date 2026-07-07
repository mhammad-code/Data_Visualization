import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
x = np.linspace(-10,10,50)

y = 10*x + 3 + np.random.randint(0,300,50)

plt.scatter(x,y)
plt.show()
df = pd.read_csv('batter.csv')
df = df.head(50)
print(df)
plt.scatter(df['avg'], df['strike_rate'], color='black', marker='D')
plt.title('Avg and SR analysis of Top 50 Batsman')
plt.xlabel('Average')
plt.ylabel('SR')

# Add this line!
plt.show()
