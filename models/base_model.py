from helpers.file_helpers import write_json_file, read_json_file


class Base:
    all: list = []
    filename = ''

    @classmethod
    def save(cls):
        write_json_file(cls.filename, [
                        todo.__dict__ for todo in cls.all])

    @classmethod
    def load(cls):
        for todo_dict in read_json_file(cls.filename):
            todo_obj = cls(name=todo_dict['name'], description=todo_dict['description'], done=todo_dict['done'])
            cls.all.append(todo_obj)
