from utils import clear_console, display_menu
from todos import add_todo, view_todos, update_todo, delete_todo


def main():
    todos = []
    clear_console()
    while True:
        display_menu()
        choice = input('Choose an option (0-4): ')

        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            view_todos(todos)
        elif choice == '3':
            update_todo(todos)
        elif choice == '4':
            delete_todo(todos)
        elif choice == '0':
            print('Exiting TODO List application. Goodbye!')
            break
        else:
            print('Invalid option, please try again.')


if __name__ == '__main__':
    main()
