import boto3
import json
import aws_auth

session = boto3.session.Session(
    aws_access_key_id = aws_auth.access_key, 
    aws_secret_access_key= aws_auth.secret_key, 
    aws_session_token = aws_auth.token,
    region_name="us-east-1"
)


ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)