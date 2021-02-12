class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #https://leetcode.com/problems/most-common-word/
    #TC-O(N+M)
    #SC-O(N+M)
        dct = {}
        banned = set(banned)
        
        norm = "".join([c.lower() if c.isalnum() else " " for c in paragraph])
        
        paragraph = norm.split()
        
        for word in paragraph:
            if word not in banned:
                if word not in dct: 
                    dct[word] = 1
                else:
                    dct[word] += 1
        
        return max(dct.items(), key=operator.itemgetter(1))[0]
        
        
