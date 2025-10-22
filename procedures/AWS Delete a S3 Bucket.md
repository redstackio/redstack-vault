---
id: 5f4ef15a-c21b-4b2e-8152-5fd99c60e2d7
name: AWS Delete a S3 Bucket
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:25.323723+00:00'
updated_at: '2023-05-25T20:06:32.616171+00:00'
commands:
- '[[aws s3 delete s3 bucket]]'
- '[[aws s3 delete s3 bucket that is not empty]]'
---

# AWS Delete a S3 Bucket

**Status**: ✓ Verified

## Summary

You can delete an S3 bucket, even one that is not empty by force. This can be helpful to clean up S3 buckets after you are done with them. 

## Description

# Description

You can delete an S3 bucket, even one that is not empty by force.

This can be helpful to clean up S3 buckets after you are done with them.

##  Instructions

1. Delete an S3 bucket

**Command** ([[aws s3 delete s3 bucket]]):

```bash
aws s3 rb s3://<bucket_name>

```

2. Force delete an S3 bucket that is not empty

**Command** ([[aws s3 delete s3 bucket that is not empty]]):

```bash
aws s3 rb s3://practicalaws.com --force

```

## Commands Used

- [[aws s3 delete s3 bucket]]
- [[aws s3 delete s3 bucket that is not empty]]
