---
id: 7699ff61-defa-4ab2-bbd3-9e106ae079ae
name: AWS S3 Bucket Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.978948+00:00'
updated_at: '2023-04-10T20:20:50.928372+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing all buckets in aws account]]'
---

# AWS S3 Bucket Enumeration

## Summary

AWS S3 Bucket Enumeration is a technique used to discover information about the S3 buckets in an AWS account. This technique is often used by attackers to identify sensitive data that may be stored in the buckets. By listing all the buckets, the attacker can determine which ones are publicly access

## Description

# Description

AWS S3 Bucket Enumeration is a technique used to discover information about the S3 buckets in an AWS account. This technique is often used by attackers to identify sensitive data that may be stored in the buckets. By listing all the buckets, the attacker can determine which ones are publicly accessible and which ones require authentication to access. This information can be used to plan further attacks against the target.

To perform this technique, the attacker uses the 'List S3 Buckets' command to obtain a list of all the buckets in the AWS account. The attacker can then use this information to identify buckets that may contain sensitive data.

## Requirements

1. Valid AWS credentials with permissions to list S3 buckets

## Defense

1. Ensure that S3 buckets are not publicly accessible unless necessary

1. Monitor S3 bucket access logs for any unauthorized access

1. Implement strong authentication and access control measures for S3 buckets

## Objectives

1. Identify all S3 buckets in an AWS account

1. Determine which buckets are publicly accessible

1. Identify buckets that may contain sensitive data

# Instructions

1. The 'list-buckets' command is used to retrieve a list of all S3 buckets in your AWS account.

This command does not require any arguments. It will simply return a JSON object with the details of each bucket, such as the name, creation date, and region. Note that this command requires the 's3:ListAllMyBuckets' permission to be granted to the user or role executing the command.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing all buckets in aws account]]
