---
id: d22e18bc-c44e-41e2-bd19-96d320f220ab
name: AWS S3 Bucket Scanner
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.864278+00:00'
updated_at: '2023-04-10T20:19:45.611557+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Searching for open buckets]]'
commands:
- '[[Bucket Search]]'
---

# AWS S3 Bucket Scanner

## Summary

The AWS S3 Bucket Scanner is a tool for discovering open S3 buckets within an AWS environment. Attackers can use this tool to identify misconfigured buckets that can be accessed without authentication. This can lead to unauthorized access to sensitive data, such as customer information, credentials

## Description

# Description

The AWS S3 Bucket Scanner is a tool for discovering open S3 buckets within an AWS environment. Attackers can use this tool to identify misconfigured buckets that can be accessed without authentication. This can lead to unauthorized access to sensitive data, such as customer information, credentials, and intellectual property. The tool works by enumerating all S3 buckets in an AWS account and checking their permissions to see if they are publicly accessible. The scanner can be run from an external system or from within an AWS environment.

## Requirements

1. Access to an AWS account or an external system with network access to the AWS environment

1. The GrayHatWarfare S3 Bucket Scanner tool

## Defense

1. Ensure that S3 buckets are not accessible to the public

1. Use AWS IAM policies to restrict access to S3 buckets

1. Monitor S3 bucket access logs for unauthorized access attempts

## Objectives

1. Identify open S3 buckets within an AWS environment

1. Gain unauthorized access to sensitive data stored in misconfigured buckets

# Instructions

1. To use GrayHatWarfare S3 Bucket Scanner, follow these steps:
1. Clone the Zeus tool from https://github.com/DenizParlak/Zeus
2. Install the required Python libraries
3. Run the tool with the command 'python zeus.py --scanner s3'
4. Provide the necessary credentials
5. The scanner will start scanning the S3 buckets and return the results

**Code**: [[https://buckets.grayhatwarfare.com/]]

> The GrayHatWarfare S3 Bucket Scanner is a tool that allows users to scan S3 buckets for security vulnerabilities. It uses the Zeus tool, which is an AWS Auditing & Hardening Tool. The scanner checks for various security issues such as public access, ACL misconfigurations, and more. Users can provide their AWS credentials to the scanner, and it will scan all the S3 buckets associated with the credentials. The results of the scan are displayed in a report format, which includes details about the vulnerabilities found and recommendations for remediation.

**Command** ([[Bucket Search]]):

```bash
https://buckets.grayhatwarfare.com/
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Bucket Search]]

## Tags

- [[Cloud - AWS]]
- [[Searching for open buckets]]
