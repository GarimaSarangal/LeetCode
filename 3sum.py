class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #https://leetcode.com/problems/3sum/
#Two pointers SOLUTION2 - FASTEST - do this
        result = []
      
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums,i, result)
        return result
    
    def twoSum(self, nums:List[int], i: int, result:List[List[int]]):
        lo, hi = i+1, len(nums)-1
        
        while(lo < hi):
            sum_o = nums[i] + nums[lo] + nums[hi]
            if sum_o < 0:
                lo += 1
            elif sum_o > 0:
                hi -= 1
            else:
                result.append([nums[i] , nums[lo] , nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
                    
# Time Complexity: O(n^2)

# Sorting the array takes O(nlogn), so overall complexity is O(nlogn + n^2)). This is asymptotically equivalent to O(n^2)

# Space Complexity: O(logn) to O(n) for the hashset.
        
        

    
#hashset SOLUTION1        
#         result = []
      
#         nums.sort()
        
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 break
#             if i == 0 or nums[i] != nums[i-1]:
#                 self.twoSum(nums,i, result)
#         return result
    
#     def twoSum(self, nums:List[int], i: int, result:List[List[int]]):
#         seen = set()
#         j = i + 1
#         while j < len(nums):
#             comp = -nums[i]-nums[j]
#             if comp in seen:
#                 result.append([nums[i],nums[j],comp])
#                 while j+1 < len(nums) and nums[j] == nums[j+1]:
#                     j += 1
                
#             seen.add(nums[j])
#             j += 1

# Time Complexity: O(n^2)

# Sorting the array takes O(nlogn), so overall complexity is O(nlogn + n^2)). This is asymptotically equivalent to O(n^2)

# Space Complexity: O(n) for the hashset.
        
      
