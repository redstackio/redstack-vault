---
id: 66548cd2-d318-4a10-8bd0-ece2625f792f
name: AWS Sync Folder with S3 Bucket
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:33.802998+00:00'
updated_at: '2023-05-25T20:07:56.422583+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws s3 sync s3 bucket delete any missing files]]'
- '[[aws s3 sync s3 bucket with region]]'
- '[[Syncing a Local Folder with a Bucket]]'
---

# AWS Sync Folder with S3 Bucket

**Status**: ✓ Verified

## Summary

Sync a folder's contents with an S3 bucket. If the Folder has items the bucket does not, or a newer timestamp, it will copy them over. This is useful for data exfiltration, or copying files into an S3 bucket to access from a wrapper. 

## Description

# Description

Sync a folder's contents with an S3 bucket. If the Folder has items the bucket does not, or a newer timestamp, it will copy them over.

This is useful for data exfiltration, or copying files into an S3 bucket to access from a wrapper.

##  Instructions

1. Sync the local folder with a S3 Bucket



**Command** ([[Syncing a Local Folder with a Bucket]]):

```bash
aws s3 sync $FOLDER s3://$AWS_S3_BUCKET

```







2. Sync the local folder contents with a S3 Bucket



**Command** ([[aws s3 sync s3 bucket with region]]):

```bash
aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION

```







3. (Optional) Any files not found in the folder will be deleted in the S3 Bucket with this delete flag



**Command** ([[aws s3 sync s3 bucket delete any missing files]]):

```bash
aws s3 sync . s3://$AWS_S3_BUCKET --region $AWS_REGION --delete

```







## Platforms

- Cloud

## Commands Used

- [[aws s3 sync s3 bucket delete any missing files]]
- [[aws s3 sync s3 bucket with region]]
- [[Syncing a Local Folder with a Bucket]]

## Tags

- [[AWS]]
- [[Cloud]]


