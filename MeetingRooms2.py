import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return
        
        intervals.sort()
        
        freeRooms = []
        
        heapq.heappush(freeRooms, intervals[0][1])
        
        for i in intervals[1:]:
            if freeRooms[0] <= i[0]:
                heapq.heappop(freeRooms)
                
            heapq.heappush(freeRooms, i[1])
            
        return len(freeRooms)
