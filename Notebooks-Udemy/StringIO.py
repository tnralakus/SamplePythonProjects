__author__ = 'alakus'


try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO
'''
we can use StringIO to turn normal strings into in-memory file objects in our code
'''
# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = StringIO()
f.write(message)
f.read()
f.seek(0)
print f.read()
f.write(' Second line written to file like object')
# Reset cursor just like you would a file
f.seek(0)
# Read again
print f.read()
print message