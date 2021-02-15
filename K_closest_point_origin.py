import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        #TC- (nlogk)
        maxHeap = []
        for point in points:
            dis = -1* (sqrt(point[0]**2 + point[1]**2))
            if len(maxHeap) < K:
                heapq.heappush(maxHeap, [dis,point])
            else: 
                if dis > maxHeap[0][0]:
                    heapq.heappushpop(maxHeap,[dis,point])
                    
        return [x[1] for x in maxHeap]
