#!/usr/bin/env python
# coding: utf-8

# In[11]:


i=int(input("enter the size"))
lst=[]

for x in range(i):
    lst.append(int(input(x)))
for x in range(i):
    for y in range(i-x-1):
        if lst[y]>lst[y+1]:
            l=lst[y]
            lst[y]=lst[y+1]
            lst[y+1]=l
            

print(lst)
            
           

