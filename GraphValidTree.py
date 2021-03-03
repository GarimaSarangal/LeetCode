class UnionFind:
    def __init__(self,n):
        #makeset
        self.parent = [node for node in range(n)]
        self.size = [1] * n
        
    def find(self,A):
        root = A
        while root! = self.parent[root]:
            root = self.parent[root]
        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root
    
    def union(self, A,B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return False
        
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        if self.size[root_A] > self.size[root_B]:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        return True
            
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # SOLUTION 3 - UNION FIND
         # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n-1 : return False
        
        # Condition 2: The graph must contain a single connected component.
        # Create a new UnionFind object with n nodes. 
        uf = UnionFind(n)
        
        # Add each edge. Check if a merge happened, because if it 
        # didn't, there must be a cycle.
        for A,B in edges:
            if not uf.union(A,B):
                return False
            
        # If we got this far, there's no cycles!
        return True
        
        #SOLUTION 2 - 
        
        #cycle check
        if len(edges) != n-1 : return False
        
        adj_list = [[] for _ in range(n)]
        
        for A,B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        
        stack = [0]
        seen = {0}
        
        while stack:
            node = stack.pop()
            for nei in adj_list[node]:
                if nei in seen:
                    continue
                stack.append(nei)
                seen.add(nei)
                
        # check if graph is fully connected
        return len(seen) == n
        
        
        #SOLUTION 1 - Iterative DFS:
        
        #case 1 - if edges != vertices-1 then false
        if len(edges) != n-1 : return False
        
        adj_list = [[] for _ in range(n)]
        
        for A,B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
            
        parent = {0: -1} #root node
        stack = [0]
        
        # cycle check
        while stack:
            node = stack.pop()
            for nei in adj_list[node]:
                if nei == parent[node]:
                    continue
                if nei in parent:
                    return False
                stack.append(nei)
                parent[nei] = node
                
    #len(parent) == n checking if all nodes were reachable, fully connected graph
        return len(parent) == n
        
