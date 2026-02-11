age=int(input("Please enter your age: "))
price=None

if age<5:
    price="Free"
elif age<13:
    price="$8"
elif age<60:
    price="$12"
else:
    price="$7"
print(f"Your ticket is {price}")