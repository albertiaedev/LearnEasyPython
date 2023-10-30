# The _heapq module provides classes and functions for implementing priority queues.

import _heapq

queue = []

heapq.heappush(queue, 1)
heapq.heappush(queue, 3)
heapq.heappush(queue, 2)

print(heapq.heappop(queue))
print(heapq.heappop(queue))
print(heapq.heappop(queue))