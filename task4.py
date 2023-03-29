# Difference b/w remove() and discard() in a Set Method.

# Explain Remove() in Set.
# By Using Remove() Removes the specified element.

Colour = {"Red", "Blue", "Yellow"}
Colour.remove("Blue")
print(Colour)

# Explain Discard() in Set.
# By Using Discard() Removes the specified Item.

Roll_No = {256, 786, 345}
Roll_No.discard(345)
print(Roll_No)

# Difference ::-> The discard() method removes the specified
# item from the set. This method is different from the remove()
# method, because the remove() method will raise an error if
# the specified item does not exist, and the discard() method will not.