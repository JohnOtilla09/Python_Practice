
phrase = "\"I'am learning Python\""

print("Hello!!! \n" + phrase.upper() + " and this is amazing\n") # Convert using upper function
print("Hello!!! \n" + phrase.lower() + " and this is amazing\n") # Convert using lower case function
print(str(phrase.upper().islower()) + "\n") # Return boolean False
print("The length of the string is " + str(len(phrase)) + "\n") # Taking the length of the string phrase
print(str(phrase[4].upper()) + "\n") # Grabbing specific character inside of a string
print(str(phrase.index("Python")) + "\n") # Knowing the index of a certain character of word in a string
print(str(phrase.replace("Python", "Javascript"))) # Replacing a character or a word inside a string
