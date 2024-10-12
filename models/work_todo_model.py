from config import constants
from .todo_base_model import TodoBase


class WorkTodo(TodoBase):
    _filename = constants.WORK_TODOS_PATH

    def __init__(self, ticket_title, ticket_number, done=False):
        super().__init__(done)
        self.__ticket_title: str = ticket_title
        self.__ticket_number: str = ticket_number

    def __str__(self):
        return f'#{self.ticket_number} {self.ticket_title}'

    @property
    def ticket_title(self):
        return self.__ticket_title.title()

    @ticket_title.setter
    def ticket_title(self, new_ticket_title: str):
        if not new_ticket_title.strip():
            raise Exception('Invalid ticket_title')
        self.__ticket_title = new_ticket_title

    @property
    def ticket_number(self):
        return self.__ticket_number.title()

    @ticket_number.setter
    def ticket_number(self, new_ticket_number: str):
        if not new_ticket_number.strip():
            raise Exception('Invalid ticket_number')
        self.__ticket_number = new_ticket_number

    def parse_to_dict(self) -> dict:
        return {
            'ticket_number': self.__ticket_number,
            'ticket_title': self.__ticket_title,
            'done': self.done,
        }
    
    @classmethod
    def parse_from_dict(cls, item: dict) -> 'WorkTodo':
        return cls(**item)
