class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, H = len(needle), len(haystack)
        
        if N == 0:
            return 0

        ph = 0
        while ph < H - N + 1:
            # find the position of the first needle character
            # in the haystack string
            while ph < H - N + 1 and haystack[ph] != needle[0]:
                ph += 1
            
            # compute the max match string
            curr_len = pL = 0
            while pL < N and ph < H and haystack[ph] == needle[pL]:
                ph += 1
                pL += 1
                curr_len += 1
            
            # if the whole needle string is found,
            # return its start position
            if curr_len == N:
                return ph - N
            
            # otherwise, backtrack
            ph = ph - curr_len + 1
            
        return -1
    
#TC - O((N-L)L)
#SC - O(1)
                
        
