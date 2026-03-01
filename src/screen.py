from enum import Enum
from core import *
import sys
import os

#Enum with choices from player
class MainScreenF(Enum):
    NEWGAME = 1
    LOADGAME = 2
    SETTINGS = 3
    USER = 4
    EXIT = 5

#Print text with border
def print_label(text, color="\033[96m", reset="\033[0m"):
    border = "═" * (len(text) + 4)
    print(f"{color}╔{border}╗{reset}")
    print(f"{color}║  {text}  ║{reset}")
    print(f"{color}╚{border}╝{reset}\n")

#Clear screen
def clear():
    if os.name == 'nt':                     # Windows
        _ = os.system('cls')
    else:
        sys.stdout.write('\033[2J\033[H')   # ANSI: Clear and go to begin
        sys.stdout.flush()

#Draw a start screen
def start_screen():
    #Get player choice and check it
    user_command = 0
    while True:
        print_label("History Generator")
        print('1 - Новая игра')
        print('2 - Загрузить игру')
        print('3 - Настройки')
        print('4 - Пользователь')
        print('5 - Выход')

        user_command = safe_input("→ ", int, -1, False)

        if user_command <= 0 or user_command > len(MainScreenF):
            clear()
        else:
            break


    match user_command:
        case 1:
            return MainScreenF.NEWGAME
        case 2:
            return MainScreenF.LOADGAME
        case 3:
            return MainScreenF.SETTINGS
        case 4:
            return MainScreenF.USER
        case 5:
            return MainScreenF.EXIT


    return None
