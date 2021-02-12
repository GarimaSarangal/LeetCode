class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #https://leetcode.com/problems/missing-number/solution/
        #TC - O(n)
        #SC - O(1)
    #Solution 1
        n = len(nums)
        sum_n = (n * (n+1)) // 2
        sum_a = sum(nums)
        return sum_n-sum_a
            
                
                
        
