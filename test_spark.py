
import os
import sys

# Tell Spark to use the Python interpreter in our virtual environment
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("AmazonReviewProject")
    .master("local[*]")
    .getOrCreate()
)

print("PySpark is working!")
print("Spark Version:", spark.version)
print("Python Executable:", sys.executable)

data = [
    (1, "Excellent product"),
    (2, "Good quality"),
    (3, "Not satisfied")
]

df = spark.createDataFrame(data, ["id", "review"])

df.show()

spark.stop()
