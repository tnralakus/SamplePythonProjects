__author__ = 'alakus'

#time
from datetime import time

t = time(4,10,19)
print t
print 'hour  :', t.hour
print 'minute:', t.minute
print 'second:', t.second
print 'microsecond:', t.microsecond
print 'tzinfo:', t.tzinfo

print 'earliest time : ', time.min
print 'latest time : ', time.max
print 'resolution:', time.resolution

#Dates
from datetime import date
today = date.today()
print today
print 'ctime:', today.ctime()
print 'tuple:', today.timetuple()
print 'ordinal:', today.toordinal()
print 'Year:', today.year
print 'Mon :', today.month
print 'Day :', today.day

print 'Earliest  :', date.min
print 'Latest    :', date.max
print 'Resolution:', date.resolution

tomorrow = today.replace(day=today.day+1)
print tomorrow

difference = tomorrow - today
print difference
print type(difference)