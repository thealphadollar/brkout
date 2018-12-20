from enum import Enum


def increase_enum(enum):
    value = enum.value

    if value < len(type(enum)) - 1:
        value = value + 1
    else:
        value = 0

    return (type(enum))(value)


def decrease_enum(enum):
    value = enum.value

    if value > 0:
        value = value - 1
    else:
        value = len(type(enum)) - 1

    return (type(enum))(value)


class E_Main_Menu_Option(Enum):
    ''' Enum used to decide either to start game or exit on main menu. '''
    start_game = 0
    quit = 1


class E_Striker_Color(Enum):
    ''' Enum to decide striker color. '''
    green = 0
    red = 1
    magenta = 2
    blue = 3


class E_Prison_Choice(Enum):
    ''' Enum to decide prison. '''
    home = 0
    dungeon = 1
    tartarus = 2
