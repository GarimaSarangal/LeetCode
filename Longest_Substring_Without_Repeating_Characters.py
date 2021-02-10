class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #sliding window and hashmap
        #O(n) and O(min(m,n))
        
        dic = {}
        n = len(s)
        length = 0
        i = 0
        
        for j in range(n):
            if s[j] in dic:
                i = max(dic[s[j]],i)
                
            length = max(length, j-i+1)
            dic[s[j]] = j+1
                
        return length
