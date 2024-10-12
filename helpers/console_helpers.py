import os

from termcolor import colored


def clear():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def display_menu():
    # ? clear_console()
    print(colored('\n--- TODO List Menu ---', 'blue', attrs=['bold', 'underline',]))
    print(colored('1. Add Personal TODO', 'light_blue', attrs=[]))
    print(colored('2. Add Work TODO', 'light_blue', attrs=[]))
    print(colored('3. View TODOs', 'light_blue', attrs=[]))
    print(colored('4. Update TODO\'s status', 'light_blue', attrs=[]))
    print(colored('5. Delete TODO', 'light_blue', attrs=[]))
    print(colored('0. Exit', 'light_red', attrs=[]))
