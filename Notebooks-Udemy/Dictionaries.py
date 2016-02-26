
# coding: utf-8

# In[1]:

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}
# Call values by their key
my_dict['key2']


# In[4]:

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
#Lets call items from the dictionary
my_dict['key3'][0].upper()


# In[8]:

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123
my_dict['key1']


# In[9]:

my_dict


# In[15]:

# Set the object equal to itself minus 123 
my_dict['key1'] += 123
my_dict['key1']


# In[16]:

# Create a new dictionary
d = {}
# Create a new key through assignment
d['animal'] = 'Dog'
# Can do this with any object
d['answer'] = 42
#Show
d


# In[18]:

# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
d['key1']['nestkey']['subnestkey']


# In[21]:

# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}


# In[22]:

d.keys()


# In[23]:

d.values()


# In[24]:

d.items()


# In[26]:

mymap = {1:2,2:3,3:4}


# In[28]:

mymap[mymap[mymap[1]]]


# In[29]:

mylist=[1,2,3,4,5,6]
mymap[mylist[1]]


# In[36]:

mylist[1:]
mylist[0:]


# In[ ]:



