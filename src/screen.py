from enum import Enum

class MainScreenF(Enum):
    NEWGAME = 1
    LOADGAME = 2
    SETTINGS = 3
    USER = 4
    EXIT = 5
#Название / гм - стандарт / выбор пользователя


def start_screen():
    print('Название')

    print('1 - Новая игра')
    print('2 - Загрузить игру')
    print('3 - Настройки')
    print('4 - Пользователь')
    print('5 - Выход')

    user_command = int(input(":"))
    
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
