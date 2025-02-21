
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))

Choice = int(input("Enter Your Choice 1(Add)/2(Subtract)/3(Multiply)/4(Divide): "))

if Choice == 1:
    print("Result:", add(a, b))
elif Choice == 2:
    print("Result:", sub(a, b))
elif Choice == 3:
    print("Result:", multiply(a, b))
elif Choice == 4:
    print("Result:", divide(a, b))
else:
    print("Invalid Choice! Please enter a valid choice.")
