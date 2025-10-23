---
id: 3e86b8b9-1097-4bb4-97ee-b39f890303d9
name: AWS S3 Bucket Object Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.070891+00:00'
updated_at: '2023-04-10T20:20:40.676725+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing all objects in a specific bucket]]'
commands:
- '[[List objects in S3 bucket]]'
---

# AWS S3 Bucket Object Enumeration

## Summary

AWS S3 Bucket Object Enumeration is a technique used to discover information about objects within a specific S3 bucket. This technique can be used by an attacker to gain insight into the data stored within the bucket, and potentially identify sensitive information. To perform this technique, the at

## Description

# Description

AWS S3 Bucket Object Enumeration is a technique used to discover information about objects within a specific S3 bucket. This technique can be used by an attacker to gain insight into the data stored within the bucket, and potentially identify sensitive information. To perform this technique, the attacker would use the 'List S3 Objects' command to retrieve a list of all objects within the targeted bucket. This information can then be used to inform further attacks against the system.

From a technical standpoint, this technique exploits the fact that the AWS S3 service provides a public API for listing the contents of a bucket. By default, this API is accessible to anyone who has access to the AWS credentials associated with the bucket.

From a business perspective, this technique highlights the importance of securing sensitive data within AWS S3 buckets. Organizations that fail to properly secure their S3 buckets are at risk of exposing sensitive information to attackers, which can result in reputational damage, legal liabilities, and financial losses.

 

## Requirements

1. Valid AWS credentials with permissions to access the targeted S3 bucket

 

## Defense

1. Secure S3 buckets by implementing access controls and permissions

1. Monitor S3 bucket activity for suspicious behavior

1. Regularly review S3 bucket configurations to ensure they align with security best practices

 

## Objectives

1. Discover information about objects within a specific S3 bucket

1. Identify sensitive information stored within the bucket

 

# Instructions

1. To list all objects in an S3 bucket, use the following command:

 

This command will list all objects in the specified S3 bucket. The output will include the object keys, sizes, and last modified dates. You can also use various options to filter the results, such as specifying a prefix or delimiter. For more information on these options, see the AWS CLI documentation.



**Command** ([[List objects in S3 bucket]]):

```bash
aws s3api list-objects --bucket name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List objects in S3 bucket]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing all objects in a specific bucket]]


