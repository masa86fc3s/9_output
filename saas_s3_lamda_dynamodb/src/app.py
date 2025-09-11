import json
import boto3
import os
import uuid

# DynamoDB リソース取得
dynamodb = boto3.resource("dynamodb")
table_name = os.environ["TABLE_NAME"]
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    S3 アップロードイベントを受け取り、DynamoDB に書き込む
    """
    print("Received event:", json.dumps(event, indent=2))

    for record in event.get("Records", []):
        s3_bucket = record["s3"]["bucket"]["name"]
        s3_key = record["s3"]["object"]["key"]

        # DynamoDB に書き込み
        item = {
            "id": str(uuid.uuid4()),
            "bucket": s3_bucket,
            "filename": s3_key
        }
        table.put_item(Item=item)
        print(f"Inserted item into DynamoDB: {item}")

    return {
        "statusCode": 200,
        "body": json.dumps("Success")
    }
