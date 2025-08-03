import uuid

from create_movie import create_movie

input = {"movie_id": str(uuid.uuid4()), "title": "New Movie", "director": "Mr. Director"}
result = create_movie.lambda_handler(input, "local_context")
print(result)
