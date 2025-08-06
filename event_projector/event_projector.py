import boto3


class MovieCreated:

    def __init__(self, entries):
        self.movie_id = entries["movie_id"]
        self.title = entries["title"]
        self.director = entries["director"]

    def __str__(self):
        return f"Movie ID: '{self.movie_id}', Title: '{self.title}', Director: '{self.director}'"


class MovieListView:

    def __init__(self, name="movie_list", movies=None):
        self.name = name
        self.movies = movies if movies is not None else []

    @staticmethod
    def from_dict(dictionary):
        return MovieListView(dictionary["name"], dictionary["movies"])


class MovieListProjection:
    VIEW_NAME = "movie_list"

    def __init__(self):
        dynamodb = boto3.resource("dynamodb")
        self.table = dynamodb.Table("Views")

    def handle_event(self, event):
        view = self.get_view()

        # TODO: Implement event handling

        self.save_view(view)

    # TODO: Improve query logic
    def get_view(self):
        views = self.table.scan()
        for view in views['Items']:
            if view['name'] == self.VIEW_NAME:
                return MovieListView.from_dict(view)

        return MovieListView()

    def save_view(self, view):
        self.table.put_item(Item=vars(view))
        print("View saved")


def deserialize_dynamodb_item(dynamodb_item):
    """Convert a DynamoDB item to a dict"""
    deserialized_item = {}
    for key, value in dynamodb_item.items():
        # Check the type of the DynamoDB data and convert accordingly
        if 'S' in value:  # String
            deserialized_item[key] = value['S']
        elif 'N' in value:  # Number
            deserialized_item[key] = float(value['N'])  # Convert to float for numeric values
        elif 'BOOL' in value:  # Boolean
            deserialized_item[key] = value['BOOL']
        elif 'L' in value:  # List
            deserialized_item[key] = [deserialize_dynamodb_item(item) for item in value['L']]
        elif 'M' in value:  # Map
            deserialized_item[key] = deserialize_dynamodb_item(value['M'])
    return deserialized_item


def lambda_handler(event, context):
    for record in event['Records']:
        event_data = record['dynamodb']['NewImage']
        event_data_dict = deserialize_dynamodb_item(event_data)

        movie_created = MovieCreated(event_data_dict)
        print(movie_created)

        projection = MovieListProjection()
        projection.handle_event(movie_created)

    return 'Successfully processed records'
