import uuid

class Movie:
    def __init__(self, id: uuid, title: str, director: str):
        self.id = id
        self.title = title
        self.director = director

    def validate_data(dictionary: dict):
        try:
            uuid.UUID(dictionary.get('id'))
        except TypeError:
            raise ValueError('Invalid id')

        if not dictionary.get('title'):
           raise ValueError('Invalid title')
        
        if not dictionary.get('director'):
           raise ValueError('Invalid director')