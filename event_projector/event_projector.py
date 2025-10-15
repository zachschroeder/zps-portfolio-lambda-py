from common.events import MovieCreated
from projections.movie_audit_projection import MovieAuditProjection
from projections.movie_list_projection import MovieListProjection


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


def get_projections():
    return [MovieListProjection(), MovieAuditProjection()]


def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] != "INSERT":
            continue
        event_data = record['dynamodb']['NewImage']
        event_data_dict = deserialize_dynamodb_item(event_data)

        movie_created = MovieCreated(event_data_dict)
        print(movie_created)

        projections = get_projections()
        for projection in projections:
            projection.handle_event(movie_created)

    return 'Successfully processed records'
