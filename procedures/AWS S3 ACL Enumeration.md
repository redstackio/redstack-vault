---
id: 39632370-6cb9-4871-8f9d-9b6eb7f12bde
name: AWS S3 ACL Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.093733+00:00'
updated_at: '2023-04-10T20:20:21.121110+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Getting ACL information about specific object]]'
commands:
- '[[Get object ACL from S3 bucket]]'
---

# AWS S3 ACL Enumeration

## Summary

AWS S3 ACL Enumeration is a technique used to gather Access Control List (ACL) information about a specific object in an AWS S3 bucket. This technique can be used by an attacker to identify sensitive data stored in an S3 bucket and to determine which AWS accounts have access to that data. An attack

## Description

# Description

AWS S3 ACL Enumeration is a technique used to gather Access Control List (ACL) information about a specific object in an AWS S3 bucket. This technique can be used by an attacker to identify sensitive data stored in an S3 bucket and to determine which AWS accounts have access to that data. An attacker can use this information to plan further attacks such as data exfiltration or privilege escalation.

To perform this technique, an attacker needs to have valid AWS credentials with the appropriate permissions to access the S3 bucket. The attacker can then use the AWS CLI or SDK to retrieve the ACL information about a specific object in the bucket. The ACL information will include a list of AWS accounts and their permissions to access the object.

Business value: This technique can help organizations to identify and secure sensitive data stored in S3 buckets. By identifying which accounts have access to sensitive data, organizations can take steps to limit access to that data and prevent unauthorized access.

## Requirements

1. Valid AWS credentials with appropriate permissions to access the S3 bucket

1. Access to the AWS CLI or SDK

## Defense

1. Ensure that AWS credentials are properly secured and not shared among users

1. Implement access controls to limit access to sensitive data stored in S3 buckets

1. Regularly monitor S3 bucket access logs for suspicious activity

## Objectives

1. To gather Access Control List (ACL) information about a specific object in an AWS S3 bucket

1. To identify sensitive data stored in an S3 bucket

1. To determine which AWS accounts have access to sensitive data

# Instructions

1. To retrieve the Access Control List (ACL) of an object in an Amazon S3 bucket, use the following command:

**Code**: [[aws s3api get-object-acl --bucket-name name --key ]]

> This command is used to retrieve the Access Control List (ACL) of an object in an Amazon S3 bucket. The `--bucket-name` parameter specifies the name of the bucket where the object is stored, and the `--key` parameter specifies the name of the object. The output of this command includes the owner of the object and a list of grants that define the permissions for the object. The grants list includes the grantee, grantee type (e.g. canonical user, Amazon S3 group, etc.), and the permissions granted to the grantee (e.g. read, write, full control, etc.).

**Command** ([[Get object ACL from S3 bucket]]):

```bash
aws s3api get-object-acl --bucket-name name --key object_name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get object ACL from S3 bucket]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Getting ACL information about specific object]]
