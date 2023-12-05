FROM bitnami/spark:latest

USER root

RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
