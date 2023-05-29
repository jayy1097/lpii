#!/usr/bin/env python
# coding: utf-8

# In[28]:


def SS(array,size):
    for ind in range(size):
        minimum_index = ind
        for j in range(ind+1,size):
            if array[minimum_index] > array[j]:
                minimum_index = j
        (array[minimum_index],array[ind]) = (array[ind],array[minimum_index])
    return array

array = [-9,17,35,-4,5]
size = len(array)
print("Array before sorting" , array )
print("Array after sorting" , SS(array,size))


# In[ ]:




