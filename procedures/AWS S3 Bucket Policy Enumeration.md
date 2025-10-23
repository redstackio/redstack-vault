---
id: 849fc679-6a2c-4a17-8a50-528e3726eed4
name: AWS S3 Bucket Policy Enumeration
type: procedure
verified: false
submitted: true
created_at: 2023-04-06T03:56:11.020459+00:00
updated_at: 2023-04-10T20:20:44.613573+00:00
tactics:
  - "[[Discovery|TA0007 - Discovery]]"
techniques:
  - "[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]"
tags:
  - "[[Cloud - AWS]]"
  - "[[Enumeration]]"
  - "[[Getting information about a specific bucket policy]]"
commands:
  - "[[Retrieve bucket policy]]"
---

# AWS S3 Bucket Policy Enumeration

## Summary

AWS S3 Bucket Policy Enumeration is a technique used by attackers to gather information about a specific bucket policy in AWS S3. This technique can be used to find misconfigured S3 buckets that are publicly accessible and can be used to exfiltrate sensitive data. Attackers can use this technique t

# Description

AWS S3 Bucket Policy Enumeration is a technique used by attackers to gather information about a specific bucket policy in AWS S3. This technique can be used to find misconfigured S3 buckets that are publicly accessible and can be used to exfiltrate sensitive data. Attackers can use this technique to gather information about the permissions granted to different AWS identities and use this information to launch further attacks. 

To perform this technique, the attacker uses the 'Retrieve S3 Bucket Policy' command to get the policy document for a specific bucket. The policy document contains information about the permissions granted to different AWS identities and can be used to identify misconfigured buckets that are publicly accessible.

Business Value: This technique can be used by attackers to identify misconfigured S3 buckets that are publicly accessible and can be used to exfiltrate sensitive data. By identifying and securing these buckets, organizations can reduce the risk of data exfiltration and improve their overall security posture.

 

## Requirements

1. Access to AWS-cli

2. Authenticated access to the target S3 bucket

3. Permissions to retrieve the bucket policy

 

## Defense

1. Ensure that S3 buckets are not publicly accessible

1. Regularly review and audit S3 bucket policies to ensure that they are properly configured

1. Use AWS Config to monitor and enforce compliance with S3 bucket policies

 

## Objectives

1. Gather information about a specific bucket policy in AWS S3

1. Identify misconfigured S3 buckets that are publicly accessible

1. Reduce the risk of data exfiltration

 

# Instructions

1. To retrieve the policy of an S3 bucket, use the following AWS CLI command:

 

This command retrieves the policy attached to the specified S3 bucket. The policy defines the permissions for the bucket and its contents. The 'name' parameter should be replaced with the name of the bucket for which you want to retrieve the policy. If the policy does not exist, the command returns an empty policy. The output of this command is a JSON representation of the bucket policy.



**Command** ([[Retrieve bucket policy]]):

```bash
aws s3api get-bucket-policy --bucket name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Retrieve bucket policy]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Getting information about a specific bucket policy]]


