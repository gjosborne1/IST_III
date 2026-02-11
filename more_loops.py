num = 1
while num <=5:
    print(num)
    num +=1 #Avoids an infinite loop

#Menu was already made in the other loops thing so I'm not doing it again
print()

inp = None
_pass = "password"
while inp != _pass:
    inp = input("Enter password: ") #This one gives infinite attempts
print("Verification successful!")

inp = None
attempts = 3
while inp != _pass and attempts > 0:
    inp = input("Enter password: ")
    if inp != _pass:
        attempts -=1
        print(f"Attempts remaining: {attempts}")
if attempts ==0:
    print("Verification failed") #This one only gives 3 attempts
else:
    print("Verification successful!")