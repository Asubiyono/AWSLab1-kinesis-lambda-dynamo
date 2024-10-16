# Real-Time Data Processing using Python with Kinesis, Lambda & DynamoDBProject
Project Scope 
As the Lead Data Engineer at a leading urban taxi service analytics company, the task is to modernize data processing using AWS. The project involves creating a scalable, real-time data pipeline to transition from traditional workflows to a cloud-based architecture. The goal is to enhance decision-making, optimize taxi operations, and accelerate the shift to agile, data-driven solutions, improving operational efficiency and driving business impact.

![image](https://github.com/user-attachments/assets/beb099d6-b0f0-4c75-8d29-e40a8b67356e)

# Objectives:
1.	Data Ingestion:
Configure AWS Lambda to stream taxi data into Kinesis Data Streams, replacing outdated ingestion methods.
2.	Real-Time Processing:
Set up AWS Lambda for real-time processing and transformation of taxi trip data from Kinesis, delivering insights like peak times and fare trends.
3.	Data Storage:
Utilize DynamoDB for storing processed data, enhancing scalability and agile retrieval.
4.	Architecture Design:
Design and integrate the architecture involving AWS Lambda, Kinesis, and DynamoDB for efficient data flow.
5.	Modernization Opportunities:
Identify opportunities to further modernize and optimize the system.

# Steps 
1.  Create an S3 bucket 
2.	Create a Kinesis data stream
3.	Create DynamoDB tables to store aggregated results
4.	Create IAM Role for Kinesis consumer Lambda Function
5.	Develop Producer Lambda function to write data into Kinesis
6.	Develop Consumer Lambda function to consume streaming data from Kinesis
7.	Deploy Consumer Lambda function
8.	Deploy Producer Lambda function
9.	Trigger end-to-end real time streaming pipeline
