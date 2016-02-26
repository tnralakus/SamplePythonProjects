
# coding: utf-8

# In[13]:

# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3
        
g=gencubes(10)
next(g)
next(g)
next(g)


# In[14]:

for x in gencubes(10):
    print x


# In[17]:

mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)


# In[11]:

#As we've noted in previous lectures (such as range()) many Standard Library functions that return lists in Python 2 
#have been modified to return generators in Python 3 because generators.


# In[18]:

def genfibon(n):
    '''
    Generate a fibonnaci sequence up to n
    '''
    a = 1
    b = 1
    for i in range(n):
        yield str(a)+'taner'
        a,b = b,a+b


# In[20]:

for num in genfibon(10):
    print num


# In[3]:

def simple_gen():
    for x in range(3):
        yield x


# In[4]:

# Assign simple_gen 
g = simple_gen()


# In[5]:

while True:
    try:
        print next(g)
    except StopIteration:
        print 'StopIteration'   
        break
    else:
        print 'DONE'


# In[6]:

print next(g)


# In[9]:

s = 'hello'

#Iterate over string
for let in s:
    print let
s_iter=iter(s)
next(s_iter)


# In[34]:

def gensquares(N):
    for i in range(N):
        yield i**2
for x in gensquares(10):
    print x


# In[35]:

import random

def rand_num(low,high,n):
    while n>0:
        yield random.randint(low,high)
        n = n -1
for num in rand_num(1,10,12):
    print num


# In[39]:

s = 'hello'

#code here
s_iter=iter(s)
print next(s_iter)


# In[ ]:



