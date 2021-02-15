import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #TC - O(nlogn)
        freq = {}
        heap = []
        
        if len(nums) * k == 0:
            return 
        
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
       
        for key, value in freq.items():
            if len(heap) < k:
                heapq.heappush(heap,(value, key))
            else:
                heapq.heappushpop(heap, (value,key))
    
        return [val for freq,val in heap]
                
            
            
        
