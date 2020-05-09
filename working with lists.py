Cars = ["Merc", "Toyota", "Skoda", "BMW", "VW", "Nissan", "Ferrari"]  # this is an array ie [...,...,...,]
#   0  ,    1   ,    2    ,    3  ,  4  ,   5    ,  6 these are the indexes of the line 1 list
Cars[2] = "Honda"  # this is how to modify "elements" in the list
print(Cars[2])
print(Cars[1:])  # it spits out from the second item on the list considering the first is zero"0"
print(Cars[2:5])  # just check how it behaves

# LEARNING LISTS FUNCTIONS
lucky_numbers = ["10", "20", "30", "40", "50", "60"]
friends = ["mike", "eloy", "allan", "tim", "jordan", "tim", "james", "tim"]
print(lucky_numbers)
print(friends)
friends.extend(lucky_numbers)  # .extend function is used to add to another list
print(friends)  # spits out the extended list now
friends.append("lee")  # the .append function adds the element lee to the last place of friends list
print(friends)
friends.insert(4, "ian")  # the . insert function lets u add an element to the list at the position you want it
print(friends)
friends.remove("mike")  # the . remove function remove the element you want
print(friends)
friends.pop()  # this basically removes the last element on the list which was the "lee" we had added
print(friends)
print(friends.index("tim"))  # this basically searches what index tim is
print(friends.count("tim"))  # shows how many times an element appears on the list and tim appears thrice
print(friends.sort())  # this basically sorts the list into alphabetical order
print(friends)
friends.reverse()  # it reverses the order of the list
print(friends)
lucky_numbers2 = lucky_numbers.copy()  # copies the exact same list
print(lucky_numbers2)
friends.clear()  # this basically removes everything on the list
print(friends)


# continue practicing these functions and more
