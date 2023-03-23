from collections import defaultdict

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


s = Solution()
g = s.maxAreaOfIsland(grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print('Final ans ',g)