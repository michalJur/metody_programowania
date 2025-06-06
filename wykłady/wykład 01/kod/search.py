import time
import random
import csv
from typing import List, Callable, Tuple

def linear_search(arr, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def measure_execution_time(func: Callable[[], int]) -> Tuple[float, int]:
    start_time = time.perf_counter()  # Using perf_counter for higher precision
    result = func()
    end_time = time.perf_counter()
    return end_time - start_time, result

def main():
    sizes_count = 10
    # skip = 50000000
    sizes_skip = 5000000
    runs_per_size = 5

    size = sizes_skip
    sizes = [size + i * sizes_skip for i in range(sizes_count)]

    with open('search_results_python.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Size', 'Run', 'Target', 'LinearTime', 'BinaryTime', 'LinearResult', 'BinaryResult'])

        random.seed(time.time())

        for n in sizes:
            print(f"Testing array size: {n}")
            
            # Create sorted array of size n
            arr = list(range(n))
            
            for run in range(runs_per_size):
                target = random.randrange(n)
                # target = int(0.5 * n + 1)
                
                time_linear, index_linear = measure_execution_time(
                    lambda: linear_search(arr, target)
                )
                
                time_binary, index_binary = measure_execution_time(
                    lambda: binary_search(arr, target)
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