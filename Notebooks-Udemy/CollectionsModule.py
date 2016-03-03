import collections

__author__ = 'alakus'

#Counter
from collections import Counter

print Counter([1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1])
print Counter('aabsbsbsbhshhbbsbs')

s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
print Counter(words)
# Methods with Counter()
c = Counter(words)
print c.most_common(2)
print c.values()
print sum(c.values())
print c.keys()
print c.items()
set(c)
list(c)
dict(c)
#print c.clear()
#print c


#defaultdict
from collections import defaultdict
d = defaultdict(object)
d['one']
for item in d:
    print item

try:
    e = {}
    e['one']
except:
    print 'dict problem'

f = defaultdict(lambda:0)
f['one']
print(f['one'])

#OrderedDict

print 'Normal dictionary:'
d={}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k,v in d.items():
    print k, v

print 'OrderedDict:'

from collections import OrderedDict

d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

print 'Dictionaries are equal? '

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

print 'Dictionaries are equal? '

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'

d2 = collections.OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

from collections import namedtuple

Dog = namedtuple('Dog','age breed name')

sam = Dog(age=2,breed='Lab',name='Sammy')
frank = Dog(age=2,breed='Shepard',name="Frankie")
print sam
print sam.age
print sam[1]