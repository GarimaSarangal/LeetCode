class Solution:
    def isValid(self, s: str) -> bool:
    #https://leetcode.com/problems/valid-parentheses/solution/
        dstack = []
        dct = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for i in s:
            if i in dct:
                top_ele = dstack.pop() if dstack else "#"
                if dct[i] != top_ele:
                    return False
            else:
                dstack.append(i)
            
        return not dstack
            
        #TC - O(n)
        #SC - O(n)
