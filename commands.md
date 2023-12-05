docker logs spark-parquet-redshift-spark-master-1

docker cp -L scripts/spark_job.py spark-parquet-redshift-spark-master-1:/opt/bitnami/spark/script_test.py

docker-compose exec spark-master spark-submit --master spark://172.18.0.2:7077 script_test.py
