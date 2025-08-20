import uuid


class CreateMovie:
    def __init__(self, id: str, title: str, director: str):
        self.id = id
        self.title = title
        self.director = director

    @staticmethod
    def validate_dict(dictionary: dict):
        if len(dictionary) != 3:
            raise ValueError('Invalid number of arguments')

        try:
            uuid.UUID(dictionary.get('movie_id'))
        except TypeError:
            raise ValueError('Invalid movie_id')

        if not dictionary.get('title'):
            raise ValueError('Invalid title')

        if not dictionary.get('director'):
            raise ValueError('Invalid director')
