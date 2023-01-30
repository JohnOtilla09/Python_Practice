# Tuples is like a list but the values in tuples cannot be modified or immutable
# Sample of tuples is coordinates

coordinates = (5, 8)
# coordinates[1] = 10 #immutable
print(coordinates)
print(coordinates[0]) # to access specific index use a bracket like we use in the list

#List of tuples
coordinates = [(5, 8), (8, 10), (34, 29), (1, 2)] # store multiple tuples in one list

print(coordinates[0][1])