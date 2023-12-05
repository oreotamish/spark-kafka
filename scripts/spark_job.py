from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType

spark = SparkSession.builder \
    .appName("KafkaPySparkIntegration") \
    .master("spark://spark-master:7077") \
    .getOrCreate()


kafka_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "test") \
    .option("startingOffsets", "earliest") \
    .load()


json_stream = kafka_stream.selectExpr("CAST(value AS STRING)")

schema = spark.read.json(json_stream.rdd.map(lambda row: row.value)).schema
parsed_stream = json_stream.select(from_json("value", schema).alias("data"))

output_path = "/data/parquet_output"
checkpoint_path = "/data/checkpoint"

query = parsed_stream.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", output_path) \
    .option("checkpointLocation", checkpoint_path) \
    .start()

query.awaitTermination()
