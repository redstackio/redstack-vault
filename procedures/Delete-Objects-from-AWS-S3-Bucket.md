---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Impact]]'
techniques:
  - '[[Data Destruction]]'
tags:
  - aws
  - cloud
  - s3
  - data-destruction
platforms:
  - Cloud
commands:
  - '[[commands/aws-s3-rm-single-object]]'
  - '[[commands/aws-s3-rm-bucket-objects]]'
  - '[[commands/aws-s3-rm-prefix-recursively]]'
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Delete-Objects-from-AWS-S3-Bucket

## Summary

This procedure outlines how to delete individual objects, multiple objects, or recursively delete contents from an AWS S3 bucket using the AWS CLI. It is useful in post-exploitation scenarios where an attacker has obtained AWS credentials with delete permissions to cause data destruction or cover tracks by removing evidence or sensitive files.

## Description

In a compromised AWS environment, deleting objects from S3 buckets can disrupt operations, destroy data, or erase logs and artifacts. The AWS CLI provides straightforward commands for targeted deletions (single files), bulk deletions (multiple specified objects), or recursive removal (entire folders or buckets). This technique requires s3:DeleteObject permissions and can be detected via CloudTrail logs if enabled. It applies to any S3 bucket where the attacker has access, potentially leading to permanent data loss unless versioning or MFA delete is configured.

## Requirements

1. AWS CLI installed and configured with credentials (e.g., access key and secret key) that have s3:DeleteObject permissions on the target bucket.
2. Knowledge of the bucket name and object keys/paths to delete.
3. Network access to AWS endpoints (no special ports beyond standard HTTPS).
4. Optional: Bucket versioning disabled or permissions to bypass it for permanent deletion.

## Defense

- Enable S3 bucket versioning to allow recovery of deleted objects.
- Configure MFA Delete to require multi-factor authentication for deletions.
- Use bucket policies to restrict DeleteObject actions to trusted IAM roles.
- Monitor CloudTrail logs for s3:DeleteObject API calls and set up alerts for unusual activity.
- Implement least-privilege IAM policies to limit delete permissions.

## Objectives

1. Remove a specific file or object from the bucket to target sensitive data.
2. Delete multiple objects to clear a collection of files or logs.
3. Recursively empty a folder or the entire bucket to maximize impact.
4. Verify deletion success without triggering excessive logging.

## Instructions

### Step 1: Delete a Single Object

**Context**: This step targets and removes one specific file or object from the S3 bucket, useful for precise data destruction without affecting other contents. Ensure the object key is exact, including any prefix paths.

**Command** ([[commands/aws-s3-rm-single-object]]):
```bash
aws s3 rm s3://$_BUCKET_NAME/$_OBJECT_KEY
```

> This command issues a DELETE request to the specified object. It outputs a confirmation line if successful. Replace $_BUCKET_NAME with the target bucket and $_OBJECT_KEY with the full path to the file (e.g., documents/secret.txt). If the object doesn't exist, it will error with "NoSuchKey".

### Step 2: Delete Multiple Objects

**Context**: For removing several known objects at once, this step allows specifying multiple keys in a single command, efficient for bulk cleanup of related files like logs or backups. List each full S3 URI separated by spaces.

**Command** ([[commands/aws-s3-rm-bucket-objects]]):
```bash
aws s3 rm s3://$_BUCKET_NAME/$_OBJECT_KEY1 s3://$_BUCKET_NAME/$_OBJECT_KEY2
```

> The command processes each object sequentially, outputting "delete:" for each successful removal. Extend the command with more URIs as needed (e.g., add s3://bucket/logs1.txt s3://bucket/logs2.txt). Errors for non-existent objects are reported individually.

### Step 3: Recursively Delete Bucket Contents

**Context**: To empty a folder or the entire bucket, use recursion to delete all objects under a prefix. This is ideal for widespread destruction but may take time for large buckets and generates multiple API calls, increasing detection risk.

**Command** ([[commands/aws-s3-rm-prefix-recursively]]):
```bash
aws s3 rm s3://$_BUCKET_NAME/$_PREFIX/ --recursive
```

> This recursively deletes all objects matching the prefix (use "" for root to empty the bucket). It outputs "delete:" for each object. For the entire bucket, set $_PREFIX to empty. Monitor for throttling on very large buckets; success is indicated by no errors and the prefix becoming empty.
