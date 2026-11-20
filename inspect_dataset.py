
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("AmazonDatasetInspection")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

# Load Amazon reviews JSONL dataset
file_path = "all_beauty_reviews_sample_20000.jsonl"

df = spark.read.json(file_path)

print("\n========== DATASET SCHEMA ==========")
df.printSchema()

print("\n========== DATASET COLUMNS ==========")
print(df.columns)

print("\n========== TOTAL NUMBER OF ROWS ==========")
print(df.count())

print("\n========== FIRST 5 REVIEWS ==========")
df.show(5, truncate=80, vertical=True)

spark.stop()
