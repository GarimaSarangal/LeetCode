class Solution:
    def firstUniqChar(self, s: str) -> int:
    #https://leetcode.com/problems/first-unique-character-in-a-string/
     # Solution 1
        dic = collections.Counter(s)
        
        for idx,value in enumerate(s):
            if dic[value] == 1:
                return idx
        return -1
        
        # Solution 2
#         dic = collections.Counter(s)
#         a = []
        
#         for key,value in dic.items():
#             if value == 1:
#                 a.append(s.index(key))
                
                
#         if len(a) > 0:
#             return min(a)
#         else:
#             return -1
            
        
                
