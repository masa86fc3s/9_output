import boto3

s3 = boto3.client('s3')  # 認証情報は ~/.aws/credentials を利用
bucket = "mini-full-stack"
filename = "../data/train.csv"
key = "train.csv"  # S3上のパスとファイルの名前決め

#key = "archive/sample.csv"  # S3上のパス

s3.upload_file(filename, bucket, key)
print("アップロード完了")
