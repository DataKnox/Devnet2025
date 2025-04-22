import boto3
import json
from dotenv import load_dotenv
import os
load_dotenv()

def get_secret(secret_name):
    client = boto3.client('secretsmanager', region_name='us-east-1')
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

# Usage
creds = get_secret("prod/db-creds")
print(creds['username'], creds['password'])
