## 🚀 Real-Time User Activity Data Pipeline

An end-to-end data engineering project that captures, processes, and analyzes user activity using Kafka, Spark, and Delta Lake.

### 🔥 Key Highlights

* Real-time event ingestion using Kafka
* Partitioned streaming architecture for scalability
* Data validation and bad record handling
* Distributed processing using Databricks (PySpark)
* Optimized storage using partitioned Delta tables

## 📌 Overview

This project demonstrates an end-to-end data engineering pipeline designed to capture, process, and analyze user activity in near real-time.

It simulates user interactions on a web application and processes the data using distributed systems to generate analytics-ready outputs.

---

## 🏗️ Architecture

Frontend → Flask Backend → Kafka → Consumer → Azure SQL → Databricks (Spark) → Delta Lake

---

## ⚙️ Tech Stack

* **Backend**: Python (Flask)
* **Streaming**: Apache Kafka (Docker)
* **Database**: Azure SQL Database
* **Processing**: Apache Spark (Databricks)
* **Storage**: Delta Lake
* **Frontend**: HTML, JavaScript (event simulation)

---

## 🔄 Data Flow

1. User interactions are simulated via frontend/backend
2. Events are sent to Kafka topics
3. Kafka streams data in real-time
4. Consumer reads events and stores them in Azure SQL (raw layer)
5. Databricks reads data from SQL using Spark
6. Data is cleaned and validated (bad records handled separately)
7. Aggregations are performed using PySpark
8. Processed data is stored in Delta Lake (partitioned format)

---

## 📊 Key Features

* Real-time event ingestion using Kafka
* Kafka topic partitioning for scalable data streaming
* Data quality checks and bad record handling
* Distributed data processing using Spark
* Partitioned Delta Lake storage for optimized querying
* Simulation of realistic user behavior (device, location, product)

---

## 🚧 Future Enhancements

* Backend-based event generator (continuous data ingestion)
* Kafka multi-consumer parallel processing
* Raw data ingestion directly into Data Lake (instead of SQL)
* Databricks workflows / asset bundle integration
* CI/CD pipeline for automated deployment

---

## 💡 Learning Outcomes

* Understanding of streaming data pipelines
* Kafka partitioning and data distribution
* Data validation and transformation using Spark
* Designing scalable data architectures
* Working with cloud-based data platforms

---

## 📎 Project Status

Actively evolving with improvements in scalability, automation, and architecture.
