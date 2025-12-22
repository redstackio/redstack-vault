---
type: procedure
description: >-
  Delete an AWS S3 bucket, including force deletion for non-empty buckets, to
  remove storage resources during cleanup or destructive operations.
tactics:
  - '[[Impact]]'
techniques:
  - '[[Data Destruction]]'
sub_techniques: []
tags:
  - aws
  - s3
  - deletion
  - impact
  - data-destruction
commands:
  - '[[commands/aws-s3-rm-bucket]]'
  - '[[commands/aws-s3-rm-bucket-force]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
skill_level: beginner
impact_level: high
detection_risk: high
verified: true
validated: true
---

# aws-delete-s3-bucket

## Summary

This procedure demonstrates how to delete an AWS S3 bucket using the AWS CLI, including options for force-deleting non-empty buckets. It is useful in red team operations for cleaning up resources after testing, or in destructive scenarios to remove data storage, potentially causing data loss and service disruption.

## Description

AWS S3 buckets are object storage resources that can hold files and data. Deleting a bucket removes the container and, if force-enabled, all objects within it. This technique aligns with impact tactics in offensive security, where attackers may delete buckets to erase evidence, disrupt operations, or destroy data. The procedure requires AWS credentials with s3:DeleteBucket and s3:DeleteObject permissions. It targets cloud environments and can be executed from any machine with AWS CLI installed. Success results in the permanent removal of the bucket, which cannot be undone without backups.

## Requirements

1. AWS CLI installed and configured with credentials that have s3:DeleteBucket permission.
2. Access to the AWS account owning the S3 bucket.
3. For non-empty buckets, s3:DeleteObject permission on all objects.
4. Network connectivity to AWS endpoints.

## Defense

Defensive measures include:
- Enabling S3 bucket versioning and MFA Delete to prevent accidental or malicious deletions.
- Monitoring CloudTrail logs for s3:DeleteBucket and s3:DeleteObject API calls.
- Implementing least-privilege IAM policies to restrict delete permissions.
- Setting up S3 bucket policies to deny delete actions from unauthorized sources.

## Objectives

1. Remove an empty S3 bucket to clean up resources.
2. Force-delete a non-empty S3 bucket to ensure complete removal of data.
3. Verify successful deletion to confirm impact.

## Instructions

### Step 1: Delete an Empty S3 Bucket

**Context**: This step removes a bucket that contains no objects. Attempting to delete a non-empty bucket without force will fail, so confirm emptiness first via AWS console or CLI listing.

**Command** ([[commands/aws-s3-rm-bucket]]):
```bash
aws s3 rb s3://$_BUCKET_NAME
```

> This command recursively removes the bucket if empty. Replace $_BUCKET_NAME with the target bucket (e.g., my-test-bucket). Expected output includes a success message like "remove_bucket: my-test-bucket". If the bucket is not empty, it will error with "BucketNotEmpty".

### Step 2: Force Delete a Non-Empty S3 Bucket

**Context**: For buckets with objects, use the --force flag to delete all contents first, then the bucket itself. This is irreversible and should be used cautiously in testing.

**Command** ([[commands/aws-s3-rm-bucket-force]]):
```bash
aws s3 rb s3://$_BUCKET_NAME --force
```

> This command deletes all objects and the bucket. Replace $_BUCKET_NAME with the target (e.g., practicalaws.com). It will output progress like "delete: s3://bucket/object1" for each object, ending with "remove_bucket: bucket-name". Monitor for errors if permissions are insufficient.
