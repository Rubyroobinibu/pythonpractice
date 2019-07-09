#!/usr/bin/env python
# coding: utf-8

# In[18]:


emp={"name":"jjj","age":22}
print(emp.get('name'))
emp['age']
for key in emp.keys():
    print(emp[key])
for key,value in emp.items():
    print(key,value)
print(len(emp))
del emp['name']
print (emp)
emp.popitem()
print(emp)


# In[19]:


def ipsplitter(s):
    return s.split(".")
print(ipsplitter("10.231.1.12"))


# In[20]:


def fruitsplitter(s):
    return s.split("#")
print(fruitsplitter("apple#orange#grapes#banana"))


# In[21]:


def fn(no):
    return no[:2]+"-"+no[2:]
print(fn("919876598764"))


# In[22]:


def fn(no):
    return no[3:]
print(fn("91-9876598764"))


# In[23]:


def fn(no):
    return no[:2]+no[3:]
print(fn("91-9876598764"))


# In[24]:


def fnspace(s):
    return s[:5]+s[6:]
print(fnspace("Hello World"))


# In[25]:


s="Hello World"
s.replace(" ","")


# In[26]:


def fn(str):
     return str.replace(" ","")
print(fn("1800 123 4567"))


# In[27]:


def fn(str):
     return str.split(".")
print(fn("10.232.23.34"))


# In[28]:


str="192.165.34.1"
j=0
i=str.split(".")
print(i)
for x in i:

    if int(x) < 256:
        j+=1
if j==4:
    print("valid")
else:
     print("invalid")


# In[29]:


lst=['aaa','dfd','a','lll']
len(lst)
lst.append('gg')
len(lst)


# In[30]:


lst=['aaa','dfd','a','lll','a']
len(lst)
lst1=lst.copy()
print(lst1)
# lst.clear()
# lst=[]
print(lst[2])
lst.index('lll')


# In[31]:


colors={'purple','yellow','blue'}
print(colors)
for i in colors:
      print(i)
# colors.update('pink','lavender')
# print(colors)
colors.update(['pink','lavender'])
print(colors)
# colors.remove('white')  #throws error
colors.discard('white') #does not throw error


# In[32]:


#type conversion
str1='10'
type(str1)
print(int(str1))


# In[33]:


ord('a')
hex(10)
oct(10)
chr(98)


# In[34]:


tuple(['a','b'])
list(('a','b'))
set(['a','b','c'])
dict((('id', 100),('name','aaaa')))


# In[35]:


tup=('a','b','c')
list(tup)


# In[36]:


tup=(('aaa','vvv'),(1,2))
dict(tup)


# In[37]:


str1='1010'
print(int(str1,2))


# In[40]:


#if-else

num=int(input("Enter a number"))
if num%2==0:
    print("%d is even" %(num))
else:
    print("{} is odd" .format(num))


# In[41]:


#elif

num=int(input("enter a number"))
if(num > 100):
    print("%d is greater than 100" %(num))
elif(num < 100):
    print("%d is less than 100" %(num))
else:
    print("%d is equal to 100" %(num))
    


# In[51]:


a=int('10')
b=int('20')
if a<b: print(a)
print(a) if a<b else print(b)


# In[56]:


a=int('30')
b=int('40')
c=int('50')
d=int('50')
print(a) if a>b  else print(b) if c!=d else print(d)


# In[66]:


#for

i=(10,20,30)
for j in i: 
    print(j)
    if(j==20): break


# In[70]:



for i in range(12):
    print()
    for j in range(i):
        print(j, end=' ')


# In[72]:



for i in range(1,10):
    print()
    for j in range(i):
        print("*", end=' ')


# In[74]:


for value in range(5):
    print(value)
else:
    print(".......")


# In[76]:


i=1
j=20
k= int(input("enter the number to be multiplied"))
while(i<=j):
    print("{} * {}   = {}" .format(k,i,k*i))
    i+=1


# In[83]:



j=20
k=int(input("enter a number"))
for x in range(1,j+1,3):
    print("{}*{}={}". format(k,x,k*x))


# In[84]:


i=1
j=20

k= int(input("enter the number to be multiplied"))
print()
while(i<=j):
    print("{} * {}   = {}" .format(k,i,k*i))
    i+=1
else:
      print("...................................")


# In[3]:


#pass
for i in range(1,10):
    if (i==7): 
        pass
        print("....")
    print(i)


# In[23]:


lst1=[10, ['user1','user2'],10.25,('test1','test2'), True, None]
flatlst=[]

for elem in lst1:
   
    if type(elem) == list:
        for e in elem:
            flatlst.append(e)
    elif type(elem) == tuple:
        for e in elem:
            flatlst.append(e)
    else:
        flatlst.append(elem)
#         else: 
#             flatlst.append(elem)
print(flatlst)


# In[36]:


for x in range(6,0,-1):
    print()
    for y in range(1,x):
        print("*",end=' ')
        i-=1

        
        
        
        


# In[44]:


size=5
for i in range(0,size+1):
    print()
    for j in range(0,size-i):
        print(" ",end="")
    for k in range(0,i):
        print("*",end=" ")


# In[45]:


size=5
for i in range(0,size+1):
    print()
    for j in range(0,size-i):
        print("*",end="")
    for k in range(0,i):
        print(" ",end=" ")
    for j in range(0,size-i):
        print("*",end="")


# In[47]:


for i in range(1,5):
    str1="* "*i
    print(str1.center(10))


# In[ ]:


movies=["The Holy Grail","The Life of Brain","The Meaning of Life"]
years=[1975,1979,1983]
result=[]
for (movie,year) in zip(movies,years):
    result.append(movie)
    result.append(year)
print(result)


# In[ ]:


import random
random.randint(1,54)


# In[ ]:


import random
i=random.randint(1,10)
c=0
for x in range(0,6):
   j=int(input("enter a number"))
   if j>i: 
         print("guess is too high")
   elif j<i:
           print("guess is too low")
   else:
           print("guessed right")
#     c+=1
#     if(c==5):
#         print("you won")
#     else: 
#         print("you lost")


# In[4]:


import random
i=random.randint(1,10)
c=0
for x in range(0,6):
    j=int(input("enter a number"))
    if j>i: 
          print("guess is too high")
    elif j<i:
            print("guess is too low")
    else:
            print("guessed right")
            break;
c+=1
if(c==5):
    print("out")
    


# In[12]:


year=int(input("enter a year"))
if (year%400==0 or (year%4==0 and year%100!=0)):
    print("{} is a leap year" .format(year))
else:
    print("{} is not a leap year".format(year))


# In[ ]:





# In[ ]:





# In[ ]:




