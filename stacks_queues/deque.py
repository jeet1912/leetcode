from collections import deque

queue = deque() 
# can add and delete elements from both end
# queue.popleft(), queue.pop()

class NumRecentCalls:
    
    def __init__(self) -> None:
        self.sliding_window = deque()

    def ping(self,t : int) -> int:
        self.sliding_window.append(t)
        while self.sliding_window[0] < t - 3000:
            self.sliding_window.popleft()
        return len(self.sliding_window)
    

class MovingAverage:

    def __init__(self,size: int) -> None:
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        win_sum = sum(queue[-size:])
        return win_sum/min(self.size,len(queue))

ma = MovingAverage(size=3)
ma.next(1)
ma.next(10)
ma.next(3)
print(ma.next(5))

