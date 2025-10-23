---
id: a3c3334e-7012-419a-8b4d-930666f3f351
name: AWS S3 Bucket Public Access Block Enumeration
type: procedure
verified: false
submitted: true
created_at: 2023-04-06T03:56:11.044162+00:00
updated_at: 2023-04-10T20:20:12.197015+00:00
tactics:
  - "[[Discovery|TA0007 - Discovery]]"
techniques:
  - "[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]"
  - "[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]"
tags:
  - "[[Cloud - AWS]]"
  - "[[Enumeration]]"
  - "[[Getting the Public Access Block configuration for an S3 bucket]]"
commands:
  - "[[Check Public Access Block for S3 Bucket]]"
---

# AWS S3 Bucket Public Access Block Enumeration

## Summary

This procedure involves checking the Public Access Block configuration for an S3 bucket in AWS. S3 buckets can be accessed publicly, which can lead to data breaches and other security issues. The Public Access Block feature allows users to restrict public access to their S3 buckets. By checking the

# Description

This procedure involves checking the Public Access Block configuration for an S3 bucket in AWS. S3 buckets can be accessed publicly, which can lead to data breaches and other security issues. The Public Access Block feature allows users to restrict public access to their S3 buckets. By checking the Public Access Block configuration, an attacker can determine if a bucket is publicly accessible or not. This information can be used to plan further attacks against the target.

From a technical perspective, this procedure involves using the 'Check S3 Bucket Public Access Block' command to retrieve the Public Access Block configuration for a specific S3 bucket. The command returns a JSON object containing the configuration information.

The business value of this procedure is that it can help organizations identify and mitigate security risks related to their S3 buckets. By ensuring that the Public Access Block is properly configured, organizations can prevent unauthorized access to their data and avoid potential data breaches.

## Requirements

1. Valid AWS credentials with permissions to access the target S3 bucket

## Defense

1. Ensure that the Public Access Block is properly configured for all S3 buckets

1. Monitor S3 bucket access logs for suspicious activity

1. Implement network security controls to prevent unauthorized access to the AWS environment

## Objectives

1. Determine if a specific S3 bucket is publicly accessible or not

1. Plan further attacks against the target

# Instructions

1. To check if a specific S3 bucket has public access blocked, run the following command:

The 'get-public-access-block' command is used to retrieve the public access block configuration for the specified S3 bucket. The '--bucket' option is used to specify the name of the bucket for which the public access block configuration needs to be retrieved. If the bucket has public access blocked, the command will return a JSON object with the 'PublicAccessBlockConfiguration' field set to 'true'. If the bucket does not have public access blocked, the command will return a JSON object with the 'PublicAccessBlockConfiguration' field set to 'false'.



**Command** ([[Check Public Access Block for S3 Bucket]]):

```bash
aws s3api get-public-access-block --bucket name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Check Public Access Block for S3 Bucket]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Getting the Public Access Block configuration for an S3 bucket]]


