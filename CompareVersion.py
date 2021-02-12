class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
    #https://leetcode.com/problems/compare-version-numbers/
    #TC - O(N+M+max(N,M))
    #Sc - O(N+M)
        v1 = [int(x) for x in version1.split(".")] #N
        v2 = [int(x) for x in version2.split(".")] #M
    
        for x in range(max(len(v1), len(v2))):
            if x < len(v1):
                version1 = v1[x]
            else:
                version1 = 0
                
            if x < len(v2):
                version2 = v2[x]
            else:
                version2 = 0
                
            if version1 > version2:
                return 1
            elif version1 < version2:
                return -1
            
        return 0