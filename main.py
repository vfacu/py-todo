from termcolor import colored

import helpers.console_helpers as console
# from core.todos import add_todo, view_todos, update_todo, delete_todo  # Recomendado, lo comento para el ejemplo
from core import *  # No recomendado, ejemplo en el control de export/import
from config import constants
from helpers.file_helpers import read_json_file


def main():
    todos = read_json_file(constants.TODOS_PATH)
    console.clear()
    while True:
        console.display_menu()
        choice = input(colored('Choose an option (0-4): ', 'yellow'))

        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            view_todos(todos)
        elif choice == '3':
            update_todo(todos)
        elif choice == '4':
            delete_todo(todos)
        elif choice == '0':
            print(colored('Exiting TODO List application. Goodbye!', 'green'))
            break
        else:
            print(colored('Invalid option, please try again.', 'red', attrs=['reverse','blink']))


if __name__ == '__main__':
    main()
