class MovieListView:

    def __init__(self, name="movie_list", movies=None):
        self.name = name
        self.movies = movies if movies is not None else []

    @staticmethod
    def from_dict(dictionary):
        return MovieListView(dictionary["name"], dictionary["movies"])
