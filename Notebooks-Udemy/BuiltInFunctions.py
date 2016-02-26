
# coding: utf-8

# In[1]:

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
    
temp = [0, 22.5, 40,100]


# In[2]:

map(fahrenheit, temp)


# In[3]:

map(celsius, map(fahrenheit, temp))


# In[6]:

f_temps = map(lambda x: (float(9)/5)*x + 32, temp)
f_temps


# In[10]:

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

map(lambda x,y,z:x+y+z,a,b,c)


# In[11]:

lst =[47,11,42,13]
reduce(lambda x,y: x+y,lst)


# In[12]:

from IPython.display import Image
Image('http://www.python-course.eu/images/reduce_diagram.png')


# In[21]:

#Find the maximum of a sequence (This already exists as max())
max_find = lambda a,b: a if(a > b) else b
#Find max
reduce(max_find,lst)


# In[22]:

#First let's make a function
def even_check(num):
    if num%2 ==0:
        return True
    
lst =range(20)

filter(even_check,lst)


# In[23]:

filter(lambda a: True if(a%2 == 0) else False, range(20))


# In[24]:

filter(lambda a: a%2 == 0, range(20))


# In[25]:

lst = ['a','b','c']

for number,item in enumerate(lst):
    print number
    print item


# In[26]:

for count,item in enumerate(lst):
    if count >= 2:
        break
    else:
        print item


# In[29]:

lst = [True,True,False,True]
#all(lst) 
any(lst)


# In[30]:

# Create 2+3j
complex(2,3)


# In[31]:

x = [1,2,3]
y = [4,5,6]

# Zip the lists together
zip(x,y)


# In[33]:

a = [1,2,3,4]
b = [5,6,7,8]

map(lambda x,y:(x,y),a,b)


# In[35]:

a = [1,2,3,4]
b = [5,6,7,8,9]

zip(a,b)


# In[36]:

d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

zip(d1,d2)


# In[37]:

zip(d2,d1.itervalues())


# In[39]:

def switcharoo(d1,d2):
    dout = {}
    
    for d1key,d2val in zip(d1,d2.itervalues()):
        dout[d1key] = d2val
    
    return dout

switcharoo(d1,d2)


# In[104]:

def word_lengths(phrase):    
    return list(map(len, phrase.split()))

print word_lengths('How long are the words in this phrase')


# In[107]:

def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y, digits)
print digits_to_num([3,4,3,2,1])


# In[82]:

def filter_words(word_list, letter):
    return filter(lambda s: s.startswith(letter), word_list)
l = ['hello' , 'are' , 'cat' , 'dog' , 'ham' , 'hi', 'go' , 'to' , 'heart']
filter_words(l, 'h')


# In[94]:

def concatenate(l1, l2, connector):
    return map(lambda (a,b): a+connector+b, zip(l1,l2)) 
concatenate(['A' , 'B'] , ['a' , 'b'] , '-')


# In[112]:

def d_list(L):
#    dic = {}
#    for number,item in enumerate(L):
#        dic[item]=number
#    return dic
    return {key:value for value,key in enumerate(L)}

d_list(['a' , 'b' , 'c' , 'd'])


# In[113]:

def count_match_index(L):
#    count=0
#    for number,item in enumerate(L):
#        if number==item:
#            count+=1
#    return count
    return len([num for count,num in enumerate(L) if num == count])
count_match_index([0,2,2,1,5,5,6,10])


# In[ ]:



