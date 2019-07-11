#!/usr/bin/env python
# coding: utf-8

# In[2]:


def dup(lst):
    print(set(lst))
lst=[]
for i in range(1,6):
    l=int(input())
    lst.append(l)
dup(lst)


# In[29]:


def f(n):
    a=0
    b=1
    
    print(a)
    print(b)
    for x in range(1,n-1):
        c=a+b
        print(c)
        a=b
        b=c
n=int(input())
f(n)


# In[14]:


import re
s="hello world"
match=re.match("hello",s)
print(match)  #returns match only if match is present in the beginning of the string


# In[15]:


import re
s="hello world"
match=re.match("world",s)
print(match)  #returns match only if match is present in the beginning of the string


# In[17]:


import re
s="hello world"
match=re.search("world",s)
print(match)  #returns match only if match is present anywhere in the string


# In[22]:


import re
s="hello world"
match=re.search("wor",s)
print(match) #returns match only if match is present anywhere in the string
print(match.span()) #returns span value of searched string
print(match.string) #returns the entire string
print(match.group(0)) #returns the searched string


# In[4]:


def palindrome(s):
    rev=s[::-1]
    if s==rev:
        return 1
    else:
        return 0

s=input()
result=palindrome(s)
if result==1:
    print("{} is a palindrome".format(s))
else:
    print("{} is not a palindrome".format(s))


# In[25]:


import re
s="hello wor ld"
match=re.findall(" ",s)
print(match)  #returns match only if match is present anywhere in the string


# In[28]:


import re
s="hello world"
match=re.split("o",s)
print(match)  #returns match only if match is present anywhere in the string


# In[30]:


import re
s="hello world"
match=re.sub("o","#",s)
print(match)  #returns match only if match is present anywhere in the string


# In[60]:


import re
s="\nhello world"
match=re.search(r'\w',s)
print(match)  #returns starting word character in the string


# In[48]:


import re
s="hel lo world"
match=re.search(r'\W',s)
print(match)  #returns white space character in the string


# In[42]:


import re
s="h1llo world"
match=re.search(r'\d',s)
print(match)  #returns digits in the string


# In[41]:


import re
s="1ello world"
match=re.search(r'\D',s)
print(match)  #returns other than digits character in the string


# In[44]:


import re
s="hello\tworld"
print(s)
match=re.search(r'\s',s)
print(match)  #returns white space,tab space character in the string


# In[47]:


import re
s="hello\nworld"
print(s)
match=re.search(r'\s',s)
print(match)  #returns white space character in the string


# In[54]:


import re
s=" hello\nworld"
print(s)
match=re.search(r'\S',s)
print(match)  #returns other than space, tab, newline character in the string


# In[59]:


import re
s="\n1elloworld"
print(s)
match=re.search(r'.',s)
print(match)  #returns any char other than new line in the string


# In[69]:


ip='192.174.32.1'
match=re.search(r'(\d\d\d)\.(\d\d\d).(\d\d).(\d)',ip)   # \. is used to skip ''.''
print(match)
print("the ip is {}" .format(match.group(0))) #returns entire string
print("the ip is {}" .format(match.group(1))) #returns first group of string
print("the ip is {}" .format(match.group(2))) #sec group
print("the ip is {}" .format(match.group(3))) #third
print("the ip is {}" .format(match.group(4))) #4th


# In[71]:


ip='192.174.342.11'
match=re.search(r'(\d\d\d)\.(\d\d\d).(\d\d).(\d)',ip)   # pattern mismatch
print(match)


# In[75]:


ip='192.174.32.1'
ip2='156.45.3.2'
match=re.search(r'(\d+)\.(\d+).(\d+).(\d+)',ip2)   # \d+ is used for more than one number in each octet
print(match)
print(match.group(0))


# In[121]:


ip='192.174.32.123'
match=re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip)   # \d+ is used for more than one number in each octet
print(match)


# In[144]:


ip='fe80::80c9:5d7a:b500:2312%24'
match=re.search(r'[a-fA-F0-9]{0,4}::[a-fA-F0-9]{0,4}:[a-fA-F0-9]{0,4}:[a-fA-F0-9]{0,4}:[a-fA-F0-9]{0,4}%\d\d',ip)   # \d+ is used for more than one number in each octet
print(match)


# In[186]:


str1='email ID:call.del@airindia.in'
domain = re.search("@[\w.]+", str1)
print(domain)




# In[188]:


str1='email Id : call.del@airindia.in'
match=re.search(r'[a-zA-Z ]+:([a-z ]+\.[a-z]+@([a-z]+\.[a-z]+))',str1)
print(match)
# print(match.group(0))
# print(match.group(1))
print(match.group(2))


# In[190]:


str1='Landline Number : 011-24667473'
match=re.search(r'[a-zA-Z ]: ([0-9]{1,3})-([0-9]{8})',str1)
print(match)
print(match.group(0))
print(match.group(1))
print(match.group(2))


# In[183]:


str1='(Monday to Saturday,0930 hrs. - 1730 hrs. IST)'
match=re.search(r'[a-zA-Z \(]+,([a-z0-9. -]+)[A-Z\)]+',str1)
print(match)
print(match.group(0))
print(match.group(1))


# In[184]:


str1='Landline Number : 011-24667473'
str2='Landline Number : 011.24667473'
str3='Landline Number : 011*24667473'
match=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str1)
match1=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str2)
match2=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str3)
print(match)
print(match1)
print(match2)


# In[196]:


import re 
for _ in range(int(input())): line = input()

while ' && ' in line or ' || ' in line:
    line = line.replace(" && ", " and ").replace(" || ", " or ")

print(line)

