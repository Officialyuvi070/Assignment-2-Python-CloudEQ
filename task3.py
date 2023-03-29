# Explain intersection_update(), symmetric_difference_update() and symmetric_difference().

# 1. intersection_update()

x = {"yuvi", "rishu", "rohit"}
y = {"rahul", "sahil", "yuvi"}
x.intersection_update(y) 
print(x)

# 2. symmetric_difference_update()

a = {"yuvi", "rishu", "rohit"}
b = {"rahul", "sahil", "yuvi"}
a.symmetric_difference_update(b)
print(a)

# 3. symmetric_difference()

p = {"yuvi", "rishu", "rohit"}
q = {"rahul", "sahil", "yuvi"}
r = p.symmetric_difference(q)
print(r)
