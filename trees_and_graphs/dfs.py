class TreeNode:
    def __init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root:TreeNode) -> int:
    if root == None:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left,right) + 1

# Given the root of a binary tree and an integer targetSum, return true if there 
# is a path from the root to a leaf such that the sum of the nodes on the path
# is equal to targetSum, and return false otherwise.

def pathSum(root,targetSum):
    def dfs(node,curr):
        if not node:
            return False
        if node.left == None and node.right == None: #its a leaf
            return (curr + node.val) == targetSum
        curr += node.val
        left = dfs(root.left,curr)
        right = dfs(root.right,curr)
        return left or right
    return dfs(root,0)

# good nodes
def goodNode(root):
    def dfs(node,maxSoFar):
        if node == None:
            return 0
        left = dfs(left,max(maxSoFar,node.val))
        right = dfs(right,max(maxSoFar,node.val))
        ans = left + right
        if node.val >= maxSoFar:
            ans+=1

    return dfs(root,float('-inf'))

# lowest common ancestor
def lowestCA(root,p,q):
    if root == None:
        return None
    
    if root == p or root == q:
        return root
    left = lowestCA(root.left,p,q)
    right = lowestCA(root.right,p,q)

    if left and right:
        return root
    
    if left:
        return left
    return right

# min dept - The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
def minDepth(root):
    if not root:
        return 0
    children = [root.left, root.right]
    if not any(children):
        return 1
    min_depth = float('inf')
    for c in children:
        if c:
            min_depth = min(minDepth(c),min_depth)
    return min_depth + 1




c = TreeNode(0)
a = TreeNode(1)
b = TreeNode(2)

c.left = a
c.right = b
