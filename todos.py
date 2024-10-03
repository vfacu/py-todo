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
    print(f'TODO "{name}" added successfully.')


def view_todos(todos):
    clear_console()
    if not todos:
        print('No TODOs available.')
        return

    for index, todo in enumerate(todos, start=1):
        done_status = '✔️' if todo['done'] else '❌'
        print(f'{index}. {todo['name']} - {done_status}')
        print(f'   Description: {todo['description']}')


def update_todo(todos):
    view_todos(todos)
    try:
        index = int(input('Enter TODO number to update: ')) - 1
        if index < 0 or index >= len(todos):
            print('Invalid TODO number.')
            return

        todo = todos[index]
        todo['name'] = input(
            f'Enter new name (current: {todo['name']}): ') or todo['name']
        todo['description'] = input(f'Enter new description (current: {
                                    todo['description']}): ') or todo['description']
        done_input = input('Is it done? (y/n): ').lower()
        todo['done'] = True if done_input == 'y' else False

        print(f'TODO "{todo["name"]}" updated successfully.')
    except ValueError:
        print('Invalid input, please enter a number.')


def delete_todo(todos):
    view_todos(todos)
    try:
        index = int(input('Enter TODO number to delete: ')) - 1
        if index < 0 or index >= len(todos):
            print('Invalid TODO number.')
            return

        deleted_todo = todos.pop(index)
        print(f'TODO "{deleted_todo["name"]}" deleted successfully.')
    except ValueError:
        print('Invalid input, please enter a number.')
