import json
import boto3

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("earthquakes")

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    data = json.loads(response['Body'].read())

    for quake in data["features"]:
        table.put_item(
            Item={
                "id": quake["id"],
                "magnitude": str(quake["properties"]["mag"]),
                "place": quake["properties"]["place"],
                "time": str(quake["properties"]["time"])
            }
        )

    return {
        "statusCode": 200,
        "body": "Success"
    }
