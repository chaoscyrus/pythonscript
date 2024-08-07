import time
import os

time.sleep(120)

import boto3

#aws_access_key_id = 'ASIAR5BNGUZRZ2IMYMLJ'
#aws_secret_access_key = 'GW7/2n3/3qpco+AkxJBDsGq6eSX8Dje5b2q86zML'
#aws_session_token = 'IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBTV8Hrdgk2M/dAvzJdBNudCTUY4KQ802XEyxNDZCr5RAiARw+IwLN5qdfgxlZp9hP+9TV3es57Jdl466/pGKD4OriqHAwgQEAEaDDEzMTA5MTMxMDE3OSIMHHYkAmPCC7fzrYiPKuQC6279DHWwoOFJ0lgVEsm6zVJ6ncg/jsTWGZszNEUaIPTOQw6OC1jaz5fYd4q2LaPv1HukgiHhWman8yRornc5KL9YbPLOiKEN6En1YGkIjuwKCgB5OLopru7rjUbN5PfONxZHvaUZjw714X06sJoNKJyYHw4CgFjSzXULcONXbluv60gkGHyUpk5WnqHKJqVr8dDL8lLPBpFe0X0okEONBBdxkp3DtCpM7KaLdRKhEA7+U7wiCq08Xa2kcrLwJzvTykiBRUYuPhMDoFUbPys35NIZpQZSv2NOwW0z05NfHHXbmR2Frf1s/vXQoOv21jjAlP/7vLp4qlURC+kN+4USk3RsNohDMHpUp85eQfqQ2sgS8Tlpy/add4jwaMhnq7ZEHeS/rprT2XYN1rnH9ZH+bglf4NW0cdaeAYmM/Z1OdUELrCoieTKd6W3SgLbdAGejag+HKNVgPiVHYb9wIFgbED7N8rswm8DMtQY6pwGlt4oZ+1R3wU9kr3sRZJFoW/ZFMqaF5CMylvxLVxw6HGRTwnbsN1O2AMoFxDpyk4zH66FAuu8TTu7KNnYDQTbE8lI1KnWWgDk9X/JYeAA68tBrCnuygTJ7s5nEyn3UCxuzSwYBiBDt76yPj9sm0VHaFejkFOPo/6RF8WNHjrGEAjiMJLxrm0H3JBm5ii7jol29H2k3jnP8IA5Anxk/EIEtJyhf0z58Zg=='
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

# Stop the EC2 instance
response = ec2.stop_instances(InstanceIds=[instance_id])
print(response)
