import boto3

# Test 1: Read txt file from S3 Bucket.
# TODO: Before pushing to GH, dont forget to delete creds and comments

ACCESS_KEY = "AKIAWFERYI3C3YQ3LGQG"
SECRET_KEY = "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"

s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, region_name='us-east-1')
bucket = 'core-ctf-2022-secrets-1'
key = 'flag.txt'
obj = s3.Object(bucket, key)
content = (obj.get()['Body'].read().decode('utf-8'))

this_is_the_flag=content
print(this_is_the_flag)

# LPM{h4rdc0d1n6_cr3d3n714l5_15_n07_c00l_hum4n!}