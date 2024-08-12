import boto3
import os


region_name = 'us-west-2'
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_session_token = os.getenv('AWS_SESSION_TOKEN')


ec2 = boto3.client(
    'ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=region_name
)

# Replace with your EC2 instance ID
instance_id = 'i-04ca03af00d4311af'

# Start the EC2 instance
response = ec2.start_instances(InstanceIds=[instance_id])
print(response)
