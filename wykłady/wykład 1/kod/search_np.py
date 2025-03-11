import time
import random
import csv
import numpy as np
from typing import List, Callable, Tuple

def numpy_linear_search(arr: np.ndarray, target: int) -> int:
    result = np.where(arr == target)[0]
    return result[0] if len(result) > 0 else -1

def numpy_binary_search(arr: np.ndarray, target: int) -> int:
    index = np.searchsorted(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1

def measure_execution_time(func: Callable[[], int]) -> Tuple[float, int]:
    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    return end_time - start_time, result

def main():
    sizes_count = 10
    sizes_skip = 5000000
    runs_per_size = 5

    size = sizes_skip
    sizes = [size + i * sizes_skip for i in range(sizes_count)]

    with open('lecture_1/search_results_numpy.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Size', 'Run', 'Target', 'LinearTime', 'BinaryTime', 'LinearResult', 'BinaryResult'])

        np.random.seed(int(time.time()))

        for n in sizes:
            print(f"Testing array size: {n}")
            
            # Create sorted array of size n using NumPy
            arr = np.arange(n)
            
            for run in range(runs_per_size):
                target = random.randrange(n)
                # target = int(0.5 * n + 1)
                
                time_linear, index_linear = measure_execution_time(
                    lambda: numpy_linear_search(arr, target)
                )
                
                time_binary, index_binary = measure_execution_time(
                    lambda: numpy_binary_search(arr, target)
                )

                # Write to console
                print(f"  Run {run + 1}: Target={target} "
                      f"Linear={time_linear:.8f} Binary={time_binary:.8f}")

                # Write to file
                writer.writerow([n, run + 1, target, time_linear, time_binary, 
                               index_linear, index_binary])
            print()

    print("Results have been saved.")

if __name__ == "__main__":
    main()