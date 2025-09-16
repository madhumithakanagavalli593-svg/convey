import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Initialize S3 client
s3 = boto3.client('s3')

# Step 1: Create a bucket
bucket_name = 'my-sample-cloud-bucket-2025'

try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'us-east-1'}
    )
    print(f'✅ Bucket "{bucket_name}" created.')
except ClientError as e:
    print(f'⚠️ Error creating bucket: {e}')

# Step 2: Upload a file
file_name = 'example.txt'
with open(file_name, 'w') as f:
    f.write('Hello from the cloud!')

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print(f'✅ File "{file_name}" uploaded to "{bucket_name}".')
except FileNotFoundError:
    print('⚠️ File not found.')
except NoCredentialsError:
    print('⚠️ AWS credentials not found.')

# Step 3: List objects in the bucket
try:
    response = s3.list_objects_v2(Bucket=bucket_name)
    print('📦 Objects in bucket:')
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f" - {obj['Key']}")
    else:
        print('Bucket is empty.')
except ClientError as e:
    print(f'⚠️ Error listing bucket contents: {e}')
