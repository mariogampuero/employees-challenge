FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive \
    JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64" \
    SPARK_HOME="/opt/spark/spark-3.5.5-bin-hadoop3" \
    PYSPARK_PYTHON="python3.8"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.8 \
        python3-pip \
        python3.8-venv \
        openjdk-8-jdk \
        wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python3 -m venv /app/venv && \
    . /app/venv/bin/activate && \
    pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p /opt/spark && \
    wget -qO - "https://dlcdn.apache.org/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz" | tar -xz -C /opt && \
    mv /opt/spark-3.5.5-bin-hadoop3 /opt/spark

RUN mkdir -p $SPARK_HOME/jars
COPY spark/mysql-connector-j-8.0.33.jar $SPARK_HOME/jars/
COPY app /app

EXPOSE 8000

CMD ["/app/venv/bin/uvicorn", "rest_service:app", "--host", "0.0.0.0", "--port", "8000"]