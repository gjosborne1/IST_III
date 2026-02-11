weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or L): ").upper()

if unit == "K":
    old_weight = str(weight)+" kgs"
    weight*=2.205
    unit = "lbs."
    print(f"Your weight, {old_weight}, is {round(weight,2)} {unit}")
elif unit == "L":
    old_weight = str(weight)+" lbs"
    weight/=2.205
    unit = "kgs."
    print(f"Your weight, {old_weight}, is {round(weight,2)} {unit}")
else:
    print(f"\"{unit}\" was not valid. Please use K or L.")