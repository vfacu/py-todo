from abc import ABC, abstractmethod
from typing import List

from helpers.file_helpers import write_json_file, read_json_file


class Base(ABC):
    all: List['Base'] = []
    filename: str = None

    @abstractmethod
    def parse_to_dict(self) -> dict:
        pass

    @classmethod
    def __check_filename(cls):
        if (cls.filename is None) or (not cls.filename.endswith('.json')):
            raise Exception('Cada clase hija de Base debe settear el atributo de clase "filename"')

    @classmethod
    def save(cls):
        cls.__check_filename()
        write_json_file(cls.filename, [item.parse_to_dict() for item in cls.all])

    @classmethod
    @abstractmethod
    def parse_from_dict(cls, item:dict) -> 'Base':
        pass

    @classmethod
    def load(cls):
        cls.__check_filename()
        
        item_list: list[dict] = read_json_file(cls.filename)
        # for item in read_json_file(cls.filename):
        #     # item_obj = cls(name=item['name'], description=item['description'], done=item['done'])
        #     item_obj = cls.parse_from_dict(item)
        #     cls.all.append(item_obj)
        cls.all = [cls.parse_from_dict(item) for item in item_list]
