import boto3
import uuid


def validate_data(dictionary: dict):
    if len(dictionary) != 3:
        raise ValueError('Invalid number of arguments')

    try:
        uuid.UUID(dictionary.get('movie_id'))
    except TypeError:
        raise ValueError('Invalid movie_id')

    if not dictionary.get('title'):
        raise ValueError('Invalid title')

    if not dictionary.get('director'):
        raise ValueError('Invalid director')


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Events")

    print(f"Event: {event}")

    # Temp code for reading items
    # items = table.scan()
    # for item in items['Items']:
    #     print(item)
    #     print(item.get('temp'))

    try:
        validate_data(event)
        event["id"] = str(uuid.uuid4())
        event["type"] = "MovieCreated"
        table.put_item(Item=event)
    except ValueError as e:
        print(e)
        return {"status_code": 400, "body": "Invalid data supplied"}
    except Exception as e:
        print(e)
        return {"status_code": 500, "body": "Item not inserted"}

    return {"status_code": 200, "body": "Item successfully inserted!"}
