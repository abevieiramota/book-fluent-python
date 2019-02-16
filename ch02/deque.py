from collections import deque 

dq = deque(range(10), maxlen=10)

print(dq)

# push to right
dq.rotate(3)

print(dq)

# with negative n, push to left
dq.rotate(-4)

print(dq)

dq.appendleft(-1)

print(dq)

# add to right
dq.extend([11, 22, 33])

print(dq)

dq.extendleft([10, 20, 30, 40])

print(dq)