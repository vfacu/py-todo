import os

from termcolor import colored


def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def display_menu():
    # ? clear_console()
    print(colored('\n--- TODO List Menu ---', 'blue', attrs=['bold', 'underline',]))
    print(colored('1. Add TODO', 'light_blue', attrs=[]))
    print(colored('2. View TODOs', 'light_blue', attrs=[]))
    print(colored('3. Update TODO', 'light_blue', attrs=[]))
    print(colored('4. Delete TODO', 'light_blue', attrs=[]))
    print(colored('0. Exit', 'light_red', attrs=[]))
