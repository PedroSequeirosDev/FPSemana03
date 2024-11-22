
from collections import deque
number = input("write a set of numbers ")
group = deque(number.split())
print(group)

for i in range (len(group)):
    squared = group.pop()
    print(int(squared)**2)



