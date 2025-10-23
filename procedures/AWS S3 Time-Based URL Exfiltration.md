---
id: ced4d768-07a9-4341-be47-cc6322a7a77a
name: AWS S3 Time-Based URL Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.164875+00:00'
updated_at: '2023-04-10T20:20:44.956719+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
tags:
- '[[Cloud - AWS]]'
- '[[Data Exfiltration]]'
- '[[Time-Based Url]]'
commands:
- '[[Generate presigned URL for S3 object]]'
---

# AWS S3 Time-Based URL Exfiltration

## Summary

AWS S3 Time-Based URL Exfiltration is a technique used by attackers to exfiltrate data from an S3 bucket. This technique involves generating a pre-signed URL for an S3 object that is set to expire after a certain period of time. Attackers can then use this URL to download the object within the spec

## Description

# Description

AWS S3 Time-Based URL Exfiltration is a technique used by attackers to exfiltrate data from an S3 bucket. This technique involves generating a pre-signed URL for an S3 object that is set to expire after a certain period of time. Attackers can then use this URL to download the object within the specified time frame. This technique can be used to bypass network security controls that may be in place to detect and prevent data exfiltration.

From a technical perspective, this technique involves using the AWS CLI or SDK to generate a pre-signed URL for an S3 object. The URL includes a signature that is valid for a specified period of time. The attacker can then use this URL to download the object before the URL expires. This technique can be used to exfiltrate sensitive data such as customer information, intellectual property, or financial data.

The business value of this technique is that it allows attackers to steal sensitive data from an organization without being detected. This can result in financial loss, reputational damage, and legal repercussions.

 

## Requirements

1. Valid AWS credentials with permissions to generate pre-signed URLs

1. Access to an S3 bucket containing sensitive data

1. AWS CLI or SDK installed on attacker's system

 

## Defense

1. Monitor S3 bucket access logs for suspicious activity

1. Implement network security controls to detect and prevent data exfiltration

1. Limit the amount of time that pre-signed URLs are valid for

 

## Objectives

1. Exfiltrate sensitive data from an S3 bucket

1. Avoid detection by network security controls

 

# Instructions

1. To generate a presigned URL for an Amazon S3 object, use the 'aws s3 presign' command followed by the S3 object path and the expiration time in seconds. The command will return a URL that can be used to access the object for the specified time period.

 



**Code**: [[aws s3 presign s3://bucket-name/object-name --expi]]



> The 'aws s3 presign' command generates a URL that can be used to access an S3 object for a specified period of time. The '--expires-in' option specifies the time in seconds for which the URL will be valid. After the specified time period, the URL will expire and can no longer be used to access the object. The presigned URL can be used to grant temporary access to an S3 object to users who do not have the necessary permissions to access the object directly. The presigned URL can also be used to provide temporary access to private content on a website.



**Command** ([[Generate presigned URL for S3 object]]):

```bash
aws s3 presign s3://bucket-name/object-name --expires-in 605000
```



## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[Generate presigned URL for S3 object]]

## Tags

- [[Cloud - AWS]]
- [[Data Exfiltration]]
- [[Time-Based Url]]


