from game_functions import*
import random

balance = 100.0
inp = None
clear()
print("""Hello, and welcome to roulette. Would you like to place a bet?
---
Type "bet" to start betting
Type "balance" to view current money amount
Type "help" for more info on how betting works
Type "save" to create, save, or restore data to your computer
Type "quit" to quit
---""")
while True:
    inp=input().lower()
    load(1)
    match inp:
        case "bet":
            num = random.randrange(38)
            if num==37:
                num_actual="00"
            else:
                num_actual=str(num)
            if num==0 or num==37:
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
                if num%3==0:
                    row=3
                else:
                    row=num%3
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
            odd=False
            even=False
            red=False
            black=False
            row1=False
            row2=False
            row3=False
            half1=False
            half2=False
            third1=False
            third2=False
            third3=False
            _0=False
            _00=False
            bet_entered=False
            while not bet_entered:
                try:
                    inp=float(input("Enter bet amount:\n"))
                except ValueError:
                    print("Invalid input, please type a number")
                else:
                    if inp>balance:
                        print(f"Bet cannot exceed current money amount\nCurrent balance: ${balance:.2f}")
                    elif inp<.01:
                        print("Bet cannot be negative or less than 1 cent")
                    else:
                        bet=inp
                        bet_entered=True
            clear()
            print("You will be asked to make certain bets in order. If you do NOT wish to make the bet, type \"n\" to move on:")
            while inp!="o" and inp!="e" and inp!="n":
                inp = input("Type \"o\" to bet on odd or \"e\" to bet on even\n").lower()
                match inp:
                    case "o":
                        odd=True
                    case "e":
                        even=True
                    case "n":
                        pass
                    case _:
                        print("Invalid input, please type \"o\" or \"e\" or move on by typing \"n\"")
            inp=None
            while inp!="r" and inp!="b" and inp!="n":
                inp=input("Type \"r\" to bet on red or \"b\" to bet on black\n").lower()
                match inp:
                    case "r":
                        red=True
                    case "b":
                        black=True
                    case "n":
                        pass
                    case _:
                        print("Invalid input, please type \"r\" or \"b\" or move on by typing \"n\"")
            inp=None
            while inp!="1" and inp!="2" and inp!="3" and inp!="n":
                inp = input("Type \"1\" to bet on column 1, \"2\" to bet on column 2, or \"3\" to bet on column 3\n").lower()
                match inp:
                    case "1":
                        row1=True
                    case "2":
                        row2=True
                    case "3":
                        row3=True
                    case "n":
                        pass
                    case _:
                        print("Invalid input, please type \"1\" or \"2\" or \"3\" or move on by typing \"n\"")
            inp=None
            while inp!="1" and inp!="2" and inp!="n":
                inp=input("Type \"1\" to bet on half 1 (1-18) or \"2\" to bet on half 2 (19-36)\n").lower()
                match inp:
                    case "1":
                        half1=True
                    case "2":
                        half2=True
                    case "n":
                        pass
                    case _:
                        print("Invalid input, please type \"1\" or \"2\" or move on by typing \"n\"")
            inp=None
            while inp!="1" and inp!="2" and inp!="3" and inp!="n":
                inp = input("Type \"1\" to bet on third 1 (1st dozen), \"2\" to bet on third 2 (2nd dozen), or \"3\" to bet on third 3 (3rd dozen)\n").lower()
                match inp:
                    case "1":
                        third1=True
                    case "2":
                        third2=True
                    case "3":
                        third3=True
                    case "n":
                        pass
                    case _:
                        print("Invalid input, please type \"1\" or \"2\" or \"3\" or move on by typing \"n\"")
            inp=None
            while inp!="y" and inp!="n":
                inp = input("Type \"y\" to bet on 0\n").lower()
                match inp:
                    case "y":
                        _0=True
                    case "n":
                        pass
                    case _:
                        print("Invalid input, please type \"y\" or move on by typing \"n\"")
            inp=None
            while inp!="y" and inp!="n":
                inp = input("Type \"y\" to bet on 00\n").lower()
                match inp:
                    case "y":
                        _00=True
                    case "n":
                        pass
                    case _:
                        print("Invalid input, please type \"y\" or move on by typing \"n\"")
            inp=None
            #Make single bet here
            load()
            print(f"Landed on: {num_actual}")
            print(f"{num_actual} is {odd_even}")
            print(f"{num_actual} is {color}")
            if row!=0:
                print(f"{num_actual} is in column {row}")
                print(f"{num_actual} is in half {half}")
                print(f"{num_actual} is in third {third}")
            print()
            #Put win conditions here
        case "balance":
            print(f"Current balance: ${balance:.2f}")
        case "help":
            print("""Available bets:
---
Odd/Even: Bet on every odd number or every even number, 1 to 1 payout
Red/Black: Bet on every red number or every black number, 1 to 1 payout
Column: Bet on the entire first, second, or third horizontal row on the table, 2 to 1 payout
1-18 or 19-36: Bet on the entire first or second vertical half of the table, 1 to 1 payout
Dozen: Bet on the entire first, second, or third vertical third of the table, 2 to 1 payout
Single: Bet on one number on the table, 36 to 1 payout. Multiple numbers can be bet on at the same time!

The table layout is as follows:
3r  6b  9r  12r  15b  18r  21r  24b  27r  30r  33b  36r   column 3
2b  5r  8b  11b  14r  17b  20b  23r  26b  29b  32r  35b   column 2
1r  4b  7r  10b  13b  16r  19r  22b  25r  28b  31b  34r   column 1
     third 1    |     third 2      |      third 3       |
         half 1           |          half 2             |

The table also includes a green 0 and a green 00, which will each have a 36 to 1 payout
---""")
        case "save":
            print() #Do this
        case "quit":
            print(f"Final money amount: ${balance:.2f}")
            print("Bye!")
            break
        case _:
            print(f"\"{inp}\" is not a valid command")
    print("Type \"bet\" to continue playing, \"balance\" to view current balance, \"help\" for info on betting, \"save\" to save or restore data, or \"quit\" to quit")
