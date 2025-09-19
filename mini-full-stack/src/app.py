import boto3
import os
import time     #Glueジョブの状態確認時に待機するため

# クライアント作成
glue = boto3.client('glue')
athena = boto3.client('athena')

# Lambdaが起動されたときに呼ばれる関数
def lambda_handler(event, context):
    job_name = os.environ['GLUE_JOB_NAME']
    database_name = os.environ['ATHENA_DATABASE']
    output_bucket = os.environ['ATHENA_OUTPUT_BUCKET']

    # -----------------------------
    # 0. 既存GlueジョブがRUNNINGか確認
    # -----------------------------
    running_jobs = glue.get_job_runs(JobName=job_name, MaxResults=1)['JobRuns']
    if running_jobs and running_jobs[0]['JobRunState'] == 'RUNNING':
        existing_run_id = running_jobs[0]['Id']
        print(f"Previous Glue job still running. JobRunId: {existing_run_id}")
        return {
            "status": "Previous Glue job still running",
            "GlueJobRunId": existing_run_id
        }

    # -----------------------------
    # 1. Glue ジョブを起動
    # -----------------------------
    glue_response = glue.start_job_run(JobName=job_name)
    job_run_id = glue_response['JobRunId']
    print(f"Glue job started. JobRunId: {job_run_id}")

    # -----------------------------
    # 2. Glue ジョブの完了待ち（最大10分）
    # -----------------------------
    timeout_seconds = 600  # 最大待機時間10分
    poll_interval = 15
    elapsed = 0

    while elapsed < timeout_seconds:
        job_status = glue.get_job_run(JobName=job_name, RunId=job_run_id)
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
    # 3. Athena データベース作成（存在しなければ）
    # -----------------------------
    create_db_query = f"CREATE DATABASE IF NOT EXISTS {database_name};"
    athena.start_query_execution(
        QueryString=create_db_query,
        ResultConfiguration={'OutputLocation': f"s3://{output_bucket}/"}
    )
    print(f"Athena database '{database_name}' ensured.")

    # -----------------------------
    # 4. Athena テーブル作成（存在しなければ）
    # -----------------------------
    create_table_query = f"""
    CREATE EXTERNAL TABLE IF NOT EXISTS {database_name}.preprocessed_table (
        datetime string,
        y int,
        week string,
        soldout int,
        name string,
        kcal int,
        remarks string,
        event string,
        payday string,
        weather string,
        precipitation string,
        temperature double
    )
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
    WITH SERDEPROPERTIES ('serialization.format' = ',')
    LOCATION 's3://{output_bucket}/preprocessed/'
    TBLPROPERTIES ('has_encrypted_data'='false');
    """


    athena.start_query_execution(
        QueryString=create_table_query,
        ResultConfiguration={'OutputLocation': f"s3://{output_bucket}/athena-results/"} #出力先のフォルダを指定できる、ただし名前のしてはできないらしい
    )
    print(f"Athena table 'preprocessed_table' ensured.")

    # -----------------------------
    # 5. Athena クエリの実行例（確認用）
    # -----------------------------
    select_query = f"SELECT * FROM {database_name}.preprocessed_table LIMIT 10;"
    athena_response = athena.start_query_execution(
        QueryString=select_query,
        QueryExecutionContext={'Database': database_name},
        ResultConfiguration={'OutputLocation': f"s3://{output_bucket}/athena-results/"}
    )
    query_execution_id = athena_response['QueryExecutionId']
    print(f"Athena SELECT query started. QueryExecutionId: {query_execution_id}")

    return {
        "status": "Glue job and Athena queries started",
        "GlueJobRunId": job_run_id,
        "AthenaQueryExecutionId": query_execution_id
    }
