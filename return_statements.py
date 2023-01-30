# Return Statements

def sayHi(n1, n2):
    result = float(n2) + float(n1)
    return result

n1 =input("Enter a number: ")
n2 = input("Enter a number: ")

result = sayHi(n1, n2) # Simple calculator in python using function

print("The answer is " + str(result))