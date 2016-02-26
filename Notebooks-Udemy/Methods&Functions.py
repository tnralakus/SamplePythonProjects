
# coding: utf-8

# In[6]:

# Create a simple list
l = [1,2,3,4,5]


# In[5]:

l.append(6)
l


# In[7]:

# Check how many times 2 shows up in the list
l.count(2)


# In[10]:

help(l.insert)


# In[14]:

def say_hello(name):
    '''
        this is the simplest function
    '''
    print 'hello %s' %name


# In[15]:

say_hello('taner')


# In[16]:

def add_num(num1,num2):
    return num1+num2


# In[17]:

# Can also save as variable due to return
result = add_num(4,5)
result


# In[19]:

def is_prime(num):
    '''
    Naive method of checking for primes. 
    '''
    for i in range(2,num):
        if num % i == 0:
            print 'not prime'
            break
    else:
        print 'prime'


# In[22]:

is_prime(3)


# In[29]:

import math
num = 10
print math.sqrt(14) + 1 
range(3, int(math.sqrt(num)) + 1, 2)


# In[30]:

import math

def is_prime(num):
    '''
    Better method of checking for primes. 
    '''
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


# In[31]:

is_prime(14)


# In[36]:

def square(num): return num**2


# In[33]:

square(10)


# In[38]:

square = lambda num: num**2


# In[39]:

square(5)


# In[40]:

even = lambda num:num%2==0


# In[41]:

even(19)


# In[42]:

first = lambda s:s[0]


# In[43]:

first('taner')


# In[44]:

rev = lambda s:s[::-1]


# In[45]:

rev('taner')


# In[46]:

adder = lambda x,y:x+y


# In[47]:

adder(9,1)


# In[48]:

# x is local here:
f = lambda x:x**2


# In[49]:

name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print 'Hello '+name
    
    hello()

greet()


# In[53]:

x = 50

def func():
    global x
    print 'This function is now using the global x!'
    print 'Because of global x is: ', x
    x = 2
    print 'Ran func(), changed global x to', x

print 'Before calling func(), x is: ', x
func()
print 'Value of x (outside of func()) is: ', x


# In[55]:

# globals()
# locals()


# In[56]:

def vol(rad):
    return (4.0/3)*(3.14)*(rad**3)


# In[63]:

#Write a function that checks whether a number is in a given range (Inclusive of high and low)
def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):  
        print " %s is in the range" %str(num)  
    else :  
        print "The number is outside the range."


# In[62]:

def ran_bool(num,low,high):
    if num in range(low,high+1):
        return True
    return False
ran_bool(10, 4, 19)


# In[72]:

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def up_low(s):
    upper = 0
    lower = 0
    for c in s:
        if c.isupper(): upper += 1
        elif c.islower(): lower += 1
        else: pass
    print "String : %s"  %s
    print 'Upper count : ' , upper
    print 'Lower count : ' , lower
    
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# In[79]:

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
    # Also possible to use list(set())
    # return list(set(l))
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# In[82]:

# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    result = 1
    for num in numbers:
        result*=num
    return result
print multiply([1, 2, 3, -4])


# In[93]:

# Write a Python function that checks whether a passed string is palindrome or not.
def palindrome(s):
    s = s.replace(' ','')
    #r = rev(s)
    return s == s[::-1]
print palindrome('hell eh')


# In[96]:

# Write a Python function to check whether a string is pangram or not.
import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())  
    
print ispangram("The quick brown fox jumps over the lazy dog")


# In[95]:

string.ascii_lowercase


# In[ ]:



