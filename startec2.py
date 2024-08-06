import boto3
import os


aws_access_key_id = aws_access_key_id = 'ASIAR5BNGUZRTE4E2TME'
aws_secret_access_key = 'RxZQzuQW2QtxnC4Z2HVj/t70Cuywkk9AViKwKSu3'
aws_session_token = 'IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCICkB0g8+5EtDVxKFPadALmD+O2d/72yYb67mg77eSirjAiEAu65S+L3X7Yz8eHt8Eahblmddc0OSsE8h2otiNDbroF4qkAMI7v//////////ARABGgwxMzEwOTEzMTAxNzkiDC1I8TA5bhgaNOx3YCrkAn1fenfnbs4mT1PUonwZy2iCd/b8Bo5EDAi5JrGsN2uNcHMUXXWZY3HOjLvFGD4f8v2gLa7o16RtRSpg0tr1PIuGqSAbJFiZE9rUq4Swlk0qLBsRc1uUzAt83Pg5OP576xhCXb7fmuYWCqiKXLiOXWMpKAQ2rKZiINJ0siTfa7F/dzfl3psySkCxkT7KaXfNh69qDm/c/HL4CiLTVkM6TrQbBv+hxhtoPAD4+wvGVGi6Bk3ML6We9ua+7YNuS/M4XmRyluxuQry2xO0wTlOuLBHgy3PE2ukB68B14p3tml3v+wK6+nh/tjikh1VpBpPY9TGqhSRYfpkA87LsjmP9Q8vK0n/kANP5AY0pApcwhPW1jf/eVRlZ47qvTghfADVMM0V1vdDYaa1iNS+JUHPk0sOi1LrRiuIl5ZkO/zWmAJ+ZXhJI3KMcOs7Po51XL0OmlkCA3tlND3NQIZDqNJyBniCo6AdfMIaxyLUGOqYBWDWzvI4zwHflX9ZHU4yfC9CPJ/f8w2n1C7nJfPTcn5Cw5c/Z+qULqGRme0mDqEVe+DNaKnVWdRklic1ACDoE6KikYSJYrWVphriY9Zd9jd1l16+UjG2FLiKgmkxFuoPlyDWg6nqqV/HyLWPL3G7Lk1vPBg3BbE3mW3rpQEZVz07ljSjH+e+iSnZrP4mOBLeNCc1xO3EYc3cOQWv5/LZknjyLurq+BQ=='
region_name = 'us-west-2'


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
