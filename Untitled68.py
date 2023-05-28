#!/usr/bin/env python
# coding: utf-8

# In[108]:


graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}


# In[109]:


visited = []
queue = []


# In[110]:


def BFS(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s,end=" ")
        for neighbour in graph[s]:
                if neighbour not in queue:
                    visited.append(neighbour)
                    queue.append(neighbour)
            


# In[111]:


BFS(visited,graph,'A')


# In[ ]:





# In[ ]:




