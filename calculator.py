from math import sqrt

x=float(input("Enter fist number: "))
y=float(input("Enter second number: "))

print("""\nOperator list:
Addition: +
Subtraction: -
Multiplication: *
Division: /
Exponentiation: ^
Square root (uses first number only): sqrt""")

operator=input("\nEnter operator: ")

if operator=="+":
    print(f"{x} + {y} = {x+y}")
elif operator=="-":
    print(f"{x} - {y} = {x-y}")
elif operator=="*":
    print(f"{x} * {y} = {x*y}")
elif operator=="/" and y!=0:
    print(f"{x} / {y} = {x/y}")
elif operator=="/" and y==0:
    print("Cannot divide by zero")
elif operator=="^":
    print(f"{x} ^ {y} = {pow(x,y)}")
elif operator=="sqrt":
    print(f"Square root of {x} is {sqrt(x)}")
else:
    print("Invalid input")