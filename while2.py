# number = 1
#
# while number <=10:
#     print(number)
#     number+=1
#
# ans = input("Type yes or no: ").lower()
#
# while not ans=="yes" and not ans=="no":
#     ans = input("Invalid input, please type yes or no: ").lower()

inp = None
while not inp==0:
    print("""Input a number to access a function:
1 - Start game
2 - Help
3 - Settings
0 - Quit""")
    inp = int(input())
    match inp:
        case 1:
            print("Loading game!\n")
        case 2:
            print("Loading manual...\n")
        case 3:
            print("Adjusting settings...\n")
        case _ if not inp==0:
            print("Invalid input\n")