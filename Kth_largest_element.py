import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #O(NK)
#         n = len(nums)-1
#         for i in range(n, n-k, -1):
#             max_idx = i
#             for j in range(i):
#                 if nums[max_idx] <= nums[j]:
#                     max_idx = j
#             nums[i], nums[max_idx] = nums[max_idx], nums[i]
#         return nums[-k]
               
     #O(nlogk)
        if len(nums) * k == 0 :
            return []
        
        if k == 1:
            return max(nums)
        
        minHeap = []
        
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap,num)
            else:
                if num > minHeap[0]:
                    heapq.heappushpop(minHeap,num)
        
        return minHeap[0]
   
            
