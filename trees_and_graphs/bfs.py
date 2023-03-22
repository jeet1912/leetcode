from collections import deque

def printAllNode(root):
    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        for _ in range(nodes_in_current_level):
            node = queue.popleft()
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def rightSideView(root):
    q = deque([root])
    ans = []
    while q:
        nodesInCL = len(q)
        ans.append(q[-1].val) # right-most element at curr Level
        for _ in range(nodesInCL):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

def findLargestInEachRow(root):
    q = deque([root])
    ans = []
   
    while q:
        nodesInCL = len(q)
        curr_max = float('-inf')
        for _ in range(nodesInCL):
            node = q.popleft()
            curr_max = max(curr_max,node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(curr_max) # max at each level
    return ans

def deepestLeavesSum(root):
    deepest_sum = depth = 0
    queue = deque([(root, 0),])

    while queue:
        node, curr_depth = queue.popleft()
        if node.left is None and node.right is None:
            # if this leaf is the deepest one seen so far
            if depth < curr_depth:
                deepest_sum = node.val      # start new sum
                depth = curr_depth          # note new depth
            # if there were already leaves at this depth
            elif depth == curr_depth:
                deepest_sum += node.val     # update existing sum    
        else:
            if node.left:
                queue.append((node.left, curr_depth + 1))
            if node.right:
                queue.append((node.right, curr_depth + 1))
                    
    return deepest_sum