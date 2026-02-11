inp = None
while not inp=="exit":
    print("""Input a number to access a function:
1 - Access Database
2 - Help
3 - Configure Settings
Type "exit" to exit\n""")
    inp = input().lower()
    match inp:
        case "1":
            print("Opening database\n")
        case "2":
            print("Opening guide\n")
        case "3":
            print("Updating settings\n")
        case "exit":
            print("Closing menu")
        case _:
            print("Invalid input\n")

print()

inp = None
attempts = 3
while inp !=4 and attempts >0:
    inp = int(input("Type 4:\n"))
    if inp != 4:
        attempts-=1
        print(f"Attempts remaining: {attempts}")

print()

inp = None
for i in range(1,4):
    while inp !=i:
        inp = int(input(f"Type {i}:\n"))
#I have no clue what this last thing would even be for tbh, it seems like there are a lot of ways you could make it more useful