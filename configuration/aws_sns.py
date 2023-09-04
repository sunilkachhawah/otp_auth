import boto3

aws_access_key_id: str = "aws_access"
aws_secret_access_key: str = "secret_key"
region_name: str = "ap-south-1"
sns_client = boto3.client(
    "sns",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)
