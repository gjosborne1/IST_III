# temp = float(input("Enter the temperature in Celsius: "))
# sunny = True
# rainy = False
# cloudy = False
#
# if temp <=10 or temp >= 30:
#     print("The temperature is bad")
# else:
#     print("The temperature is good")
#
# if sunny:
#     print("It is sunny outside")
# elif rainy:
#     print("It is rainy outside")
# elif cloudy:
#     print("It is cloudy inside")
# else:
#     print("It is snowy outside")


# not, and, or

age = int(input("Enter the age: "))
_pass = input("Do you have an entry pass? y/n: ").lower()
_license = input("Do you have a valid license? y/n: ").lower()

if _pass == "y":
    _pass = True
elif _pass == "n":
    _pass = False
else:
    print("Invalid input for entry pass")
    _pass = False

if _license == "y":
    _license = True
elif _license == "n":
    _license = False
else:
    print("Invalid input for license")
    _license = False

if age < 18:
    print("Entry denied")
else:
    if _pass:
        print("Entry granted")
    else:
        print("Entry denied")

if age < 16 and _license:
    print("License is not legal, you cannot drive")
elif age < 16 and not _license:
    print("You cannot drive")
else:
    if _license:
        print("You can drive")
    else:
        print("You cannot drive")