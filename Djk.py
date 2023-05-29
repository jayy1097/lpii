#!/usr/bin/env python
# coding: utf-8

# In[2]:


import heapq
INF = 999999
graph = {
    'A': {'B': 1},
    'B': {'A': 1, 'C': 2, 'D': 3},
    'C': {'B': 2, 'D': 1, 'E': 5},
    'D': {'B': 3, 'C': 1, 'E': 1},
    'E': {'C': 5, 'D': 1}
}
def DJK(graph,source):
    Q = set()
    dist = {}
    for vertex in graph:
        dist[vertex]=INF
        Q.add(vertex)
    dist[source]=0
    
    while(Q):
        u = min(Q,key=lambda v:dist[v])
        Q.remove(u)
        
        for v in graph[u]:
            cost_uv = graph[u][v]
            if dist[u]+cost_uv < dist[v]:
                dist[v] = dist[u]+cost_uv
    return dist
source_node = 'A'
sd = DJK(graph,source_node)
for node in sd:
    d = sd[node]
    print("Shortest Distance from",source_node,"to",node,":",d)


# In[ ]:





# In[ ]:




