
import json
import os
import boto3
from urllib.parse import unquote_plus

sns = boto3.client("sns")

def lambda_handler(event, context):
    topic_arn = os.environ.get("SNS_TOPIC_ARN")

    if not topic_arn:
        raise ValueError("SNS_TOPIC_ARN environment variable is missing")

    for record in event["Records"]:
        bucket_name = record["s3"]["bucket"]["name"]
        file_name = unquote_plus(
            record["s3"]["object"]["key"]
        )

        message = (
            "New document uploaded!\n\n"
            f"Bucket: {bucket_name}\n"
            f"File: {file_name}"
        )

        sns.publish(
            TopicArn=topic_arn,
            Subject="Document Upload Notification",
            Message=message
        )

    return {
        "statusCode": 200,
        "body": json.dumps("Notification sent successfully!")
    }

