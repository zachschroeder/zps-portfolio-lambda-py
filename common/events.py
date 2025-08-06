class MovieCreated:

    def __init__(self, entries):
        self.movie_id = entries["movie_id"]
        self.title = entries["title"]
        self.director = entries["director"]

    def __str__(self):
        return f"Movie ID: '{self.movie_id}', Title: '{self.title}', Director: '{self.director}'"
