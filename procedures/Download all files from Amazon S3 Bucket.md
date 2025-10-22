---
id: d66caf92-29f4-480a-811c-c800a09b7fbd
name: Download all files from Amazon S3 Bucket
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.631869+00:00'
updated_at: '2023-04-06T03:55:53.648548+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
tags:
- '[[Amazon Bucket S3 AWS]]'
- '[[Basic tests]]'
- '[[Download every things]]'
commands:
- '[[Sync S3 bucket content to local directory]]'
---

# Download all files from Amazon S3 Bucket

## Summary

This procedure allows an attacker to download all files from an Amazon S3 bucket. Amazon S3 is a cloud-based storage service provided by AWS. An attacker can use this procedure to exfiltrate data from an organization's S3 bucket. The attacker can use this procedure to download sensitive data such a

## Description

# Description

This procedure allows an attacker to download all files from an Amazon S3 bucket. Amazon S3 is a cloud-based storage service provided by AWS. An attacker can use this procedure to exfiltrate data from an organization's S3 bucket. The attacker can use this procedure to download sensitive data such as customer information, financial data, and intellectual property.

This procedure uses the AWS CLI to download all files from the S3 bucket. The AWS CLI provides a command-line interface for interacting with AWS services. The attacker can use this procedure to download all files from the S3 bucket without authorization.

The business value of this procedure is that it allows an attacker to steal sensitive data from an organization's S3 bucket. This can result in financial loss, reputational damage, and legal liability for the organization.

## Requirements

1. Access to AWS CLI

1. Access to an Amazon S3 bucket

## Defense

1. Implement access controls to restrict access to S3 buckets to authorized personnel only

1. Enable server-side encryption for data stored in S3 buckets

1. Monitor S3 bucket activity for suspicious behavior

## Objectives

1. Download all files from an Amazon S3 bucket

1. Steal sensitive data from an organization's S3 bucket

# Instructions

1. 1. Open a terminal
2. Install AWS CLI
3. Run the following command: aws s3 sync s3://<bucket_name>/ . --no-sign-request --region <region_name>

**Code**: [[aws s3 sync s3://level3-9afd3927f195e10225021a578e]]

> This command uses the AWS CLI to download all files from the specified S3 bucket. The --no-sign-request option is used to bypass authentication. The --region option specifies the region where the S3 bucket is located.

**Command** ([[Sync S3 bucket content to local directory]]):

```bash
aws s3 sync s3://level3-9afd3927f195e10225021a578e6f78df.flaws.cloud/ . --no-sign-request --region us-west-2
```

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[Sync S3 bucket content to local directory]]

## Tags

- [[Amazon Bucket S3 AWS]]
- [[Basic tests]]
- [[Download every things]]
