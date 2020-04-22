#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import boto3

boto3.Session(profile_name='GenAdmin')

session = boto3.Session(profile_name='GenAdmin')

s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)

print(dir(s3))
