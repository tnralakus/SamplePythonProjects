
# coding: utf-8

# In[1]:

my_list = ['A string',23,100.232,'o']


# In[2]:

len(my_list)


# In[3]:

my_list[:3]


# In[4]:

my_list[3:]


# In[5]:

my_list[:]


# In[6]:

my_list + ['new item']


# In[7]:

my_list


# In[8]:

my_list = my_list + ['new_item']


# In[10]:

my_list


# In[11]:

my_list * 2


# In[12]:

# Create a new list
l = [1,2,3]


# In[13]:

# Append
l.append('append me!')


# In[14]:

l


# In[15]:

l.pop(0)


# In[16]:

l


# In[17]:

l.pop()


# In[18]:

l


# In[19]:

l[100]


# In[20]:

new_list = ['a','e','x','b','c']


# In[21]:

new_list.reverse()


# In[22]:

new_list


# In[23]:

new_list[::-1]


# In[24]:

new_list


# In[25]:

new_list=new_list[::-1]


# In[26]:

new_list


# In[27]:

new_list.sort()


# In[28]:

new_list


# In[29]:

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]


# In[31]:

matrix[0][0]


# In[32]:

first_col = [row[0] for row in matrix]


# In[33]:

first_col


# In[ ]:



