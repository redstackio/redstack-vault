---
id: b2bcf595-ea2d-4c2c-b713-4649a1eebd9e
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:08.938062+00:00'
updated_at: '2023-04-10T20:20:58.743576+00:00'
platforms:
  - Linux
  - macOS
tags:
  - aws
  - s3
  - boto3
validated: true
---

# Python Script List AWS S3 Buckets

## Code

```python
import boto3

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id='AKIAJQDP3RKREDACTED', aws_secret_access_key='igH8yFmmpMbnkcUaCqXJIRIozKVaREDACTED', region_name='us-west-1')

try:
    # List all S3 buckets
    result = s3.list_buckets()
    print(result)
except Exception as e:
    print(e)
```

## Description

This Python script uses the Boto3 library to list all S3 buckets in an AWS account, providing a simple way to enumerate storage resources during cloud assessments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| aws_access_key_id | AWS access key ID | AKIAJQDP3RKREDACTED |
| aws_secret_access_key | AWS secret access key | igH8yFmmpMbnkcUaCqXJIRIozKVaREDACTED |
| region_name | AWS region | us-west-1 |

## Usage

Save the script as list_buckets.py and run with `python list_buckets.py` after setting credentials. Useful in procedures like [[procedures/aws-cloud-security-assessment-and-auditing]] for initial S3 discovery.

## Detection

- Monitor AWS API calls to ListBuckets via CloudTrail.
- Look for unusual Boto3 usage in process logs or network traffic to AWS endpoints.
