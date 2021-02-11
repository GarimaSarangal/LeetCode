class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #https://leetcode.com/problems/3sum-closest/solution/
        diff = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            lo, hi = i+1, len(nums)-1
            while(lo < hi):
                sum_o = nums[i] + nums[lo] + nums[hi]
                if abs(target-sum_o) < abs(diff):
                    diff = target - sum_o
                    print(diff)
                if sum_o < target :
                    lo += 1
                else: 
                    hi -= 1
                    
            if diff == 0:
                break
                
        return target - diff
            
#TC- O(n2)
#SC - O(logn) to O(n)
