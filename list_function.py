# List Function

lucky_numbers = [10, 3, 23, 56, 7, 9]
toys = ['car', 'gun', 'ball', 'doll', 'doll', 'animal']

# toys.extend(lucky_numbers) # Append all value of lucky_number in toys list
toys.append("whisle") # append new value to toys list variable
toys.insert(3, "flower") # insert a specific value in a particular index
toys.pop() #remove an element in the last index of the list. Here the 'whisle' is removed
toys.index("animal") # Check whether an element is present in the list

toys2 = toys.copy() # copy the list toys in a new variable list
print(toys)
print(toys2)
print("\n")

toys.sort() # sort in ascending order
print(toys)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers) # reverce lucky_numbers


# print(toys.count('doll')) # count the number of time an element is available in the list
# toys.clear() #remove/clear all the values inside the list toys
# print(toys)