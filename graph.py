#!/usr/bin/env python
# coding: utf-8

# In[3]:


#graphcoloring:

V=4
m=3

graph=[[0,1,1,1],
       [1,0,1,0],
       [1,1,0,1],
       [1,0,1,0]]

def issafe(v,color,c):
    for i in range(v):
        if graph[v][i]==1 and color[i]==c:
            return False
        
    return True    
        


def graphColorUtil(m,color,v):
    if v==V:
        return True
    
    for c in range(1,m+1):
        if issafe(v,color,c)==True:
            color[v]=c
            
            if graphColorUtil(m,color,v+1)==True:
                return True
            
            color[v]=0
            
    return False        


def graphColor(m):
    color = [0]*V
    
    if graphColorUtil(m,color,0)==False:
        return False
    
    for c in color:
        print(c)
    
    return True
        
graphColor(m)


# In[ ]:




