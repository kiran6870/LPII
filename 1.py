from collections import deque

class Graph:

    graph={}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self,start):
        visited=set()
        stack=[start]
        while stack:
            node=stack.pop()
            if node not in visited:
                visited.add(node)
                print(node,end=" ")
                for neighbour in reversed(self.graph[node]):
                    if neighbour not in visited:
                        stack.append(neighbour)
    
    def bfs(self,start):
        visited=set()
        queue=deque([start])
        visited.add(start)
        while queue:
            vertex=queue.popleft()
            print(vertex,end=" ")
            for i in self.graph[vertex]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
    
gr=Graph()
root=input("enter the root node:")
gr.graph[root]=[]

num_nodes=int(input("enter the no of nodes(including the root):"))
print("now enters the node and its child node")

for i in range(num_nodes-1):
    node=input("enter the node:")
    ans='y'
    while ans=='y':
        print("child node present or not (y or n):")
        ans=input()
        if(ans=='n'):
            break
        child=input('enter the child node:')
        gr.add_edge(node,child)

print("\n graph(Adjancency matrix):")
print(gr.graph)
start_node=input('\n enter the starting node:')
print('DFS')
print(gr.dfs(start_node))
print("\n BFS:")
print(gr.bfs(start_node))