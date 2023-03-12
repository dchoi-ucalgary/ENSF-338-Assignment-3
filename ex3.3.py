import sys

list1 = []
size = sys.getsizeof(list1)
print("Initial size is: ", size)
for i in range(64):
    list1.append(i)
    if (sys.getsizeof(list1) != size):
        size = sys.getsizeof(list1)
        print("Size changed to: ", size, " Happened at:", i)