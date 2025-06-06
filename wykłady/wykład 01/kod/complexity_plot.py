import numpy as np
import matplotlib.pyplot as plt

# Generate data points
n = np.linspace(1, 100, 1000)

# Calculate different complexities
constant = np.ones_like(n)  # O(1)
logarithmic = np.log2(n)  # O(log n)
linear_1 = n  # O(n)
linear_2 = 2 * n  # O(n) with coefficient 2
quadratic = n**2  # O(n^2)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))  # Square figure

# Plot the complexities
ax.plot(n, constant, label='Constant', linestyle='-')
ax.plot(n, logarithmic, label='Logarithmic', linestyle='--')
ax.plot(n, linear_1, label='Linear (c=1)', linestyle='-.')
ax.plot(n, linear_2, label='Linear (c=2)', linestyle=':')
# ax.plot(n, quadratic, label='Quadratic')

# Customize the plot
ax.set_xlabel('Input Size (n)')
ax.set_ylabel('Number of Operations')
ax.set_title('Comparison of Algorithm Complexities')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left')

# # Make axes equal and boxed
# ax.set_aspect('equal')
# ax.set_box_aspect(1)

# Add padding to axes to better show all functions
# ax.set_xlim(-5, 105)
# ax.set_ylim(-5, 105)

# Save the plot
plt.tight_layout()
plt.savefig('lecture_1/complexity_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Print example values
print("\nExample values for different input sizes:")
test_sizes = [1, 10, 100]
for size in test_sizes:
    print(f"\nInput size n = {size}:")
    print(f"Constant (1):  {1}")
    print(f"Constant (2):  {2}")
    print(f"Logarithmic:   {np.log2(size):.2f}")
    print(f"Linear:        {size}")
    print(f"Quadratic:     {size**2}")