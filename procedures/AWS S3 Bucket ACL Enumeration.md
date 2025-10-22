---
id: b5deba00-ca85-49f4-99f5-1e7f1960f6a3
name: AWS S3 Bucket ACL Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.999424+00:00'
updated_at: '2023-04-10T20:20:44.280139+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Getting information about a specific bucket]]'
commands:
- '[[Get S3 Bucket ACL]]'
---

# AWS S3 Bucket ACL Enumeration

## Summary

The AWS S3 Bucket ACL Enumeration procedure involves identifying and listing the Access Control List (ACL) for a specific S3 bucket. This procedure can be used by an attacker to gain information about the permissions granted to specific AWS S3 buckets, which can be useful in further attacks. The AC

## Description

# Description

The AWS S3 Bucket ACL Enumeration procedure involves identifying and listing the Access Control List (ACL) for a specific S3 bucket. This procedure can be used by an attacker to gain information about the permissions granted to specific AWS S3 buckets, which can be useful in further attacks. The ACL lists the users and groups that are granted access to the bucket and the permissions they have. This procedure can be executed using the 'Get S3 Bucket ACL' command.

## Requirements

1. Valid AWS credentials

1. Access to the AWS S3 service

## Defense

1. Ensure that AWS credentials are properly secured and not exposed

1. Implement access control policies to restrict access to S3 buckets

1. Monitor S3 bucket access logs for suspicious activity

## Objectives

1. Identify the permissions granted to a specific AWS S3 bucket

1. Gather information for further attacks

# Instructions

1. Use the 'aws s3api get-bucket-acl' command to retrieve the access control list (ACL) for the specified S3 bucket.

The 'get-bucket-acl' command is used to retrieve the access control list (ACL) for the specified S3 bucket. The command takes the name of the bucket as an argument and returns a JSON object that contains the ACL information. The ACL information includes the owner of the bucket, the grantee (user/group) and the permissions granted to the grantee. This command can be useful for auditing the permissions of a bucket or troubleshooting access issues.

**Command** ([[Get S3 Bucket ACL]]):

```bash
aws s3api get-bucket-acl --bucket name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get S3 Bucket ACL]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Getting information about a specific bucket]]
