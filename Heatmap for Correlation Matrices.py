import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset("iris")
corr_matrix = iris.drop(columns="species").corr()

# Plot the heatmap with values annotated inside the squares
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)

plt.title("Correlation Coefficient Matrix")
plt.show()