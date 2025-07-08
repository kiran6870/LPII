
def prims(graph,start_node):
    mst=[]
    visited=set([start_node])
    total_cost=0
    edges=[]
    for neighbor,weight in graph[start_node]:
        edges.append((weight,start_node,neighbor))
    
    while edges:
        edges.sort()
        weight,parent,node=edges.pop(0)
        if node not in visited:
            visited.add(node)
            total_cost+=weight
            mst.append((parent,node,weight))
            for neighbor,edge_weight in graph[node]:
                edges.append((edge_weight,node,neighbor))
    return total_cost,mst

graph={}
n=int(input("entre the no of edges:"))
for i in range(n):
    u,v,w=input('enter (node1,node2,weight):').split()
    W=int(w)
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[]
    graph[u].append((v,W))
    graph[v].append((u,W))
start_node=input("enter the start node:")
TOTAL_COST,MST=prims(graph,start_node)
print('Mininmum spanning tree:',MST)
print('Total cost:',TOTAL_COST)
