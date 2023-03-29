# Use append() func by converting tuples into a list.
#Because we cannot append() use in tuple directly.

# Declare the Tuple
self = ("YUVRAJ ARORA", 256, "ECE", 1903811) 
print(self)
print(type(self))

# Firstly make the list and convert the elments of tuple into list.
myself = list(self)
print(myself)
print(type(myself))

# now use append() to add the element in list.
myself.append("DAVIET")
print(myself)

# Now back to convert the elments of list into tuple.
self = tuple(myself)
print(self)
print(type(self))
