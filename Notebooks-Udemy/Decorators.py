
# coding: utf-8

# In[1]:

def func():
    return 1


# In[3]:

s = 'Global Variable'

def func():
    print locals()
func()


# In[7]:

s = 'Global Variable'

def func():
    print globals()
func()


# In[8]:

globals().keys()


# In[9]:

globals()['s']


# In[12]:

def hello(name='Jose'):
    return 'Hello '+name
hello()


# In[13]:

greet = hello


# In[14]:

greet


# In[15]:

greet()


# In[16]:

del hello


# In[17]:

hello()


# In[18]:

greet()


# In[19]:

def hello(name='Jose'):
    print 'The hello() function has been executed'
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    print greet()
    print welcome()
    print "Now we are back inside the hello() function"


# In[20]:

hello()


# In[21]:

welcome()


# In[22]:

def hello(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet
    else:
        return welcome


# In[25]:

x = hello()
x


# In[27]:

print x()


# In[33]:

def hello():
    return 'Hi Jose!'

def other(func):
    print 'Other code would go here'
    print func()
    
other(hello)


# In[31]:

def new_decorator(func):
    def wrap_func():
        print "Code would be here, before executing the func"
        func()
        print "Code here will execute after the func()"
    return wrap_func

def func_needs_decorator():
    print "This function is in need of a Decorator"
    
func_needs_decorator=new_decorator(func_needs_decorator)
func_needs_decorator()


# In[32]:

@new_decorator
def func_needs_decorator_annotation():
    print "This function is in need of a Decorator"
func_needs_decorator_annotation()


# In[ ]:



