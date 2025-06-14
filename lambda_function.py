import boto3
import uuid
import os

from movie import Movie


def main():
    result = lambda_handler("local_event", "local_context")
    print(result)


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Items")

    movie = Movie(str(uuid.uuid4()), "New Movie", "Mr. Director")
    print(f"Movie ID: {movie.id}")

    try:
        table.put_item(Item=movie.__dict__)
    except:
        return {"statusCode": 500, "body": "Item not inserted"}

    return {"statusCode": 200, "body": "Item successfully inserted!"}


if os.getenv("AWS_EXECUTION_ENV") is None:
    main()
