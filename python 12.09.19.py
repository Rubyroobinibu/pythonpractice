#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
str1='hello world'
matches=re.search(r'o',str1)
print(matches.group(0))

pattern=re.compile(r'o')
matches=pattern.finditer(str1)
for i in matches:
    print(i.group(0),end=' ')


# In[34]:


fid=open(r'C://Users/Trainee/Desktop/pythonruby/file1.txt','a')
print(fid.write("skfjsdkf"))
fid.close()


# In[35]:


fid=open(r'C://Users/Trainee/Desktop/pythonruby/file1.txt','r')
print(fid.read())
fid.close()


# In[36]:


with open(r'C://Users/Trainee/Desktop/pythonruby/file1.txt') as f:
    with open(r'C://Users/Trainee/Desktop/pythonruby/file2.txt', "w") as f1:
        for line in f:
            f1.write(line)
    


# In[39]:


n=int('2')
if n==2:
    print("dsfd")
elif n==3:
    print("dfsffdsfd")
    


# In[1]:


import re
str1='email ID:call.del@airindia.in'
domain = re.search(r'\w+\.\w+@\w+.\w+', str1)
# domain = re.search(r'\S+\s+\S+@\S+', str1)
print(domain.group(0))


# \w+\.\w+@\w+\.\w+
# \S+@\S+


# In[41]:


str1='Landline Number : 011-24667473'
str2='Landline Number : 011.24667473'
str3='Landline Number : 011*24667473'
# match=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str1)
# match1=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str2)
# match2=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str3)
match4=re.search(r' \d{3}[-|.|*]\d{8}',str1)
match5=re.search(r' \d{3}[-.*]\d{8}',str2)
match6=re.search(r' \d{3}[-.*]\d{8}',str3)
# print(match)
# print(match1)
# print(match2)
print(match4)
print(match5)
print(match6)


# In[ ]:


lst=[5,6,7,8,9]
# print(lst)
try:
    num1=int(input("enter first num:"))
    num2=int(input("enter second num:"))
    print(num1/num2)
    print(lst)
except ValueError as er:
    print("enter number\n")
    print("Error \n{}".format(er))
    
except ZeroDivisionError as err:
    print("divisor should be greater than 0\n")
    print("Error \n{}".format(err)) # to print system generated error msg
    


# In[7]:


import sys
sys.maxsize


# In[ ]:


lst=[5,6,7,8,9]
# print(lst)
try:
    num1=int(input("enter first num:"))
    num2=int(input("enter second num:"))
    print(num1/num2)
    print(lst[6])
    
except ValueError as er:
    print("enter number\n")
    print("Error \n{}".format(er))
    
except ZeroDivisionError as err:
    print("divisor should be greater than 0\n")
#     print("Error \n{}".format(err)) # to print system generated error msg
    print(err)
    
except Exception as err:
    print(err)
    


# In[6]:



try:
    num1=int(input("enter first num:"))
    num2=int(input("enter second num:"))
    if num2==0:
        raise ZeroDivisionError
    print(num1/num2)
    
    
except ValueError:
    print("enter number\n")

    
except ZeroDivisionError:
    print("divisor should be greater than 0\n")
#     print("Error \n{}".format(err)) # to print system generated error msg
#     print(err)
    
except Exception as err:
    print(err)
    


# In[8]:


try:
    num1=int(input("enter first num:"))
    num2=int(input("enter second num:"))
    
    
except ValueError as er:
    print("enter number\n")
    print("Error \n{}".format(er))
    
else:
    print("division is %d" %(num1/num2))


# In[ ]:


try:
    num1=int(input("enter first num:"))
    num2=int(input("enter second num:"))
    
    
except ValueError as er:
    print("enter number\n")
    print("Error \n{}".format(er))
    
else:
    print("division is %d" %(num1/num2))
    
finally:
    num1=0
    num2=0
    print(num1,num2)


# In[5]:


lst=[5,6,7,8,9]
try:
    num1=int(input("enter first num:"))
    num2=int(input("enter second num:"))
    if num2==0:
        raise ZeroDivisionError
    print(num1/num2)
    print(lst[10])
    
except (ValueError,ZeroDivisionError) as err:
#     print("enter number\n")
    print("error")

    

    


# In[13]:


import string
import random

def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    return ''.join(random.choice(chars) for x in range(8))

print(randompassword())


# In[14]:


import secrets
import string
import random

def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    return ''.join(secrets.choice(chars) for x in range(8))

print(randompassword())


# In[15]:


for x in range(6,0,-1):
    print()
    for y in range(1,x):
        print("*",end=' ')
       


# In[17]:


import re
str1='https://youtube.com'
str2='https://python.org'
match1=re.search(r'[a-z]+://[a-z]+.[a-z]+',str1)
match2=re.search(r'[a-z]+://[a-z]+.[a-z]+',str2)
print(match1.group(0))
print(match2.group(0))


# In[42]:


import re
str1='https://youtube.com'
str2='http://yahoo.co.in'
match1=re.search(r'[a-z]+://[a-z]+.[a-z]+.[a-z]+',str1)
match2=re.search(r'[a-z]+://[a-z]+.[a-z]+.[a-z]+',str2)
# match1=re.search(r'\S+',str1)
# match2=re.search(r'\S+',str2)
# match1=re.search(r'\w+://\w+.\w+.\w+',str1)
print(match1.group(0))
print(match2.group(0))


# In[43]:


ph1 = '234-456-1234'
ph2 = '123.456.1234'
match1=re.search(r'\d+[-.]\d+[-.]\d+',ph1)
match2=re.search(r'\d+[-.]\d+[-.]\d+',ph2)
print(match1.group(0))
print(match2.group(0))


# In[45]:


ph = '+91 987 180 3333'
match=re.search(r'\+\d\d\s(\d{1,3}\s\d{1,3}\s\d{1,4})',ph)
print(match.group(1))


# In[46]:


name1 = 'Mr. Ram'
name2 = 'Mr John'
match1=re.search(r'[a-zA-Z. ]+',name1)
match2=re.search(r'[a-zA-Z. ]+',name2)
print(match1.group(0))
print(match2.group(0))


# In[47]:


date1 = '21/10/2019'
match=re.search(r'\d{1,2}/\d{1,2}/\d{1,4}',date1)
print(match.group(0))


# In[60]:


class Student:
    name="Sam"
    age=10
    
    def displayName(self):
        return self.name
        
stud=Student()
stu=Student()
print(stud.name)
print(stud.age)
print(stud.displayName())
print(stud)
print(stu)


# In[79]:


#parameterised constructor

class Student:
    school='lgms'
    def __init__(self,roll,name):   #constructor--> __init__
        self.roll=roll
        self.name=name

s1=Student(1,'dsfds')
s2=Student(2,'aaaa')
print(s1.roll,s1.name,s1.school)
print(s2.roll,s2.name,Student.school)  # common var can be accessed by classname or instance but private var are accessed only by obj
print(s1.__dict__)
print(s2.__dict__)

del s1.name
print(s1.__dict__)


# In[67]:


#non parameterised constructor

class Student:
    def __init__(self):
        print("Non parameterised constructor")
        
s=Student()


# In[92]:


class Employee:
    dept='lgms'
    def __init__(self,firstname,lastname):   #constructor--> __init__
        self.firstname=firstname
        self.lastname=lastname
        self.password=firstname+"123"+lastname+"@gmail.com"    
    

e1=Employee('ruby','roobini')
e2=Employee('aaa','bbb')
print(e1.firstname,e1.lastname,e1.dept,e1.password)
print(e2.firstname,e2.lastname,e2.dept,e2.password)


# In[1]:


import re
l=int(input())
lst=[]
for i in range(l):
    lst.append(input())
for j in lst:
    match=re.search(r'[4-6]{0,1}[0-9\-]{0,4}[0-9\-]{0,6}[0-9\-]{0,6}[0-9\-]{0,6}',j)
#     match=re.search(r'[4-6\-])
    print(match.group(0))


# In[2]:


import re
credit=input("Enter your credit card number")
match=re.search(r'[4-6]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',credit)
if(match):
    l=len(credit)
    for i in range(0,l-3,1):
        flag=0
        for j in range(i+1,l,1):
            if credit[i]==credit[j]:
                flag+=1
        if flag>=4:
           print("Invalid")
           break
        break
    print("valid")    
else:
    print("Invalid")

