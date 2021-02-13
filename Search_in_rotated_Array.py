class Solution:
    def search(self, nums: List[int], target: int) -> int:
    #https://leetcode.com/problems/search-in-rotated-sorted-array/
    #TC -  O(logn)
    #SC - O(1)
        low, high = 0 , len(nums)-1
        if len(nums) == 1 and target == nums[0]:
            return 0
        
        while(low <= high):
            mid = floor((low + high) / 2)
            # print("mid" , nums[mid])
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
            
            
