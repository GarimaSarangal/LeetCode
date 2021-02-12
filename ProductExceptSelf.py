class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    #https://leetcode.com/problems/product-of-array-except-self/
    #TC - O(n)
    #SC - O(n)
    
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            dp[i] = dp[i-1] * nums[i-1]
            
        prod = 1
            
        for i in range(len(nums)-1,-1,-1):
            dp[i] = dp[i] * prod
            prod = prod * nums[i]
            
        return dp
        
