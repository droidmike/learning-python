# a tuple is a type of data structure
# they are like lists but with some key differences
# they are created using parentheses() while lists use square brackets[]
# tuples are unique as they are immutable meaning they cant be changed or modified
coordinates = (5, 7)  # we created the variable coordinates
print(coordinates[0])  # indexes still start at zero
print(coordinates[1])

# we can put a tuple inside a list
coordinates1 = [(2, 3), (4, 7), (8, 0)]
print(coordinates1[1])
