# IF statements

import sys

isMale = input("Are you a male: ")
isTall = input("Are you tall: ")

if isMale.__eq__('true') or isMale.__eq__('True'): # __eq__() function to compare two strings
    isMale = True
else:
    isMale = False

if isTall.__eq__('true') or isTall.__eq__('True'): # __eq__() function to compare two strings
    isTall = True
else:
    isTall = False

# if is_male or isTall: # Using of "or"
#     print("You'r a male")
# else:
#     print("You'r a girl")

if isMale and isTall:
    print("You'r a male.")
elif isMale and not(isTall):
    print("You'r a short male.")
elif not(isMale) and isTall:
    print("You'r a female")
else:
    print("You'r a female and short one")

