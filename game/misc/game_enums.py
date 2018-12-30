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
    credits = 1
    quit = 2


class E_Striker_Color(Enum):
    ''' Enum to decide striker color. '''
    green = 0
    red = 1
    magenta = 2
    blue = 3


class E_Prison_Option(Enum):
    ''' Enum to decide prison. '''
    home = 0
    dungeon = 1
    tartarus = 2


class E_Game_Result(Enum):
    ''' Enum for game result. '''
    loss = 0
    win = 1


class E_Pause_Option(Enum):
    ''' Enum for pause menu options. '''
    resume = 0
    restart = 1
    main_menu = 2
    quit = 3


class E_End_Game_Option(Enum):
    ''' Enum for end game options. '''
    restart = 0
    main_menu = 1
    quit = 2


class E_Powerup_Type(Enum):
    ''' Enum for powerups. '''
    double_damage = 0
    double_power = 1
    double_speed = 2
    no_friction = 3
