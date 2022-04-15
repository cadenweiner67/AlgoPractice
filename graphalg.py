from collections import defaultdict
  
  
class Graph:
    def __init__(self):  
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def dfsutil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfsutil(neighbour, visited)
    def dfs(self, v):
        visited = set()
        self.dfsutil(v, visited)
    def bfs(self, s): 
        visited = [False] * (len(self.graph) + 1)
        
        queue = [] 
        queue.append(s)
        visited[s] = True
        
        while queue != []: 
            current = queue.pop(0) #pop first item to make a queue
            print(current, end=" ")
            for neighbour in self.graph[current]: 
                if visited[neighbour] == False: # if we haven't visited yet add to queue
                    queue.append(neighbour)
                    visited[neighbour] = True





if __name__ == "__main__":       
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print("Following is DFS from (starting from vertex 2)")
    g.dfs(2)
    g.bfs(2)

