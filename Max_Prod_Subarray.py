class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # loop from front and loop from back
        
        if len(nums) == 0:
            return 0
        
        dp = [1] * len(nums)
        reverse_dp = [1] * len(nums)
        dp[0] = nums[0]
        reverse_dp[len(nums)-1] = nums[len(nums)-1]
        
        for i in range(1,len(nums)): 
            if dp[i-1] != 0 and  nums[i] != 0:
                dp[i] = nums[i] * dp[i-1] 
            else:
                dp[i] = nums[i]
            
        for i in range(len(nums)-2, -1, -1): 
            if reverse_dp[i+1] != 0 and nums[i] != 0:
                reverse_dp[i] = nums[i] * reverse_dp[i+1]
            else:
                reverse_dp[i] = nums[i]

        return max(max(dp), max(reverse_dp))
        
        
