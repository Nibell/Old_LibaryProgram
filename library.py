"""
A client at a library looks up some books...
"""

import xmlrpclib
import random
import time

# Initialize random numbers:
random.seed()

SERVER_PORT = 50003
SERVER_IP = "127.0.0.1"

http_address = 'http://%s:%d' % (SERVER_IP, SERVER_PORT)
print "Using server at:", http_address

s = xmlrpclib.ServerProxy(http_address)
cache = {}

length = s.get_len()
print "ISBN records on server:", length
print

# Get 10 first records
print "10 first records"
start = time.time()
startprocent = 0
procent = 0
ms = 0
MAXSIZE = 20
clenght = 0
for i in range(2400):
    index = random.randint(0, length-1) # random number
    if cache.has_key(index):
        r = cache[index]
        startprocent +=1
        clenght +=1
        # print cache
    else:
        if len(cache) == MAXSIZE:
            arr = cache.keys()
            arrIndex = random.randint(0, len(arr)-1)
            Slumpa = arr[arrIndex]
            del cache[Slumpa]
        r = s.get_record(index)
        cache[index] = r
        # print r
        # print r['isbn'], r['title']
procent = startprocent/2400.0 * 100
ms = time.time() - start
ms = ms / 0.001
ms = ms / 2400
print "Cache", len(cache)
print "Cache lenght", clenght
print "Procent:", procent,"%"
print "Ms:", ms
print "Time:", time.time() - start, "seconds"

# Get a random record:
# index = random.randint(0, length-1) # random number
# print
# print "Record number: ", index
# print s.get_record(index)
