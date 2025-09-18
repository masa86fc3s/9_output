import boto3
import os
import time

# クライアント作成
glue = boto3.client('glue')
athena = boto3.client('athena')

def lambda_handler(event, context):
    # -----------------------------
    # 1. Glue ジョブを起動
    # -----------------------------
    glue_response = glue.start_job_run(JobName=os.environ['GLUE_JOB_NAME'])
    job_run_id = glue_response['JobRunId']
    print(f"Glue job started. JobRunId: {job_run_id}")

    # -----------------------------
    # 2. Glue ジョブの完了待ち（最大10分）
    # -----------------------------
    waiter = glue.get_waiter('job_run_succeeded')
    try:
        waiter.wait(JobName=os.environ['GLUE_JOB_NAME'], RunId=job_run_id, WaiterConfig={'Delay': 15, 'MaxAttempts': 40})
        print("Glue job succeeded.")
    except Exception as e:
        print(f"Glue job failed or timed out: {e}")
        return {"status": "Glue job failed", "error": str(e)}

    # -----------------------------
    # 3. Athena クエリの実行
    # -----------------------------
    query = "SELECT * FROM preprocessed_table LIMIT 10;"  # 適宜変更
    athena_response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': os.environ['ATHENA_DATABASE']},
        ResultConfiguration={'OutputLocation': f"s3://{os.environ['ATHENA_OUTPUT_BUCKET']}/"}
    )
    query_execution_id = athena_response['QueryExecutionId']
    print(f"Athena query started. QueryExecutionId: {query_execution_id}")

    return {
        "status": "Glue job and Athena query started",
        "GlueJobRunId": job_run_id,
        "AthenaQueryExecutionId": query_execution_id
    }
