import matplotlib.pyplot as plt
import numpy as np

# Sample Data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([45, 51, 52, 60, 68, 70, 80, 81, 89, 95])

# Calculate Linear Regression (y = mx + c)
m, c = np.polyfit(x, y, 1)  # 1 means linear (degree 1)

# Initialize the plot
plt.figure(figsize=(8, 5))

# Plot elements
plt.scatter(x, y, color='blue', label='Data Points')  # Scatter plot
plt.plot(x, m*x + c, color='red', linewidth=2, label='Regression Line')  # Regression line

# Styling
plt.title("Matplotlib: Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Display the static plot
plt.show()