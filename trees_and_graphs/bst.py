#Sum of all the nodes, whose value is in the range [low,high]

def sumNodes(root,low,high):
    if not root:
        return 0
    ans = 0
    if low<=root.val<=high:
        ans+=root.val
    if low < root.val:
        ans += sumNodes(root.left,low,high)
    if high > root.val:
        ans += sumNodes(root.right,low,high)
    return ans

def getMiniDiff(root):
    def dfs(root):
        if not root:
            return []
        left = dfs(root.left)
        right = dfs(root.right)
        return left + [root.val] + right
    
    values = dfs(root)
    ans = float('inf')
    for i in range(1,len(values)):
        ans = min(ans,(values[i]-values[i-1]))
    return ans

def isValidBst(root):
    def dfs(node,small,large):
        if not node:
            return True

        if not (small < node.val < large):
            return False
        
        left = dfs(node.left,small,node.val)
        right = dfs(node.right,node.val,large)
        return left and right                   # tree is a bst if both left and right subtrees are bsts
    return dfs(root,float('-inf'),float('inf'))

def closestValue(root,target):
    def inorder(r):
        if not r:
            return []
        return inorder(r.left) + [r.val] + inorder(r.right)
    return min(inorder(root), key = lambda x: abs(target-x)) 