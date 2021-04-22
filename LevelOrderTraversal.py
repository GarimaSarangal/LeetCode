# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        levels = []
        queue = collections.deque() 
        
        if root:
            levels.append([root.val])
            queue.append(root)
        else:
            return
         
        while queue:
            level = []

            for i in range(len(queue)):
                ele = queue.popleft()
                if ele.left:
                    queue.append(ele.left)
                    level.append(ele.left.val)
                if ele.right: 
                    queue.append(ele.right)
                    level.append(ele.right.val)
            
            if level:
                levels.append(level)   
            
        return levels
            
