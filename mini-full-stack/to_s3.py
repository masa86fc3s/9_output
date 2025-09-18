import boto3

s3 = boto3.client('s3')  # 認証情報は ~/.aws/credentials を利用
bucket = "mini-full-input"

# アップロードするファイル一覧
files_to_upload = [
    {"local": "../data/train.csv", "s3_key": "train.csv"},
    {"local": "./src/glue-scripts/etl.py", "s3_key": "glue-scripts/etl.py"}  # etl.py を S3 にアップロード
]

for f in files_to_upload:
    s3.upload_file(f["local"], bucket, f["s3_key"])
    print(f"アップロード完了: {f['s3_key']}")
