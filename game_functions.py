from time import sleep
from os import get_terminal_size

def clear():
    print("\033c", end="")

def terminal_height():
    try:
        get_terminal_size()
    except OSError:
        return 3
    else:
        return get_terminal_size().lines-1

def load(sec=1.6):
    time = sec
    while time>0:
        clear()
        print("/", end="\n"*terminal_height())
        sleep(.2)
        clear()
        print("|", end="\n"*terminal_height())
        sleep(.2)
        clear()
        print("\\", end="\n"*terminal_height())
        sleep(.2)
        clear()
        print("—", end="\n"*terminal_height())
        sleep(.2)
        time-=.8
    clear()