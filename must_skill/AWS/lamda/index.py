def handler(event, context):
    print("S3 Event:", event)
    return {"statusCode": 200, "body": "Lambda executed successfully"}
