from time import sleep

points=int(input("What is your current XP amount? "))

sleep(1)
points+=250
print(f"After quest: {points}")
sleep(1)
points-=50
print(f"After duel loss: {points}")
sleep(1)
points*=2
print(f"After event bonus: {points}")
sleep(1)
points%=500
print(f"After level up: {points}")