#!/usr/bin/env python
# coding: utf-8

# In[2]:


no=int(input("enter a no"))
if no%2 == 0:
    print("%d is even " %no)
else:
    print("%d is odd " %no)


# In[ ]:


n=int(input("enter a no: "))
if n > 0:
    print("positive number")
elif n < 0:
    print("negative number")
else:
    print("equals to zero")


# In[25]:


def fibonacci(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(3,num+1):
        c=a+b
        print(c)
        a,b=b,c
        
n=int(input("Enter the limit"))
fibonacci(n)


# In[3]:


def sq(a,b=2):
    return a*a+b*b
x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
print(sq(x))


# In[11]:


l=int(input("enter limit"))
lst=[]
for i in range(l):
    lst.append(input())
def minfunc(lst):
    l=len(lst)
    
    for i in range(l):
        for j in range(l-i-1):
            if lst[j]>lst[j+1]:
                a=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=a
    return lst[0]
print(minfunc(lst))


# In[15]:


def avg(*args):
    l=len(args)
    sum=0
    for i in args:
        sum+=i
    return int(sum/l)


print(avg(1,2,3))
print(avg(1,2,3,4,5))


# In[21]:


import random
def randomfunc():
     return random.randint(1,10)

print(randomfunc())

# r=random.randint(1,10)
# print(r)


# In[28]:


def decfun(lst):
    l=len(lst)
    for i in range(l):
        for j in range(l-i-1):
            if lst[j]<lst[j+1]:
                a=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=a
    return lst
    
lst=[5,1,10,24,53,12,53]
print(decfun(lst))


# In[49]:


import math

def func(tup):
    res=lambda x: math.sqrt(x)
    mapobj=map(res,tup)    
    tup=tuple(mapobj)
    return list(tup)

tup=(1,2,3,4,5,6,7,8)
print(func(tup))


# In[48]:


odd=lambda x: x%3
lst1=[]
for i in range(1,50):
    lst1.append(i)

filterobj=filter(odd,lst1)

print(list(filterobj))

