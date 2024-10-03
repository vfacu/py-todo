import os

from termcolor import cprint


def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def display_menu():
    # ? clear_console()
    cprint('\n--- TODO List Menu ---', 'red')
    print('1. Add TODO')
    print('2. View TODOs')
    print('3. Update TODO')
    print('4. Delete TODO')
    print('0. Exit')
