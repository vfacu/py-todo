from config import constants

from .todo_base_model import TodoBase


class PersonalTodo(TodoBase):
    filename = constants.TODOS_PATH

    def __init__(self, name, description, done=False) -> None:
        super().__init__(done)
        self.__name = name
        self.description = description
        

    @property
    def name(self):
        return self.__name.title()
    
    def __str__(self):
        description = '' if not self.description else f': {self.description}'
        return f'{self.name}{description}'

    @name.setter
    def name(self, new_name):
        if not new_name.strip():
            raise Exception('Invalid name')
        self.__name = new_name

    # @property
    # def __dict__(self):
    #     return {
    #         'name': self.__name,
    #         'description': self.description,
    #         'done': self.done,
    #     }

    def parse_to_dict(self) -> dict:
        return {
            'name': self.__name,
            'description': self.description,
            'done': self.done,
        }

    @classmethod
    def parse_from_dict(cls, item: dict) -> 'PersonalTodo':
        # return cls(name=item['name'], description=item['description'], done=item['done'])
        return cls(**item)
