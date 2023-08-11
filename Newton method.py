import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the Seaborn style to whitegrid
sns.set(style="whitegrid")

# Define the function
def equation(x):
    return (2 * x ** 2) - 200

# Define the derivative of the function
def derivative(x):
    return 4 * x

# Newton-Raphson method for finding tangent points
def newton_iteration(x):
    return x - equation(x) / derivative(x)

# Initial value for x
x = -100
x_val = []

# Perform Newton-Raphson iterations
for i in range(10):
    eq = equation(x)
    diff = derivative(x)
    x_new = x - float(eq / diff)
    x = x_new
    x_val.append(x_new)

# Compute corresponding y values
y_val = [equation(x) for x in x_val]

# Generate x values for the plot
x_plot = np.linspace(min(x_val) - 20, max(x_val) + 20, 1000)

# Compute corresponding y values for the plot
y_plot = equation(x_plot)

# Set up the figure and axis
plt.figure(figsize=(10, 8))
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Plot the function
plt.plot(x_plot, y_plot, label='(2*x ** 2) - 200', color='#1f77b4', linewidth=2)

# Highlight tangent points
plt.scatter(x_val, y_val, color='#ff7f0e', label='Tangent Points', s=70, zorder=5)

# Plot tangents at the selected points
for i in range(len(x_val)):
    tangent = derivative(x_val[i]) * (x_plot - x_val[i]) + y_val[i]
    plt.plot(x_plot, tangent, linestyle='--', color='#9467bd', linewidth=1, alpha=0.7, label=f'Tangent at x={x_val[i]:.2f}')

# Add labels and title
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('x', fontsize=14, color='#333333')
plt.ylabel('y', fontsize=14, color='#333333')
plt.title('Graph of (2*x ** 2) - 200 and Tangents', fontsize=16, color='#333333')

# Customize legend
plt.legend(fontsize=12)

# Set background color
ax.set_facecolor('#f7f7f7')

# Set axis limits
plt.xlim(min(x_val) - 20, max(x_val) + 20)
plt.ylim(min(y_val) - 100, max(y_val) + 100)

# Show the plot
plt.show()

# Display the list of x values from Newton-Raphson iterations
print(x_val)

