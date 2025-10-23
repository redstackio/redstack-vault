---
id: 95dbbaf1-5fc2-49e5-a86c-73ae8a7ea6eb
name: S3 Bucket Size Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.661902+00:00'
updated_at: '2023-04-06T03:55:53.679503+00:00'
tags:
- '[[Amazon Bucket S3 AWS]]'
- '[[Basic tests]]'
- '[[Check bucket disk size]]'
commands:
- '[[Calculate total size of files in S3 bucket]]'
- '[[Signing disabled]]'
---

# S3 Bucket Size Enumeration

## Summary

S3 Bucket Size Enumeration is a technique used to determine the size of a target S3 bucket. This technique can be used by an attacker to discover the amount of data stored in an S3 bucket and can help them determine the value of the target. An attacker can use this information to determine the next

## Description

# Description

S3 Bucket Size Enumeration is a technique used to determine the size of a target S3 bucket. This technique can be used by an attacker to discover the amount of data stored in an S3 bucket and can help them determine the value of the target. An attacker can use this information to determine the next steps in their attack.

 

## Requirements

1. Access to the AWS CLI

 

## Defense

1. Ensure that S3 buckets are not publicly accessible.

1. Implement access controls to restrict access to S3 buckets.

1. Monitor S3 bucket size and usage to detect any anomalies or unexpected changes.

 

## Objectives

1. Determine the size of a target S3 bucket

 

# Instructions

1. to use the AWS CLI without signing in to your account.

 



**Code**: [[--no-sign]]



> This command is used to bypass the need to sign in to your AWS account in order to use the AWS CLI.



**Command** ([[Signing disabled]]):

```bash
--no-sign
```



2. to enumerate the size of the target S3 bucket.

 



**Code**: [[aws s3 ls s3://<bucketname> --recursive  | grep -v]]



> This command is used to enumerate the size of a target S3 bucket. It recursively lists all objects in the bucket and calculates the total size of the bucket in megabytes. The output is in the format of 'x MB'.



**Command** ([[Calculate total size of files in S3 bucket]]):

```bash
s3 ls s3://<bucketname> --recursive  | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'
```



## Commands Used

- [[Calculate total size of files in S3 bucket]]
- [[Signing disabled]]

## Tags

- [[Amazon Bucket S3 AWS]]
- [[Basic tests]]
- [[Check bucket disk size]]


