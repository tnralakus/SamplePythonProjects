__author__ = 'alakus'

d = {'k1':1,'k2':2}

d = {x:x**2 for x in range(10)}
print d

for k in d.iterkeys():
    print k

for v in d.itervalues():
    print v

for item in d.iteritems():
    print item

print d.viewitems()
print d.viewkeys()
print d.viewvalues()