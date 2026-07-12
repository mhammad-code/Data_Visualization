import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate 1000 random points from a Normal Distribution
normal_data = np.random.normal(loc=0, scale=1, size=1000)

# Plot the distribution
sns.histplot(normal_data, kde=True, color="purple", bins=30)

plt.title("Normal Distribution Visualization")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()