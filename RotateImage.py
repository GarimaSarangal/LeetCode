class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #https://leetcode.com/problems/rotate-image/solution/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#Solution 1
     #reversed
        n = len(matrix)
        e = n-1
        for i in range(n//2):
            matrix[i], matrix[e] = matrix[e], matrix[i]
            e -= 1
        
        #transpose 
        for i in range(len(matrix[0])):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

#Solution 2
# or do transpose and reverse
#         n = len(matrix[0])
#         # transpose of matrix
#         for i in range(n):
#             for j in range(i,n):
#                 matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                
                
#         # reverse a matrix
#         for i in range(n):
#             matrix[i].reverse()
       
                
#Solution 3
# for rotation matrix reverse and then transpose
#         # reverse first
#         matrix.reverse()
#         n = len(matrix[0])
        
#         # transpose of matrix
#         for i in range(n):
#             for j in range(i,n):
#                 matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
            
