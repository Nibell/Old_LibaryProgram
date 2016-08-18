"""
A server serving ISBN (book) database records
"""

DATABASE_FILENAME = "isbn_database.txt"

SERVER_PORT = 50003

# Initialization

class ISBN_Record:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.author = "unknown"
        self.year   = "unknown"
        self.metadata = "ISBN records usually contains a lot of other data as well..."

    # Automatic printout if printed by 'print'
    def __str__(self):
        return self.isbn + ", " + self.title

database = []
infile = file(DATABASE_FILENAME, 'r')
for line in infile.readlines():
    if line != "" and line[0].isdigit():
        isbn, title = line.split(" ", 1)
        database += [ISBN_Record(isbn, title.rstrip())]

print "Number of ISBN records in database:", len(database)

# Server RPC methods

def get_len():
    return len(database)

def get_record(index):
    return database[index]

# Server RPC part

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Create server
server = SimpleXMLRPCServer(("", SERVER_PORT),
                            logRequests = False)
server.register_introspection_functions()

server.register_function(get_len)
server.register_function(get_record)

# Run the server's main loop
print "Waiting for connections on port:", SERVER_PORT
server.serve_forever()
