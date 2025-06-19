import uuid

class Movie:
    def __init__(self, id: uuid, title: str, director: str):
        self.id = id
        self.title = title
        self.director = director

    def validate_data(dictionary: dict):
        uuid.UUID(dictionary.get('id')) # Will raise ValueError if id is bad

        if not dictionary.get('title'):
           raise ValueError('Invalid title')
        
        if not dictionary.get('director'):
           raise ValueError('Invalid director')