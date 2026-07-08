import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''iris=pd.read_csv('iris.csv')
print(iris)
iris['Species']=iris['Species'].replace({'Iris-setosa':0, 'Iris-virginica':1,'Iris-versicolor':2})
iris.sample(5)
plt.scatter(iris['SepalLengthCm'],iris['SepalWidthCm'],c=iris['Species'])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Width vs Sepal Length')
plt.colorbar()
plt.show()
'''
# 1. Create ONE canvas
plt.figure(figsize=[18, 10])

# 2. Load and sample data
df = pd.read_csv('batter.csv')
df = df.head(100).sample(25, random_state=5)

# 3. Plot the scatter points
plt.scatter(df['avg'], df['strike_rate'], color='blue', zorder=1)
plt.xlabel('Average')
plt.ylabel('Strike Rate')
plt.title('Batter Performance (Top 25 Sampled)')
plt.axhline(y=130, color='red')

plt.axhline(y=140, color='pink')
plt.axvline(x=30, color='blue')
# 4. Loop through and add text ON THE SAME CANVAS
for i in range(df.shape[0]):
    plt.text(
        df['avg'].values[i] + 0.2,       # Added a small offset (+0.2) so text isn't right on top of the dot
        df['strike_rate'].values[i],
        df['batter'].values[i],
        fontsize=9                       # Optional: makes the text highly readable
    )

# 5. Show the combined plot
plt.show()