from typing import List

from termcolor import colored

from models import PersonalTodo, WorkTodo, TodoBase
import helpers.console_helpers as console


class TodoController:

    @classmethod
    def start(cls):
        PersonalTodo.load()
        WorkTodo.load()
        console.clear()
        while True:
            console.display_menu()
            choice = input(colored('Choose an option (0-5): ', 'yellow'))

            if choice == '1':
                cls.add_personal()
            elif choice == '2':
                cls.add_work()
            elif choice == '3':
                cls.list_all()
            elif choice == '4':
                cls.update()
            elif choice == '5':
                cls.delete()
            elif choice == '0':
                print(colored('Exiting TODO List application. Goodbye!', 'green'))
                break
            else:
                print(colored('Invalid option, please try again.',
                      'red', attrs=['reverse', 'blink']))

    @staticmethod
    def __add(new_todo: TodoBase):
        # PersonalTodo.all.append(new_todo)
        # PersonalTodo.save()
        # print(colored(f'TODO "{name}" added successfully.', 'light_green'))
        new_todo.__class__.all.append(new_todo)
        new_todo.__class__.save()
        print(colored(f'"{new_todo}" added successfully.', 'light_green'))

    @classmethod
    def add_personal(cls):
        console.clear()
        name = input('Enter TODO name: ')
        description = input('Enter TODO description: ')
        new_todo = PersonalTodo(name, description)
        cls.__add(new_todo)

    @classmethod
    def add_work(cls):
        console.clear()
        ticket_number = input('Enter Ticket Number: ')
        ticket_title = input('Enter Ticket Title: ')
        new_todo = WorkTodo(ticket_title, ticket_number)
        cls.__add(new_todo)

    @staticmethod
    def __get_all_todos() -> List[TodoBase]:
        return PersonalTodo.all + WorkTodo.all

    @classmethod
    def list_all(cls):
        console.clear()
        all_todos = cls.__get_all_todos()
        if not all_todos:
            print(colored('No TODOs available.', 'yellow'))
            return
        for index, todo in enumerate(all_todos, start=1):
            done_status = '[✔️]' if todo.done else '[ ]'
            todo_color = 'dark_grey' if todo.done else 'red'
            print(colored(f'{done_status} {index}. {todo}', todo_color))
            # print(
            #     colored(f'{index}. {todo.name} - {done_status}', 'dark_grey'))
            # print(colored(f'   Description: {todo.description}', 'grey'))

    @classmethod
    def update(cls):
        cls.list_all()
        all_todos = cls.__get_all_todos()
        try:
            index = int(
                input(colored('Enter TODO number to update: ', 'light_blue'))) - 1
            if index < 0 or index >= len(all_todos):
                print(colored('Invalid TODO number.', 'red'))
                return

            todo = all_todos[index]
            # todo.name = input(
            #     colored(f'Enter new name (current: {todo.name}): ', 'light_grey')) or todo.name
            # todo.description = input(colored(f'Enter new description (current: {
            #                          todo.description}): ', 'light_grey')) or todo.description
            done_input = input(colored('Is it done? (y/n): ', 'light_grey'))
            todo.done = True if done_input.lower() == 'y' else False
            todo.__class__.save()
            print(colored(f'"{todo}" updated successfully.', 'light_green'))
        except ValueError:
            print(colored('Invalid input, please enter a number.', 'red'))

    @classmethod
    def delete(cls):
        cls.list_all()
        all_todos = cls.__get_all_todos()
        try:
            index = int(
                input(colored('Enter TODO number to delete: ', 'light_blue'))) - 1
            if index < 0 or index >= len(all_todos):
                print(colored('Invalid TODO number.', 'red'))
                return

            deleted_todo = all_todos.pop(index)
            deleted_todo.__class__.all.remove(deleted_todo)
            deleted_todo.__class__.save()
            print(colored(f'"{deleted_todo}" deleted successfully.', 'green'))
        except ValueError:
            print(colored('Invalid input, please enter a number.', 'red'))
