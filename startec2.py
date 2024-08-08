import boto3
import os


aws_access_key_id = 'ASIAR5BNGUZR3RYG4NFH'
aws_secret_access_key = 'JfQrYVV36qmQKrYcGnMAnkNr5h+YFVC0azareLCB'
aws_session_token = 'IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIGw4mGDEJK0Zi+8qU7A0BALISvkoQBrkJfiQDwn/39ikAiA1FOD4FMDUsSufoomEWpsmYSGxqqWxBjFII0/lQI8rLyqHAwgwEAEaDDEzMTA5MTMxMDE3OSIMVO4wtzi4EJzO6uABKuQCYodXuJUmIshuT7p+OXwAz+sCeHASCMqnyiWTZTmdG+n70KLmETsmirXGR5UyN5sAEepkb5jN3cRYX6HZbT6c++DHch0lLy4zeIZf60bVi+PVgRZfpsWA/uANT/JuixPJGi6DU4T0sCJLmeS1CKmdU8o4sJieqE4h7ZP8w8lK+vXm2VpdG8mDJVS4b9jB9+3dzgMR25topj7YNjsmzsTAIwST8VIwjfkPumPMSvVmvYwem+nV3DDuVxQ/AEssJgk4Nra3gSykU9UZOz/0eNzG8kDDXKDJarSNPJQmo/FSRbiNYGBe6AkN1GnZukYcMAKU7GFJCDfoN80cBjsVNrqu54xPlzHIeGFkzHHouabYYZ0qfTPCx7+Ioi8mmNxI9PJl7D5mrnk9OMIw4bfQuO07yRKWhR7lUuyTc9VgMjSmAvz0arZYcy1HsR3h4sNhMDAOAPYIOcyIB5R8RinJvTZH4+Vqoi4wmrXTtQY6pwFYDD9xBLpIOHSXwVwdu05Fz5QNnBCAFKmPvridaGdekyGeLvXi5ijfxVr3dW3CR40f8mXQpSBuF158KS3JymBxMxUidRdYjaV3vfjnS1/whQkblunyIIKoeGYYCO3vYe7lDLvwK4dJYcDEDiI1PV9vQQJ5j1ITvZkvvlLgfNu+owWL31l+k7wi9A1Fu4rCfXqSFqthzqLoQ106/rj672ph7GzBOSVixQ=='
region_name = 'us-west-2'
#aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
#aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
#aws_session_token = os.getenv('AWS_SESSION_TOKEN')


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
