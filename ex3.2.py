import json
from matplotlib import pyplot as plt
import timeit

# regular recursive binary search function
def binarySearch(arr, first, last, key):
    if first <= last:
        mid = int((first + last)/2)
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binarySearch(arr, first, mid-1, key)
        elif key > arr[mid]:
            return binarySearch(arr, mid+1, last, key)
    else:
        return -1

# this is to start the binary search with a chosen mid
def binaryStart(arr, first, last, key, mid):
    if first <= last:
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binarySearch(arr, first, mid-1, key)
        elif key > arr[mid]:
            return binarySearch(arr, mid+1, last, key)
    else:
        return -1

with open("ex2data.json", "r") as inF:
    data = json.load(inF)

with open("ex2tasks.json", "r") as inF:
    tasks = json.load(inF)

# 499474 is the midpoint
low = 0
high = len(data)-1
midpoints = [499378, 499403, 499425, 499445, 499474, 499492, 499508, 499534, 499558]  # midpoints chosen
mid_index = [499916, 499937, 499958, 499978, 500000, 500021, 500041, 500062, 500080]  # index of midpoints in data
best_mid = []

# test for tasks
for t in tasks:
    best_time = 1000
    best_index = 0
    for m in mid_index:
        time = timeit.timeit(lambda: binaryStart(data, low, high, t, m), number=10)
        if time < best_time:
            best_time = time
            best_index = mid_index.index(m)
    best_mid.append(best_index)

# Show to tally
best = [i+1 for i in best_mid]
my_dict = {i:best.count(i) for i in best}
sort = sorted(my_dict.items())
new_dict = dict(sort)
print(new_dict)

# graph
plt.scatter(tasks, best)
plt.xlabel("Tasks")
plt.ylabel("Midpoints")
plt.show()