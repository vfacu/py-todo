from termcolor import colored

from utils import clear_console, display_menu
from todos import add_todo, view_todos, update_todo, delete_todo


def main():
    todos = []
    clear_console()
    while True:
        display_menu()
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
