---
id: 895f3c46-7c03-4a33-b825-35c5d298ea74
name: AWS S3 API
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:34.663717+00:00'
updated_at: '2023-05-25T20:07:44.584676+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws s3 list buckets]]'
- '[[Listing the Content of a Bucket]]'
---

# AWS S3 API

**Status**: ✓ Verified

## Summary

You can use your own IAM API key and test for public access to s3 buckets you don't own. 

## Description

# Description

You can use your own IAM API key and test for public access to s3 buckets you don't own.

##  Instructions

1. List all of the S3 buckets you have access to. This one depends directly on the access provided to your IAM user/role's API Key

**Command** ([[aws s3 list buckets]]):

```bash
aws s3 ls

```

2. You can request to list the contents of a bucket, if the bucket allows public access, your IAM API key will work with S3 buckets

Owned by another organization. You can script this or use third party tools to brute-force / fuzz s3 bucket names.

**Command** ([[Listing the Content of a Bucket]]):

```bash
aws s3 ls s3://$AWS_S3_BUCKET --region $AWS_REGION

```

## Platforms

- Cloud

## Commands Used

- [[aws s3 list buckets]]
- [[Listing the Content of a Bucket]]

## Tags

- [[AWS]]
- [[Cloud]]
