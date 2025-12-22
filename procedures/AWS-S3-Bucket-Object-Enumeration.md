---
id: 3e86b8b9-1097-4bb4-97ee-b39f890303d9
name: AWS-S3-Bucket-Object-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.070891+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing all objects in a specific bucket]]'
commands:
  - '[[commands/aws-s3api-list-objects-in-bucket]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-S3-Bucket-Object-Enumeration

## Summary

This procedure demonstrates how to enumerate objects within a specific AWS S3 bucket using the AWS CLI. It allows discovery of stored data, including potentially sensitive files, by listing object keys, sizes, and modification dates, aiding in reconnaissance of cloud storage configurations.

## Description

In cloud environments, attackers often target S3 buckets for data discovery due to misconfigurations that expose buckets publicly or to unauthorized users. This procedure uses the AWS S3 API via the CLI to list objects in a targeted bucket, exploiting read permissions if present. It is applicable in scenarios where initial access to AWS credentials (e.g., via compromised IAM roles or access keys) has been obtained. The technique reveals the structure and contents of the bucket without downloading files, enabling further targeted exfiltration. Success depends on the bucket's policy allowing the ListBucket action.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least s3:ListBucket permissions on the target bucket.
2. AWS CLI installed and configured with the credentials (via `aws configure`).
3. Network access to AWS endpoints (no VPC endpoints required for public buckets).
4. Target S3 bucket name known or enumerated previously.

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict ListBucket actions to authorized roles only.
- Enable S3 server access logging and monitor CloudTrail for unauthorized ListObjects API calls.
- Use bucket policies to deny public access and require MFA for sensitive operations.
- Regularly audit S3 bucket permissions with tools like AWS Config or Pillage.

## Objectives

1. Retrieve a list of all objects in the specified S3 bucket to understand its contents.
2. Identify potentially sensitive files based on keys, sizes, and last modified dates.
3. Gather intelligence for subsequent data exfiltration or deeper cloud reconnaissance.

## Instructions

### Step 1: Configure AWS CLI Credentials

**Context**: Ensure the AWS CLI is set up with credentials that have access to the target bucket. This step verifies authentication before enumeration.

Run `aws configure` to set your access key, secret key, region, and output format if not already done.

> This command prompts for input and stores credentials in `~/.aws/credentials`. Expected output: No errors, and subsequent AWS commands authenticate successfully.

### Step 2: List Objects in the S3 Bucket

**Context**: Use the AWS S3 API to query and list all objects in the bucket. This reveals the bucket's inventory without downloading data.

**Command** ([[commands/aws-s3api-list-objects-in-bucket]]):
```bash
aws s3api list-objects-v2 --bucket $_BUCKET_NAME
```

> Replace $_BUCKET_NAME with the target bucket (e.g., mycompany-data). The -v2 flag uses the newer API version for better pagination support. Expected output: JSON response with a "Contents" array listing objects, including Key (object name), Size (bytes), LastModified (timestamp), and ETag (hash). If the bucket is empty or access denied, it returns an empty Contents array or error.
