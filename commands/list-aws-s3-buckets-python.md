---
id: c0c980d0-3ed1-4803-810e-030eb9e1b8cf
type: command
executor: python
data: >-
  import boto3\n\ns3 = boto3.client('s3',
  aws_access_key_id='$_AWS_ACCESS_KEY_ID',
  aws_secret_access_key='$_AWS_SECRET_ACCESS_KEY',
  region_name='$_AWS_REGION')\n\ntry:\n    result = s3.list_buckets()\n   
  print(result)\nexcept Exception as e:\n    print(e)
output: null
created_at: '2023-04-06T03:56:08.938062+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
tags:
  - python
  - s3
  - list
verified: true
validated: true
---

# List AWS S3 Buckets Python

## Command

```python
import boto3

s3 = boto3.client('s3', aws_access_key_id='$_AWS_ACCESS_KEY_ID', aws_secret_access_key='$_AWS_SECRET_ACCESS_KEY', region_name='$_AWS_REGION')

try:
    result = s3.list_buckets()
    print(result)
except Exception as e:
    print(e)
```

## Description

Uses Boto3 to list all S3 buckets in the AWS account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_AWS_ACCESS_KEY_ID | AWS access key | Yes |
| $_AWS_SECRET_ACCESS_KEY | AWS secret key | Yes |
| $_AWS_REGION | AWS region | Yes |

## Examples

### Basic Usage

Save as script.py and run `python script.py`

## Expected Output

{'Buckets': [{'Name': 'my-bucket', 'CreationDate': '2023-...'}], 'Owner': {...}}
