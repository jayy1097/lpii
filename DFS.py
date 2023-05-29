#!/usr/bin/env python
# coding: utf-8

# In[3]:


graph = {
    'A' : ['B' , 'C'],
    'B' : ['D' , 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
}

visited = []

def DFS(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                DFS(visited,graph,neighbour)

DFS(visited,graph,'A')


# In[43]:




