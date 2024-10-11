from termcolor import colored

from models.personal_todo_model import PersonalTodo
import helpers.console_helpers as console


class TodoController:

    @classmethod
    def start(cls):
        PersonalTodo.load()
        console.clear()
        while True:
            console.display_menu()
            choice = input(colored('Choose an option (0-4): ', 'yellow'))

            if choice == '1':
                cls.add()
            elif choice == '2':
                cls.list_all()
            elif choice == '3':
                cls.update()
            elif choice == '4':
                cls.delete()
            elif choice == '0':
                print(colored('Exiting TODO List application. Goodbye!', 'green'))
                break
            else:
                print(colored('Invalid option, please try again.', 'red', attrs=['reverse','blink']))

    @classmethod
    def add(cls):
        console.clear()
        name = input('Enter TODO name: ')
        description = input('Enter TODO description: ')
        new_todo = PersonalTodo(name, description)
        PersonalTodo.all.append(new_todo)
        PersonalTodo.save()
        print(colored(f'TODO "{name}" added successfully.', 'light_green'))

    @classmethod
    def list_all(cls):
        console.clear()
        if not PersonalTodo.all:
            print(colored('No TODOs available.', 'yellow'))
            return
        for index, todo in enumerate(PersonalTodo.all, start=1):
            done_status = '[✔️]' if todo.done else '[ ]'
            todo_color = 'dark_grey' if todo.done else 'red'
            print(colored(f'{done_status} {index}. {todo}', 'dark_grey'))
            # print(
            #     colored(f'{index}. {todo.name} - {done_status}', 'dark_grey'))
            # print(colored(f'   Description: {todo.description}', 'grey'))

    @classmethod
    def update(cls):
        cls.list_all()
        try:
            index = int(
                input(colored('Enter TODO number to update: ', 'light_blue'))) - 1
            if index < 0 or index >= len(PersonalTodo.all):
                print(colored('Invalid TODO number.', 'red'))
                return

            todo = PersonalTodo.all[index]
            todo.name = input(
                colored(f'Enter new name (current: {todo.name}): ', 'light_grey')) or todo.name
            todo.description = input(colored(f'Enter new description (current: {
                                     todo.description}): ', 'light_grey')) or todo.description
            done_input = input(
                colored('Is it done? (y/n): ', 'light_grey')).lower()
            todo.done = True if done_input.lower() == 'y' else False
            PersonalTodo.save()
            print(
                colored(f'TODO "{todo.name}" updated successfully.', 'light_green'))
        except ValueError:
            print(colored('Invalid input, please enter a number.', 'red'))

    @classmethod
    def delete(cls):
        cls.list_all()
        try:
            index = int(
                input(colored('Enter TODO number to delete: ', 'light_blue'))) - 1
            if index < 0 or index >= len(PersonalTodo.all):
                print(colored('Invalid TODO number.', 'red'))
                return

            deleted_todo = PersonalTodo.all.pop(index)
            PersonalTodo.save()
            print(
                colored(f'TODO "{deleted_todo.name}" deleted successfully.', 'green'))
        except ValueError:
            print(colored('Invalid input, please enter a number.', 'red'))
