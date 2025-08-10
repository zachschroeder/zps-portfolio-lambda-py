from typing import List

from common.aggregates import Movie


class MovieListView:

    def __init__(self, name="movie_list", movies: List[Movie] = None):
        self.name = name
        self.movies = movies if movies is not None else []

    # Would like to use MovieListView.__dict instead of this custom method
    # However that results in the movies entry as a List[Movie], we want it as a List[dict]
    def to_dict(self):
        return {
            "name": self.name,
            'movies': [movie.__dict__ for movie in self.movies]
        }

    # Would like to use MovieListView(**dict) instead of this custom method
    # However that results in the movies property as a List[dict], we want it as a List[Movie]
    @staticmethod
    def from_dict(dictionary):
        movies = []
        for dict_movie in dictionary["movies"]:
            movies.append(Movie(**dict_movie))

        return MovieListView(dictionary["name"], movies)
