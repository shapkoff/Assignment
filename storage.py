import boto3
from botocore.exceptions import ClientError

from dotenv import load_dotenv

import os


load_dotenv()

def upload_json_to_s3(
    file_path: str,
    bucket_name: str,
    object_name: str,
) -> None:
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION', 'us-east-1'),
    )

    try:
        s3.upload_file(
            Filename=file_path,
            Bucket=bucket_name,
            Key=object_name,
            ExtraArgs={'ContentType': 'application/json'},
        )
    except ClientError as e:
        raise RuntimeError(f'S3 upload failed: {e}') from e