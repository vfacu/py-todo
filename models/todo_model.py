from config import constants

from .base_model import Base


class Todo(Base):
    filename = constants.TODOS_PATH

    def __init__(self, name, description, done=False) -> None:
        self.__name = name
        self.description = description
        self.done = done

    @property
    def name(self):
        return self.__name.title()
    
    @name.setter
    def name(self, new_name):
        if not new_name.strip():
            raise Exception('Invalid name')
        self.__name = new_name

    @property
    def __dict__(self):
        return {
            'name': self.__name,
            'description': self.description,
            'done': self.done,
        }
