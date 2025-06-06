import pandas as pd
import matplotlib.pyplot as plt

# Read all CSV files
df_python = pd.read_csv('lecture_1/search_results_python.csv')
df_cpp = pd.read_csv('lecture_1/search_results_cpp.csv')
df_numpy = pd.read_csv('lecture_1/search_results_numpy.csv')

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot Python results
# ax.scatter(df_python['Size'], df_python['LinearTime'], alpha=0.6, label='Python Linear Search', marker='o')
# ax.scatter(df_python['Size'], df_python['BinaryTime'], alpha=0.6, label='Python Binary Search', marker='s')

# Plot C++ results
ax.scatter(df_cpp['Size'], df_cpp['LinearTime'], alpha=0.6, label='C++ Linear Search', marker='^')
ax.scatter(df_cpp['Size'], df_cpp['BinaryTime'], alpha=0.6, label='C++ Binary Search', marker='D')

# Plot NumPy results
ax.scatter(df_numpy['Size'], df_numpy['LinearTime'], alpha=0.6, label='NumPy Linear Search', marker='*')
ax.scatter(df_numpy['Size'], df_numpy['BinaryTime'], alpha=0.6, label='NumPy Binary Search', marker='p')

# Customize the plot
ax.set_xlabel('Array Size')
ax.set_ylabel('Time (seconds)')
ax.set_title('Search Performance Comparison: Python vs C++ vs NumPy')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left')

# Save the plot
plt.tight_layout()
plt.savefig('lecture_1/search_comparison_all.png', dpi=300, bbox_inches='tight')
plt.close()

# Print statistics for all implementations
print("\nSummary Statistics:")
for size in df_python['Size'].unique():
    print(f"\nArray Size: {size}")
    py_data = df_python[df_python['Size'] == size]
    cpp_data = df_cpp[df_cpp['Size'] == size]
    numpy_data = df_numpy[df_numpy['Size'] == size]
    
    print("Python Implementation:")
    print(f"  Linear Search - Mean: {py_data['LinearTime'].mean():.8f}s")
    print(f"  Binary Search - Mean: {py_data['BinaryTime'].mean():.8f}s")
    
    print("C++ Implementation:")
    print(f"  Linear Search - Mean: {cpp_data['LinearTime'].mean():.8f}s")
    print(f"  Binary Search - Mean: {cpp_data['BinaryTime'].mean():.8f}s")
    
    print("NumPy Implementation:")
    print(f"  Linear Search - Mean: {numpy_data['LinearTime'].mean():.8f}s")
    print(f"  Binary Search - Mean: {numpy_data['BinaryTime'].mean():.8f}s")