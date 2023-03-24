from collections import defaultdict, deque

def buildGraph(edges):
    d = defaultdict(list)
    for x,y in edges:
        d[x].append(y)
        #d[y].append(x) for undirected graphs
    return d

class Solution:

    #Find no. of connected components. Given adjacency matrix
    def findCircleNum(self,isConnected: list[list[int]])->int:
        
        def dfs(node):
            print('Node in Dfs ',node)
            print('G[node] in Dfs',graph[node])
            for neighbor in graph[node]:
                print('Neighbor in Dfs ',neighbor)
                # prevents cycles
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        #graph
        n = len(isConnected)
        print('Length ',n)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        print('Graph ',graph)
        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:
                ans += 1
                print('Ans ',ans)
                seen.add(i)
                print('Seen ',seen)
                dfs(i)
        return ans
    
    #find number of connected componenets
    # format of input graph is different
    def findNumIslands(self,grid:list[list[str]]) -> int:
        
        def valid(row,col):
            return 0<=row<m and 0<=col<n and (grid[row][col] == '1')        
        
        def dfs(row,col):
            print('DFS function call ',row,' ',col)
            for dx,dy in directions:
                print('for loop Dx ',dx,' Dy ',dy)
                next_row, next_col = row + dy, col + dx
                print('Next ',next_row,' ',next_col)
                if valid(next_row, next_col) and (next_row,next_col) not in seen:
                    print('Its valid')
                    seen.add((next_row, next_col))
                    dfs(next_row,next_col)
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        seen = set()
        ans = 0
        m = len(grid)
        n = len(grid[0])
        print('M ',m,'  N ',n)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1' and (row,col) not in seen:
                    ans+=1
                    print('Ans ',ans)
                    seen.add((row,col))
                    print('Seen ',seen)
                    dfs(row,col)
        return ans
    
    # connections is directed graph
    def minReorder(self, n:int, connections:list[list[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        #creating an undirected graph while maintaining the original input in roads set.
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y)) 

        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node,neighbor) in roads:
                        ans+=1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans
        seen = {0}      # basically, we're traversing away from 0. So if our edge, i.e, (node,neighbor) is in the original connection, then we need to swap its direction.
        return dfs(0)

    def keysAndRooms(self,rooms:list[list[int]]) -> bool:
        def dfs(node):
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        seen = {0}
        dfs(0)
        return len(rooms) == len(seen)

    # for a cyclic graph
    # same as nodes that cannot be reached from other nodes, i.e, indegree of node == 0
    def minNoOfNodesToReachAllNodes(self, n:int, edges:list[list[int]]) -> list[int]:
        indegree = [0]*n
        for _,y in edges:
            indegree[y] +=1
        
        return [node for node in range(n) if indegree[node]==0]

    # find if path exists in a graph
    def findPath(self, n:int, edges:list[list[int]], source:int, destination: int) -> bool:
        def dfs(node):
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
            return False

        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()
        return dfs(source)
    
    # find no. of connected components in an undirected graph
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        
        def dfs(node):
            print(graph[node])
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    print(neighbor)
                    dfs(neighbor)

        seen = set()
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        print('Graph ',graph)
        ans = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                ans+=1
        return ans
    
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
    
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]):
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = [False] * n
        for node in restricted:
            seen[node] = True
        self.ans = 0
        def dfs(node):
             seen[node] = True
             self.ans += 1
             for neighbor in graph[node]:
                 if not seen[neighbor]:
                    dfs(node)    
        dfs(0)
        return self.ans
    
    ## BFS and graphs ##

    # clear path - path from (0,0) to (n-1,n-1), can move 8-directionally 
    def shortestClearPathBinaryMatrix(self,grid: list[list[int]]) -> int :
        if grid[0][0] == 1:
            return -1
        
        def valid(row,col):
            return 0<=row<n and 0<=col<n and grid[row][col] == 0
        
        n = len(grid)
        seen = {(0,0)}
        queue = deque([(0,0,1)]) # r,c and steps
        directions = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        while queue:
            row, col, steps = queue.popleft()
            if (row,col) == (n-1,n-1):
                return steps
            
            for dx,dy in directions:
                next_r, next_c = row + dy, col + dx
                if valid(next_r, next_c) and (next_r,next_c) not in seen:
                    seen.add((next_r,next_c))
                    queue.append((next_r,next_c,steps+1))
        return -1


    # nodes at distance k from target node
    # logic - convert bt to undirected graph 
    def distanceK(self,root,target, k:int) -> list[int]:
        def dfs(node,parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left,node)
            dfs(node.right,node)
        
        dfs(root,None)
        queue = deque([target])
        seen = {target}
        distance = 0

        while queue and distance<k:
            curr_length = len(queue)
            for _ in range(curr_length):
                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return [node.val for node in queue]
    
    
    
    def updateMat(self, mat:list[list[int]]) -> list[list[int]]:

        def isValid(r,c):
            return 0<=r<n and 0<=c<n

        m = len(mat)
        n = len(mat[0])
        queue = deque()
        seen = set()

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row,col,1))
                    seen.add((row,col))
        
        directions = [ (0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                new_r, new_c = row + dy, col + dx
                if isValid(new_r,new_c) and (new_r,new_c) not in seen:
                    seen.add((new_r,new_c))
                    queue.append((new_r,new_c,steps+1))
                    mat[new_r,new_c] = steps
        return mat
    
    
    def shortestPathWithKObstacles(self, grid: list[list[int]], k:int) -> int:
        def valid(row,col):
            return 0<=row<m and 0<=col<n
        
        m = len(grid)
        n = len(grid[0])
        seen = {(0,0,k)}
        queue = deque([(0,0,k,0)]) # r,c, remain and steps
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            row, col, remain, steps = queue.popleft()
            if (row,col) == (m-1,n-1):
                return steps
            
            for dx,dy in directions:
                next_r, next_c = row + dy, col + dx
                if valid(next_r, next_c):
                    if grid[next_r,next_c] == 0:
                        if (next_r,next_c,remain) not in seen:
                            seen.add((next_r,next_c,remain))
                            queue.append(next_r,next_c,remain,steps+1)
                elif remain and (next_r,next_c,remain-1) not in seen:
                            seen.add((next_r,next_c,remain-1))
                            queue.append((next_r,next_c,remain-1,steps+1))
        return -1 

            
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        RED = 0
        BLUE = 1
        graph = defaultdict(lambda:defaultdict(list))
        for x,y in redEdges:
            graph[RED][x].append(y)
        for x,y in blueEdges:
            graph[BLUE][x].append(y)
        
        ans = [float('inf')]*n
        seen = {(0,RED),(0,BLUE)}
        queue = deque([(0,RED,0),(0,BLUE,0)])

        while queue:
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node],steps)
            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) not in seen:
                    seen.add((neighbor,1-color))
                    queue.append((neighbor,1-color,steps+1))
        
        return [x if x!=float('inf') else -1 for x in ans]

    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        
        def valid(row,col):
                return 0<=row<m and 0<=col<n
        
        m = len(maze)
        n = len(maze[0])
        seen = {(entrance[0],entrance[1])}
        queue = deque()
        queue.append([entrance[0],entrance[1],0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
        while queue:
            r,c,steps = queue.popleft()
            for dx, dy in directions:
                new_r, new_c = r + dy, c + dx
                if valid(new_r,new_c) and maze[new_r][new_c] == '.' and (new_r,new_c) not in seen:
                    if(new_r == 0 or new_r == m-1) or (new_c == 0 or new_c == n-1):
                        return steps + 1
                    seen.add((new_r,new_c))
                    queue.append([new_r,new_c,steps+1])
        return -1

   
    def openTheLock(self, deadends: list[str], target: str) -> int:
        
        def neighbors(node):
            ans = []
            for i in range(4):
                num = int(node[i])
                for change in [-1,1]:
                    x = (num+change)%10
                    ans.append(node[:i] + str(x) + node[i+1:])
            return ans

        if "0000" in deadends:
            return -1
        
        queue = deque([("0000",0)])
        seen = set(deadends)
        seen.add("0000")

        while queue:
            lock, steps = queue.popleft()
            if lock == target:
                return steps
            for neighbor in neighbors(lock):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor,steps+1))
        return -1

    

s = Solution()
g = s.openTheLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202")
print('Final ans ',g)
