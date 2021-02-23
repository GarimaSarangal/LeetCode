# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

# https://leetcode.com/problems/serialize-and-deserialize-bst/ O(n) O(n)

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(node):
            if not node:
                res.append("None,")
                return None
            
            res.append(str(node.val) + ",")
            dfs(node.left)
            dfs(node.right)
        
        res = []
        dfs(root)
        return "".join(res)
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def createTree(li):
            if li[0] == "None":
                li.pop(0)
                return None
            
            root = TreeNode(li[0])
            li.pop(0)
            root.left = createTree(li)
            root.right = createTree(li)
            
            return root
            
        dataSplit = data.split(",")
        root = createTree(dataSplit)
        
        return root
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
