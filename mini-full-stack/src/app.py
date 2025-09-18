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
    timeout_seconds = 600  # 最大待機時間10分
    poll_interval = 15
    elapsed = 0

    while elapsed < timeout_seconds:
        job_status = glue.get_job_run(JobName=os.environ['GLUE_JOB_NAME'], RunId=job_run_id)
        state = job_status['JobRun']['JobRunState']
        print(f"Current Glue job state: {state}")
        if state in ['SUCCEEDED', 'FAILED', 'STOPPED']:
            break
        time.sleep(poll_interval)
        elapsed += poll_interval

    if state != 'SUCCEEDED':
        print(f"Glue job did not succeed: {state}")
        return {"status": "Glue job failed or stopped", "GlueJobState": state}

    print("Glue job succeeded.")

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
