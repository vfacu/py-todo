from termcolor import colored

from utils import clear_console


def add_todo(todos):
    clear_console()
    name = input('Enter TODO name: ')
    description = input('Enter TODO description: ')
    todo = {
        'name': name,
        'done': False,
        'description': description
    }
    todos.append(todo)
    print(colored(f'TODO "{name}" added successfully.', 'light_green'))


def view_todos(todos):
    clear_console()
    if not todos:
        print(colored('No TODOs available.', 'yellow'))
        return

    for index, todo in enumerate(todos, start=1):
        done_status = '✔️' if todo['done'] else '❌'
        print(colored(f'{index}. {todo['name']} - {done_status}', 'dark_grey'))
        print(colored(f'   Description: {todo['description']}', 'grey'))


def update_todo(todos):
    view_todos(todos)
    try:
        index = int(input(colored('Enter TODO number to update: ','light_blue'))) - 1
        if index < 0 or index >= len(todos):
            print(colored('Invalid TODO number.', 'red'))
            return

        todo = todos[index]
        todo['name'] = input(colored(f'Enter new name (current: {todo['name']}): ', 'light_grey')) or todo['name']
        todo['description'] = input(colored(f'Enter new description (current: {todo['description']}): ', 'light_grey')) or todo['description']
        done_input = input(colored('Is it done? (y/n): ', 'light_grey')).lower()
        todo['done'] = True if done_input == 'y' else False

        print(colored(f'TODO "{todo["name"]}" updated successfully.', 'light_green'))
    except ValueError:
        print(colored('Invalid input, please enter a number.', 'red'))


def delete_todo(todos):
    view_todos(todos)
    try:
        index = int(input(colored('Enter TODO number to delete: ', 'light_blue'))) - 1
        if index < 0 or index >= len(todos):
            print(colored('Invalid TODO number.', 'red'))
            return

        deleted_todo = todos.pop(index)
        print(colored(f'TODO "{deleted_todo["name"]}" deleted successfully.', 'green'))
    except ValueError:
        print(colored('Invalid input, please enter a number.', 'red'))
