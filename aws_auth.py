import requests
import json

req = json.loads(requests.get('http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance/').content)
access_key = req["AccessKeyId"]
secret_key = req["SecretAccessKey"]
token = req["Token"]