__author__ = 'alakus'

print bin(1024)
print hex(1024)

print round(5.23222,2)

s = 'hello how are you Mary, are you feeling okay?'
print s.islower()

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print s.count('w')

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print set1.difference(set2)
print set1.union(set2)

d = {n:n**3 for n in range(5)}
print d

l = [1,2,3,4]
l.reverse()
print l

l = [3,4,2,5,1]
l.sort()
print l