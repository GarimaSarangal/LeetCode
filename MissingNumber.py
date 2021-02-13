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
            
                
     #SOlution 2 - Hashset
      #TC - O(n)
      #SC - O(n)
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
                
        
