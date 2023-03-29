# How to access a particular element in set.
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if 
# a specified value is present in a set, by using the in keyword.

# By Using For Loop.
Subject = {"Python", "C++", "JAVA"}

for x in Subject:
  print(x)

# By Using in keyword.
Marks = {89, 78, 70}

print(89 in Marks)
