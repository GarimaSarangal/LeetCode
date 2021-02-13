class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # https://leetcode.com/problems/group-anagrams/  
        #TC - O(NKlogK) - where NN is the length of strs, and KK is the maximum length of a string in strs.
        #O(NK) 
        ans  = collections.defaultdict(list)
        
        for s in strs:
            ans[tuple(sorted(s))].append(s)
            
        return ans.values()
        
           
