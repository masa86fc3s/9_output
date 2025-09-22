import sys
from pyspark.sql.functions import col, when
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# -----------------------------
# 0. Glueジョブ初期化
# -----------------------------
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# -----------------------------
# 1. S3 からデータ読み込み
# -----------------------------
input_path = "s3://mini-full-input/train.csv"
df = spark.read.option("header", True).csv(input_path)

# -----------------------------
# 2. 欠損値処理
# -----------------------------
# 数値列の欠損値を0で埋める
numeric_columns = ['y', 'kcal', 'temperature', 'precipitation', 'soldout']
for col_name in numeric_columns:
    df = df.withColumn(col_name, when(col(col_name).isNull(), 0).otherwise(col(col_name)))

# 文字列列の欠損値を空文字で埋める
string_columns = ['week', 'name', 'remarks', 'event', 'payday', 'weather']
for col_name in string_columns:
    df = df.withColumn(col_name, when(col(col_name).isNull(), '').otherwise(col(col_name)))

# -----------------------------
# 3. 出力先に書き込み
# -----------------------------
output_path = "s3://mini-full-output/preprocessed/"
df.write.mode("overwrite").csv(output_path)

# -----------------------------
# 4. Glueジョブ終了
# -----------------------------
job.commit()
