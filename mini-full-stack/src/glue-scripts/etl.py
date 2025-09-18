import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# S3 からデータ読み込み例
input_path = "s3://mini-full-input/train.csv"
df = spark.read.option("header", True).csv(input_path)

# 出力先に書き込み（ここは仮）
output_path = "s3://mini-full-output/preprocessed/"
df.write.mode("overwrite").csv(output_path)

job.commit()
