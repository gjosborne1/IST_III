from game_functions import*
import random

num = random.randrange(0,38)
if num==37:
    num_actual="00"
else:
    num_actual=str(num)
if num==0 or num==38:
    odd_even="neither odd nor even"
    color="green"
    row=0; half=0; third=0
else:
    if num%2==0:
        odd_even="even"
    else:
        odd_even="odd"
    if num<11 or 18<num<29:
        if odd_even=="even":
            color="black"
        else:
            color="red"
    else:
        if odd_even=="even":
            color="red"
        else:
            color="black"
    if num<19:
        half=1
    else:
        half=2
    if num<13:
        third=1
    elif num<25:
        third=2
    else:
        third=3
    num+=2
    if num%3==0:
        row=1
    elif num%3==1:
        row=2
    else:
        row=3

load() #TESTING PURPOSES
print(f"Landed on: {num_actual}") #TESTING PURPOSES
print(f"{num_actual} is {odd_even}") #TESTING PURPOSES
print(f"{num_actual} is {color}") #TESTING PURPOSES
if row!=0: #TESTING PURPOSES
    print(f"In row {row}") #TESTING PURPOSES
    print(f"In half {half}") #TESTING PURPOSES
    print(f"In third {third}") #TESTING PURPOSES