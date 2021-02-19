# The effects of the three different methods to remove an element from a list:
# removes the first matching value, not a specific index:
a = [0, 3, 2, 8]
a.remove(2)
print(a)

# del removes the item at a specific index:
a = [0, 3, 2, 8]
del a[2]
print(a)

# and pop removes the item at a specific index and returns it.
a = [0, 3, 2, 8]
number = a.pop(3)
print(a)
print(number)