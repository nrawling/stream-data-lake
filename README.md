# stream-data-lake
Example of an AWS data lake consuming DB streams from S3

## General Overview

This project attempts to demonstrate an AWS-focused data lake solution.
Data sourced in RDBMS and NoSQL data sources are extracted to S3 and cataloged using Glue.
Infrastructure is provisioned using AWS-CDK (Python). 

## Architecture

(MySQL, PostgreSQL, DynamoDB, DocumentDB) -> Kinesis Stream -> S3 -> Glue

Note: the sources here are made publicly available so that you can easily test with your own data.
This solution is almost certainly not suitable for any real-world use case.

## Deployment

cdk init
cdk deploy

