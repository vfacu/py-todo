from typing import List

from config import constants
from helpers.file_helpers import write_json_file, read_json_file


class Todo:
    all: List['Todo'] = []

    def __init__(self, name, description, done=False) -> None:
        self.name = name
        self.description = description
        self.done = done

    @classmethod
    def save(cls):
        write_json_file(constants.TODOS_PATH, [todo.__dict__ for todo in cls.all])

    @classmethod
    def load(cls):
        for todo_dict in read_json_file(constants.TODOS_PATH):
            todo_obj = Todo(name=todo_dict['name'], description=todo_dict['description'], done=todo_dict['done'])
            cls.all.append(todo_obj)
