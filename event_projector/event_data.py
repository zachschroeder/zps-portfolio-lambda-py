dev_event_json = '''
{
   "Records":[
      {
         "eventID":"1",
         "eventName":"INSERT",
         "eventVersion":"1.0",
         "eventSource":"aws:dynamodb",
         "awsRegion":"us-east-1",
         "dynamodb":{
            "Keys":{
               "id":{
                  "S": "b7ee5dfe-fec9-4596-9084-eaa80e014b8a"
               }
            },
            "NewImage":{
               "director":{
                  "S":"Mr. Director"
               },
               "id":{
                  "S": "b7ee5dfe-fec9-4596-9084-eaa80e014b8a"
               },
               "movie_id": {
                  "S": "0eb06f60-1249-46a2-a2ec-0661a336e5ad"
               },
               "title": {
                  "S": "New Movie"
               },
               "type": {
                  "S": "movie_created"
               }
            },
            "SequenceNumber":"111",
            "SizeBytes":26,
            "StreamViewType":"NEW_AND_OLD_IMAGES"
         },
         "eventSourceARN":"stream-ARN"
      }
   ]
}
'''
