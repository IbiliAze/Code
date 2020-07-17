import boto3
from pprint import pprint
import json

s3 = boto3.client('s3')
buckets = s3.list_buckets()
pprint(buckets)
print(type(buckets))