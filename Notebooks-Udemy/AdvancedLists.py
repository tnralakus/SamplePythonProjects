__author__ = 'alakus'

l = [1,2,3]

l.append(4)
print l

print l.count(10)

x = [1, 2, 3]
x.append([4, 5])
print x

x = [1, 2, 3]
x.extend([4, 5])
print x

print l.index(2)
#print l.index(12)

# Place a letter at the index 2
l.insert(2,'inserted')
print l

print l
ele = l.pop()
print l
print ele

l.remove('inserted')
print l

l.reverse()
print l

l.sort()
print l