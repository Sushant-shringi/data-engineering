import json
import boto3
import urllib.request

s3 = boto3.client('s3')

def lambda_handler(event, context):

    url = (
        "https://earthquake.usgs.gov/fdsnws/event/1/query"
        "?format=geojson"
        "&starttime=2025-06-01"
        "&endtime=2025-06-10"
        "&minmagnitude=4.5"
    )

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    s3.put_object(
        Bucket="sushant-earthquake",
        Key="earthquakes/usgs_data.json",
        Body=json.dumps(data)
    )

    return {
        "statusCode": 200,
        "body": "Data uploaded to S3"
    }
