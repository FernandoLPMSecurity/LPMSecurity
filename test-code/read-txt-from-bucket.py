import boto3

ACCESS_KEY = "REDACTED"
SECRET_KEY = "REDACTED"

s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name='us-east-1')
bucket = 'core-ctf-2022-secrets-2'
key = 'flag.txt'
obj = s3.Object(bucket, key)
content = (obj.get()['Body'].read().decode('utf-8'))

this_is_the_flag=content
print(this_is_the_flag)