import boto3


def lambda_handler(query, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Views")

    try:
        table_item = table.get_item(Key={"name": "movie_list"})
        view = table_item["Item"]["movies"]
    except Exception as e:
        print(e)
        return {"status_code": 500, "body": "Could not fetch movie list"}

    return {"status_code": 200, "body": view}
