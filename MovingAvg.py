class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        
        queue.append(val)
        
        window_sum = sum(queue[-size:])
        
        return window_sum / min(len(queue), size)
        
