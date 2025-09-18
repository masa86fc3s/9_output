import boto3
import os

glue = boto3.client('glue')
# athena = boto3.client('athena')  # コメントアウト

def lambda_handler(event, context):
    # Glue Job 起動
    glue.start_job_run(JobName=os.environ['GLUE_JOB_NAME'])
    
    # Athena 呼び出しは一旦コメントアウト
    # query = "SELECT * FROM some_table LIMIT 10;"
    # athena.start_query_execution(
    #     QueryString=query,
    #     QueryExecutionContext={'Database': os.environ['ATHENA_DATABASE']},
    #     ResultConfiguration={'OutputLocation': f"s3://{os.environ['ATHENA_OUTPUT_BUCKET']}/"}
    # )
    return {"status": "Glue job started"}
