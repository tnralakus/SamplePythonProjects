
# coding: utf-8

# In[5]:

x = True
if x:
    print 'It was True'
else:
    print 'It was false'


# In[11]:

person = 'George'

if person == 'Sammy':
    print 'Welcome Sammy!'
elif person =='George':
    print "Welcome George!"
else:
      print "Welcome, what's your name?" 


# In[18]:

l = [1,2,3,4,5,6,7,8,9,10]
for num in l:
    if num % 2 == 0:
        print num
    else:
        print 'odd number'


# In[19]:

sum = 0
for num in l:
    sum += num
print sum


# In[20]:

for letter in 'this is a message':
    print letter


# In[21]:

tup = (1,2,3,4,5)

for t in tup:
    print t


# In[22]:

l = [(2,4),(6,8),(10,12)]
for t in l:
    print t
for (t1,t2) in l:
    print t1


# In[23]:

d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print item


# In[24]:

# Create a generator
for k,v in d.iteritems():
    print k
    print v  


# In[26]:

# Create a generator
for a in d.iteritems():
    print a  


# In[27]:

# For Python 3
for k,v in d.items():
    print k
    print v  


# In[29]:

x = 0

while x < 10:
    print 'x is currently: ',x
    print ' x is still less than 10, adding 1 to x'
    x+=1
else:
    print 'done'


# In[31]:

x = 0
while x < 10:
    print 'x is currently: ',x
    print ' x is still less than 10, adding 1 to x'
    x+=1
    if x ==3:
        print 'x==3'
    elif x==6:
        print 'it is 6!!!'
        break
    else:
        print 'continuing...'
        continue


# In[32]:

range(0,10)


# In[34]:

t=range(0,10)
type(t)


# In[35]:

t


# In[36]:

for num in xrange(10):
    print num


# In[37]:

# Grab every letter in string
lst = [x for x in 'word']


# In[38]:

lst


# In[42]:

num_lst = [x**2 for x in range(1,10)]
num_lst


# In[40]:

num_lst


# In[44]:

num_lst = [x for x in range(10) if x % 2 == 0]
num_lst


# In[45]:

lst = [ x**2 for x in [x**2 for x in range(11)]]
lst


# In[47]:

st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print word


# In[51]:

# Use range() to print all the even numbers from 0 to 10.
ls = [l for l in range(10) if l % 2 == 0]
ls


# In[54]:

range(0,10,2)


# In[56]:

# Use List comprehension to create a list of all numbers between 1 and 50 that are divisble by 3.
ls = [l for l in range(50) if l % 3 == 0]
ls


# In[57]:

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print word


# In[58]:

st = 'Create a list of the first letters of every word in this string'
l = [s[0] for s in st.split()]
l


# In[59]:

for num in xrange(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print "FizzBuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num


# In[ ]:



