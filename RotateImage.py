class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #https://leetcode.com/problems/rotate-image/solution/
#Solution 1
        # for rotation matrix reverse and then transpose
        # reverse first
        matrix.reverse()
        n = len(matrix[0])
        
        # transpose of matrix
        for i in range(n):
            for j in range(i,n):
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
