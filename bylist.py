STACK:

stack=[1,2,3,4]
stack.append(5)
stack.append(6)
stack.pop()

QUEUE:

from collections import deque   #To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.
queue=deque(["abc","def","ghi","jkl"])
queue.append("mno")
queue.append("pqr")
queue.popleft()
queue
