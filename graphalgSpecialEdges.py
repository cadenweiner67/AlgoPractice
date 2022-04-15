from collections import defaultdict
  
  
class Graph:
    def __init__(self):  
        self.graph = defaultdict(list)
    def addEdge(self, u, v, EdgeType):
        self.graph[u].append((v,EdgeType))
    def bfs(self, s, t, M): 
        visited = [False] * (len(self.graph) + 1)
        
        queue = [] 
        queue.append(s)
        visited[s] = True
        
        while queue != []: 
            current = queue.pop(0) #pop first item to make a queue
            print(current, end=" ")
            for neighbour, EdgeType in self.graph[current]: 
                if visited[neighbour] == False and EdgeType == M: # if we haven't visited yet add to queue. Only looking for nodes along the edges of a special type otherwise don't treat it as an edge
                    queue.append(neighbour)
                    visited[neighbour] = True
                    if neighbour == t: 
                        return True
        print(t, " is unreachable from ", s, " along ", M, " type edges.")
        return False # if we reach this point without finding a connection to the target, it is unreachable





if __name__ == "__main__":       
    g = Graph()
    g.addEdge(0, 1, 't')
    g.addEdge(0, 2 ,'t')
    g.addEdge(1, 2, 'v')
    g.addEdge(2, 4, 't')
    g.addEdge(2, 3, 'v')
    g.addEdge(0, 1, 'v')
    g.addEdge(4, 2, 't')
    g.addEdge(3, 2, 'v')
    
    
    
    print("Following is DFS from (starting from vertex 2)")
    print("These two should be true.")
    print(g.bfs(0, 4, 't'))
    print(g.bfs(0, 3, 'v'))
    print("These two should be false.")
    print(g.bfs(0, 4, 'v'))
    print(g.bfs(0, 3, 't'))