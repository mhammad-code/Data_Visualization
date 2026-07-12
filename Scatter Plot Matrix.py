import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Using Seaborn's built-in 'iris' dataset as an example
iris = sns.load_dataset("iris")

# Plot pairwise relationships grouped by species
sns.pairplot(iris, hue="species", palette="Set2")
plt.show()