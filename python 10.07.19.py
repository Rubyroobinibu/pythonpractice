#!/usr/bin/env python
# coding: utf-8

# In[3]:


lst=[1,2,3,4,5]
min(lst)
max(lst)
sum(lst)


# In[2]:


def add(a,b):
    return a+b
a,b=int(input("enter a")),int(input("enter b"))
print(add(a,b))
#reg arg print(add(a)) requires b


# In[3]:


def add(a,b):
    print("{}+{}={}".format(a,b,a+b))

add(10,34)


# In[4]:


def add(a,b):
    print("{}+{}={}".format(a,b,a+b))
#keyword arg
add(b=35,a=47)


# In[7]:


#default arg
def add(a,b=69):
    print("{}+{}={}".format(a,b,a+b))
add(10)
#add(10,99)


# In[10]:


#variable length arg
def add(*s):
    sum=0
    for n in s:
        sum+=n;
    print(sum)
add(3,4)
add(5,6,7)


# In[15]:


#**kwargs
def display(**data):
    for i,j in data.items():
        print("{} \t {}" .format(i,j))

display(roll=33,name="roobini",age=22)


# In[19]:


def func(a,b,c):
    print("a :{}" .format(a))
    print("b :{}" .format(b))
    print("c :{}" .format(c))
    
s=(1,2,3)
func(*s)

j={"a":1, "b":2 , "c":5}
func(**j)


# In[51]:


#lambda func
def lambdafun():
    pass
print(lambda x : x+3)
result= lambda x:x+3
print(result(86))


# In[41]:


def sq(lst):
    lst1=[]
    for i in lst:
        lst1.append(i**2)
    return lst1
lst=[1,2,3,4]
print(sq(lst))


# In[45]:


def oddno():
    odd=[]
    for i in range(1,1000):
        if(i%2!=0):
            odd.append(i)
    return(odd)
print(oddno())


# In[48]:


maxfunc=lambda a,b: a if(a>b) else b
print(maxfunc(20,30))


# In[47]:


def add(lst):
    return(sum(lst))
print(add([10,20,30,40,50]))


# In[59]:


cube=lambda x: pow(x,3)
print(cube(3))
#map func
# mapobj= map(cube, [1,2,3,4,5])
mapobj= map(cube, (1,2,3,4,5))
# print(list(mapobj))
print(tuple(mapobj))


# In[71]:


odd=lambda x: x%3
lst1=[]
for i in range(1,100):
    lst1.append(i)

filterobj=filter(odd,lst1)

print(list(filterobj))



# In[83]:


#file handling

fid=open('C://Users/Trainee/Desktop/python/pythonfile.txt','w')
fid.write("dsfsdfs")
fid.close()


# In[88]:


fid=open('C://Users/Trainee/Desktop/python/pythonfile.txt','r')
print(fid.read())
print(fid.tell())
print(fid.seek(3))
fid.close()


# In[95]:


fid=open('C://Users/Trainee/Desktop/python/pythonfile1.txt','w')
print(fid.write('a'*100))

fid.close()
fid=open('C://Users/Trainee/Desktop/python/pythonfile1.txt','r')
print(fid.read())

fid.close()
fid=open('C://Users/Trainee/Desktop/python/pythonfile1.txt','a')
print(fid.write("hello"))

fid.close()
fid=open('C://Users/Trainee/Desktop/python/pythonfile1.txt','r')
print(fid.read())

fid.close()


# In[102]:


with open('C://Users/Trainee/Desktop/python/pythonfile1.txt','a') as fileid:
    print(fileid.write('b'*30))
print(fileid.closed)
with open('C://Users/Trainee/Desktop/python/pythonfile1.txt','r') as fileid:
    print(fileid.read())


# In[2]:


import time
dir(time)


# In[3]:


import time
time.time()


# In[4]:


import time
time.localtime(time.time())


# In[10]:


import time
time.asctime(time.localtime(time.time()))


# In[14]:


import time
time.sleep(5)


# In[15]:


from datetime import datetime
datetime.now()


# In[23]:


from datetime import datetime
d=datetime.now()
d.strftime("%A") #full abbrev of day
d.strftime("%B") #full abbrev of current month
d.strftime("%b") #short form of current month
d.strftime("%p") #AM or PM
d.strftime("%d") #date


# In[25]:


import os
path=r"C:\Users\Trainee\Desktop\pyth"
os.mkdir(path)


# In[40]:


import os
path=r"C:\Users\Trainee\Desktop\pythonruby"
os.listdir()


# In[26]:


import math
dir(math)


# In[59]:


import math
math.sqrt(4)
math.pow(4,5)
math.fabs(10)
math.sin(45)
math.cos(40)


# In[31]:


import random
dir(random)


# In[63]:


import random
random.random()
random.randint(1,3) #includes endpoint
random.choice(['red', 'green','purple'])
random.randrange(1,5) #does not include endpoint


# In[71]:


import random
col=['yellow','red','green']
random.shuffle(col)
print(col)


# In[64]:


from functools import reduce
add=lambda a,b: a+b
sumobj=reduce(add, [10,40,50,60,70])
print(sumobj)


# In[91]:


from functools import reduce

lst=[2,1,11,9,5,7,6]
# maxfun=lambda a,b: max(a,b)
maxfun=lambda a,b: a if a>b else b

result=reduce(maxfun,lst)
print(result)


# In[104]:


i=int(input())
lst=[]
rep={}
for s in range(i):
    lst.append(input())
# print(lst)
for i in lst:
    if i in rep:
        rep[i]+=1
    else:
        rep[i]=1
print(len(rep))
k=[]
for i in rep.values():
    k.append(i)
print(k)

