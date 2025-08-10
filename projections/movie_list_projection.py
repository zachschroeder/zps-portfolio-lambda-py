import boto3

from common.aggregates import Movie
from common.events import MovieCreated
from common.views import MovieListView


class MovieListProjection:
    VIEW_NAME = "movie_list"

    def __init__(self):
        dynamodb = boto3.resource("dynamodb")
        self.table = dynamodb.Table("Views")

    def handle_event(self, event):
        view = self.get_view()
        view = self.handle_movie_created(view, event)
        self.save_view(view)

    # TODO: Improve query logic
    def get_view(self):
        views = self.table.scan()
        for view in views['Items']:
            if view['name'] == self.VIEW_NAME:
                return MovieListView.from_dict(view)

        return MovieListView()

    def save_view(self, view):
        self.table.put_item(Item=view.to_dict())

    @staticmethod
    def handle_movie_created(view: MovieListView, event: MovieCreated):
        new_movie = Movie(event.movie_id, event.title, event.director, [])

        if new_movie not in view.movies:
            view.movies.append(new_movie)

        return view
