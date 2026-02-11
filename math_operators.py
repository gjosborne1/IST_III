# import math
#
# radius=float(input("Enter the radius of the circle: "))
# circumference=2*math.pi*radius
# area=math.pi*pow(radius,2)
#
# print(f"The circumference is: {round(circumference,2)} units")
# print(f"The area is: {round(area,2)} square units")
# print("\n")
#
# a=float(input("Enter side A of the triangle: "))
# b=float(input("Enter side B of the triangle: "))
# c=math.sqrt(pow(a,2)+pow(b,2))
#
# print(f"Side C of the triangle is {round(c,2)} units")

price=float(input("Enter game price: "))
discount=float(input("Enter discount percent: "))/100
tax_percent=float(input("Enter tax percent: "))/100
price_d=price*(1-discount)
tax=price_d*tax_percent
price_f=price_d+tax

print(f"\nThe discounted price of your game is ${price_d}")
print(f"Your tax is ${tax}")
print(f"Your final price is ${price_f}")
print(f"Your change when paying with $100 will be ${100-price_f}")