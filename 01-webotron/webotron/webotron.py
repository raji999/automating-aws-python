#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import boto3
import click


session = boto3.Session(profile_name='GenAdmin')

s3 = session.resource('s3')

@click.group()
def cli():
    '''Webotron deploys websites to AWS'''
    pass

@cli.command('list-buckets')
def list_buckets():
    '''List all s3 buckets'''
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command('list-bucket-object')
@click.argument('bucket')
def list_bucket_objetcs(bucket):
    '''List objects in an S3 bucket'''
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == "__main__":
    cli()


