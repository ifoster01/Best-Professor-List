import boto3
import json

access_key = "AKIAUH3ULRMECUSPS5EJ"
secret_access_key = "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"
region = "us-east-1"

session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=region)
client_dynamo = session.resource('dynamodb')
table = client_dynamo.Table('courses')

path = r'C:\Users\isaac\Documents\RPI\Junior Year\Software Design and Documentation\bpl\src\Data\courses.json'

with open(path) as coursedata:
    records = json.load(coursedata)
    