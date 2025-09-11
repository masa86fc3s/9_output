import boto3
import os
import requests
from datetime import datetime

s3 = boto3.client("s3")
bucket_name = os.environ["BUCKET_NAME"]

def lambda_handler(event, context):
    """
    SaaS API からデータ取得 → S3 に CSV アップロード
    """
    # ここは例としてダミー CSV を作成
    csv_content = "id,name,value\n1,Alice,100\n2,Bob,200"

    # ファイル名に日付を入れて一意にする
    filename = f"saas_data_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.csv"

    # S3 にアップロード
    s3.put_object(Bucket=bucket_name, Key=filename, Body=csv_content)
    print(f"Uploaded {filename} to bucket {bucket_name}")

    return {
        "statusCode": 200,
        "body": f"Uploaded {filename} to {bucket_name}"
    }
