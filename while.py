from time import sleep

num = int(input("Enter a number 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number 1-10: "))

print(f"Your number is {num}")

password = "password"
user_in = input("Enter password: ")

while not user_in == password:
    print("Wrong password. Please try again")
    user_in = input("Enter password: ")

print("Access granted")

counter = 20

while counter >= 0:
    print(counter)
    counter-=1
    sleep(.2)

print("Countdown ended")

name = input("Enter your name: ")

while name == "":
    name = input("Please enter your name: ")

print(f"Welcome, {name}")