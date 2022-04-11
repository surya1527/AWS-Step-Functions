import json
import boto3
import time

def lambda_handler(event, context):
    return event['transactionId'] + "-" + event['type']
    
