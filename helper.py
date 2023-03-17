import boto3

# Define your AWS access key and secret key
aws_access_key_id = "AKIAXEPGBBEACCKCLEJH"
aws_secret_access_key = "QqDb5ZvICTnpRZui0fRQAxHUBhyGQ3qAtOHnU57X"

# Use boto3 to create a session with your AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Use awswrangler to connect to your S3 bucket
bucket_name = "ra-aws-bucket-dev"

# List the contents of your S3 bucket
s3 = session.client("s3")
print(s3)
result = s3.list_objects(Bucket=bucket_name)

# Print the contents of the bucket
if "Contents" in result:
    for obj in result["Contents"]:
        print(obj["Key"])
else:
    print("The bucket is empty.")