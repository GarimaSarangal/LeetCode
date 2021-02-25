class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
            
        lNums1 = len(nums1)
        lNums2 = len(nums2)
        
        
        low , high = 0, lNums1
        
        while low <= high:

            partNums1 = (low+high)//2
            
            partNums2 = ((lNums1 + lNums2 + 1) // 2) - partNums1
            

            max1 = -math.inf if partNums1 == 0 else nums1[partNums1-1]
            min1 = math.inf if partNums1 == lNums1 else nums1[partNums1]

            max2 = -math.inf if partNums2 == 0 else nums2[partNums2-1]
            min2 = math.inf if partNums2 == lNums2 else nums2[partNums2]
        
            if max1 <= min2 and max2 <= min1:
                if (lNums1+lNums2) % 2 == 0:
                    return (max(max1,max2) + min(min1,min2))/2
                else:
                    return max(max1,max2)
                
            elif max1 > min2:
                high = partNums1 - 1
            else:
                low = partNums1 + 1
                
        raise ValueError("Arrays must be sorted")
