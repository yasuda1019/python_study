from typing import Counter


a = int(input('整数A'))
b = int(input('整数B'))
a,b =  sorted([a,b])
Counter = a
while Counter <= b:
    print(Counter,end='')
    Counter = Counter + 1
print()