import boto3
import requests
import json
import os

# ec2 = boto3.resource('ec2')
#sts = boto3.resource('sts')

#req = requests.get('http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance/')

session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN,
    region_name="us-east-1"
)

#ec2.describe-instances()