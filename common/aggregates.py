class Movie:
    def __init__(self, id: str, title: str, director: str, ratings: list):
        self.id = id
        self.title = title
        self.director = director
        self.ratings = ratings

    def __eq__(self, other):
        return self.id == other.id and self.title == other.title and self.director == other.director
