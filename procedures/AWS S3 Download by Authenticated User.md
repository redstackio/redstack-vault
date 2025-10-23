---
id: 9ef03344-339d-4d68-b6ad-25a131dc2def
name: AWS S3 Download by Authenticated User
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.138841+00:00'
updated_at: '2023-04-10T20:19:54.012639+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
sub_techniques:
- '[[Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 - Exfiltration Over Unencrypted
  Non-C2 Protocol]]'
tags:
- '[[Authenticated User]]'
- '[[Cloud - AWS]]'
- '[[Data Exfiltration]]'
commands:
- '[[Download Object from S3 Bucket]]'
---

# AWS S3 Download by Authenticated User

## Summary

This procedure involves an authenticated user downloading an S3 object from an AWS environment. This technique is commonly used to exfiltrate data from a compromised AWS account. An attacker can use this technique to obtain sensitive data stored in S3 buckets, such as customer data, credentials, or

## Description

# Description

This procedure involves an authenticated user downloading an S3 object from an AWS environment. This technique is commonly used to exfiltrate data from a compromised AWS account. An attacker can use this technique to obtain sensitive data stored in S3 buckets, such as customer data, credentials, or intellectual property. To perform this technique, an attacker must have valid AWS credentials and access to the S3 bucket containing the target data. The attacker can use the AWS CLI or SDKs to download the object to their local machine. 

From a technical perspective, this technique abuses the legitimate functionality of AWS S3. The attacker can use the AWS CLI or SDKs to authenticate to the AWS environment and download the target object. The download can be performed over HTTPS, making it difficult to detect. 

The business value of this technique is that an attacker can obtain sensitive data from an AWS environment without being detected. This can lead to reputational damage, financial loss, and legal penalties for the victim organization.

 

## Requirements

1. Valid AWS credentials with S3 access

1. Access to the S3 bucket containing the target data

1. AWS CLI or SDKs installed on the attacker's machine

 

## Defense

1. Implement proper access controls to limit the number of users who can access S3 buckets

1. Enable S3 server-side encryption to protect data at rest

1. Monitor S3 bucket activity for suspicious behavior

 

## Objectives

1. Download sensitive data from an AWS S3 bucket

1. Avoid detection while exfiltrating data

 

# Instructions

1. To download an object from an S3 bucket, use the following command:

 

Replace 'name' with the name of the S3 bucket, 'object-name' with the name of the object you want to download, and 'download-file-location' with the location on your local machine where you want to save the downloaded file. This command will download the specified object from the S3 bucket to your local machine.



**Command** ([[Download Object from S3 Bucket]]):

```bash
aws s3api get-object --bucket name --key object-name download-file-location
```



## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

### Sub-Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol]]

## Commands Used

- [[Download Object from S3 Bucket]]

## Tags

- [[Authenticated User]]
- [[Cloud - AWS]]
- [[Data Exfiltration]]


