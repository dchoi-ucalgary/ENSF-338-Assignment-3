# ex3.5.a_experiment.py

import timeit
import matplotlib.pyplot as plt
import numpy as np

# Inefficient implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return 0

# Efficient implementation
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

# Generate large input
arr = list(range(1000000))
target = 999999

# Measure the execution time of each implementation
num_measurements = 100
inefficient_times = []
efficient_times = []

for i in range(num_measurements):
    inefficient_time = timeit.timeit(lambda: linear_search(arr, target), number=1)
    inefficient_times.append(inefficient_time)

    efficient_time = timeit.timeit(lambda: binary_search(arr, target), number=1)
    efficient_times.append(efficient_time)

# Plot the distribution of measured values
bins = np.linspace(0, max(inefficient_times + efficient_times), 20)
plt.hist(inefficient_times, bins, alpha=0.5, label='Inefficient')
plt.hist(efficient_times, bins, alpha=0.5, label='Efficient')
plt.legend(loc='upper right')
plt.xlabel('Execution Time (s)')
plt.ylabel('Frequency')
plt.show()

# Print the aggregate of measured values
print("Inefficient implementation:")
print("Minimum time: ", min(inefficient_times))
print("Average time: ", sum(inefficient_times) / num_measurements)
print("Maximum time: ", max(inefficient_times))

print("Efficient implementation:")
print("Minimum time: ", min(efficient_times))
print("Average time: ", sum(efficient_times) / num_measurements)
print("Maximum time: ", max(efficient_times))
