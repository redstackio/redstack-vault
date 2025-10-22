---
id: 993c1730-0f11-44e8-8b1f-3e577cda6830
name: AWS Delete File from S3 Bucket
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:24.074477+00:00'
updated_at: '2023-05-25T20:08:20.928078+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Data Destruction|T1485 - Data Destruction]]'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws s3 delete contents of S3 Bucket recursively]]'
- '[[aws s3 delete file from S3 Bucket]]'
- '[[aws s3 delete objects from S3 Bucket]]'
---

# AWS Delete File from S3 Bucket

**Status**: ✓ Verified

## Summary

You can delete individual files, folders or empty an entire bucket folder. 

## Description

# Description

You can delete individual files, folders or empty an entire bucket folder.

##  Instructions

1. Delete a file from a S3 Bucket

**Command** ([[aws s3 delete file from S3 Bucket]]):

```bash
aws s3 rm s3://<bucket_name>/<object_name>

```

2. (Optional) Delete all objects in an S3 Bucket

**Command** ([[aws s3 delete objects from S3 Bucket]]):

```bash
aws s3 rm s3://$AWS_S3_BUCKET/$OBJECT

```

3. (Optional) Empty the contents of a S3 Bucket

**Command** ([[aws s3 delete contents of S3 Bucket recursively]]):

```bash
aws s3 rm s3://$AWS_S3_BUCKET/$OBJECT --recursive

```

## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Impact|TA0040 - Impact]]

### Techniques

- [[Data Destruction|T1485 - Data Destruction]]

## Commands Used

- [[aws s3 delete contents of S3 Bucket recursively]]
- [[aws s3 delete file from S3 Bucket]]
- [[aws s3 delete objects from S3 Bucket]]

## Tags

- [[AWS]]
- [[Cloud]]
