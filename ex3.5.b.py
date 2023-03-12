from matplotlib import pyplot as plt
import timeit

# Used to create a node
class ListNode:
    def __init__(self, val, prio):
        self.value = val
        self.priority = prio
        self.next = None

    def getPrio(self):
        return self.priority

#-------------------------------------------------------------------------------------------------------------------------------#

"""
Unsorted Linked List
append: add to end of list, head becomes first element and tail becomes the last element
remove: removes the first element with the highest priority, go through entire linked list and find highest priority
"""
class List1: 
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val, prio):
        node = ListNode(val, prio)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
        
    def remove(self):
        if self.head is None:
            return
        else:
            prevNode = None
            remNode = self.head
            tmp = self.head
            
            while tmp.next is not None:
                if tmp.next.getPrio() > remNode.getPrio():
                    prevNode = remNode
                    remNode = tmp.next
                tmp = tmp.next
            
            if prevNode is None:
                self.head = remNode.next
            else:
                prevNode.next = remNode.next

    def printNode(self, node):
        print(f"Value: {node.value} , Priority: {node.priority}")
        return node.next
    
#-----------------------------------------------------------------------------------------------------------------------#

"""
Sorted Linked List
Idea: group together nodes with equal priority, with higher priority at front of list
remove: remove first node if not empty

Essentially, the "first in" is at the beginning of its own group of similar priorities, higher the priority the closer it is to the beginning of the array 
"""

class List2:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val, prio):        # oh boy, lots of ifs
        node = ListNode(val, prio)
        if self.head is None:           # if queue is empty just add it
            self.head = node
            self.tail = self.head
        else:
            tmp = self.head
            while True:
                if tmp.next is None:    # if there is only one element
                    if self.head.next is None:
                        tmp = self.head
                        if (node.priority > self.head.priority):
                            self.head = node
                            self.head.next = tmp
                        else:
                            self.head.next = node
                        self.tail = self.head.next
                    else:
                        self.tail.next = node
                        self.tail = self.tail.next
                    break
                elif (node.priority > tmp.next.priority):    # will add the "tail" of the same priority group, or make its own if its the first one
                    if tmp.next is None:
                        self.tail.next = node
                        self.tail = self.tail.next
                        break
                    else:
                        node.next = tmp.next
                        tmp.next = node
                        break
                tmp = tmp.next
        return

    def remove(self):                       # removes first element
        if self.head is not None:
            self.head = self.head.next
        else:
            return

    def printNode(self, node):              # prints node value and priority
        print(f"Value: {node.value} , Priority: {node.priority}")
        return node.next

#------------------------------------------------------------------------------------------------------------#
# This short bundle of code is used to check if the queues work as they should
# Try if you want
"""
pq = List1()
pq.append(1,1)
pq.append(4,13)
pq.append(2,4)
pq.append(4,4)
pq.append(3,3)
pq.append(4,9)

pq.remove

node = pq.head
while node is not None:
    pq.printNode(node)
    node = node.next

print("------------------------------")

pq = List2()
pq.append(1,1)
pq.append(4,13)
pq.append(2,4)
pq.append(4,4)
pq.append(3,3)
pq.append(4,9)

pq.remove()

node = pq.head
while node is not None:
    pq.printNode(node)
    node = node.next
"""


# Rest of code is used to test each implementation

def both1():
    pq = List1()
    priorityList = list(range(1, 101))
    priorityIndex = 0
    for i in range(1000):
        pq.append(i, priorityList[priorityIndex])
        priorityIndex += 1
        if priorityIndex == 99:
            priorityIndex = 0

    for i in range(500):
        pq.remove()

def both2():
    pq = List2()
    priorityList = list(range(1, 101))
    priorityIndex = 0
    for i in range(1000):
        pq.append(i, priorityList[priorityIndex])
        priorityIndex += 1
        if priorityIndex == 99:
            priorityIndex = 0

    for i in range(500):
        pq.remove()

# Start of timing
timeBoth1 = []
timeBoth2 = []

for i in range(100):
    time = timeit.timeit(lambda: both1(), number=10)
    timeBoth1.append(time)

for i in range(100):
    time = timeit.timeit(lambda: both2(), number=10)
    timeBoth2.append(time)

ave1 = sum(timeBoth1)/len(timeBoth1)
ave2 = sum(timeBoth2)/len(timeBoth2)
print()
print(f'The min for the unsorted linked list is: {min(timeBoth1)}')
print(f'The average for the unsorted linked list is: {ave1}')
print(f'The max for the unsorted linked list is: {max(timeBoth1)}')
print()
print(f'The min for the sorted linked list is: {min(timeBoth2)}')
print(f'The average for the sorted linked list is: {ave2}')
print(f'The max for the sorted linked list is: {max(timeBoth2)}')

x = list(range(1, 101))
plt.plot(x, timeBoth1, label='Unsorted')
plt.plot(x, timeBoth2, label='Sorted')
plt.xlabel("Trial")
plt.ylabel("Time")
plt.legend()
plt.show()



