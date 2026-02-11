temp = float(input("Enter temperature: "))
unit = input("Is the temperature in celsius or fahrenheit? (C or F): ").upper()

if unit == "C":
    old_temp = str(temp)+"°C"
    temp*=(9/5); temp+=32
    unit = "°F"
    print(f"{old_temp} is {round(temp, 1)}{unit}.")
    if temp<=32:
        print("That's freezing.")
    elif temp>=212:
        print("That's boiling.")
elif unit == "F":
    old_temp = str(temp)+"°F"
    temp-=32; temp*=(5/9)
    unit = "°C"
    print(f"{old_temp} is {round(temp, 1)}{unit}.")
    if temp<=0:
        print("That's freezing.")
    elif temp>=100:
        print("That's boiling.")
else:
    print(f"\"{unit}\" was not valid. Please use C or F.")