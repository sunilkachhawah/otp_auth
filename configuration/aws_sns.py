import boto3

aws_access_key_id: str = "AKIA3KELJ4PJC7QLRK77"
aws_secret_access_key: str = "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"
region_name: str = "ap-south-1"
sns_client = boto3.client(
    "sns",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)
