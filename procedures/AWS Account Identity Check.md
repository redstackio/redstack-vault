---
id: 574953ed-45fa-4436-8c6e-9f0f4b11b6b8
name: AWS Account Identity Check
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.626346+00:00'
updated_at: '2023-04-10T20:19:48.459605+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Checking which user is executing]]'
- '[[Cloud - AWS]]'
- '[[Persistence]]'
commands:
- '[[Get AWS Caller Identity]]'
---

# AWS Account Identity Check

## Summary

The AWS Account Identity Check procedure is used to determine which user is currently executing commands within an AWS environment. By using the 'Get AWS Account Identity' command, the user can retrieve information about the AWS account that is currently being used. This information can be used to 

## Description

# Description

The AWS Account Identity Check procedure is used to determine which user is currently executing commands within an AWS environment. By using the 'Get AWS Account Identity' command, the user can retrieve information about the AWS account that is currently being used. This information can be used to identify potential security risks, such as unauthorized access, and to monitor user activity within the environment. Additionally, this procedure can be used to ensure that the correct user is executing commands and to troubleshoot any issues related to user access.

## Requirements

1. Valid AWS credentials with appropriate permissions

## Defense

1. Ensure that AWS credentials are securely stored and not shared among users

1. Implement multi-factor authentication for AWS accounts

1. Regularly monitor AWS account activity for suspicious behavior

## Objectives

1. Identify the user currently executing commands within an AWS environment

1. Monitor user activity within the environment

1. Ensure correct user access and troubleshoot access issues

# Instructions

1. This command returns details about the AWS account that is associated with the credentials used to call the command. The details include the account ID, ARN, and user ID.

**Code**: [[aws sts get-caller-identity]]

> The 'aws sts get-caller-identity' command is used to retrieve the AWS account identity. This command is useful when you need to verify which AWS account you are currently using. The command returns the account ID, ARN (Amazon Resource Name), and user ID associated with the credentials used to call the command. This information can be used to ensure that you are using the correct AWS account and to troubleshoot any issues related to AWS permissions or access.

**Command** ([[Get AWS Caller Identity]]):

```bash
aws sts get-caller-identity
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get AWS Caller Identity]]

## Tags

- [[Checking which user is executing]]
- [[Cloud - AWS]]
- [[Persistence]]
