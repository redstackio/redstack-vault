---
id: a46a8148-dcde-4c40-943b-a3dc4ba9aea6
name: AWS IAM Role Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.195931+00:00'
updated_at: '2023-04-10T20:20:20.446749+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[3. Enumeratig Roles]]'
- '[[Cloud - AWS]]'
- '[[Listing IAM Roles]]'
commands:
- '[[List IAM Roles]]'
---

# AWS IAM Role Enumeration

## Summary

AWS IAM Role Enumeration is a technique used to discover the IAM roles present in an AWS account. IAM roles are used to grant permissions to an AWS resource, and can be used to escalate privileges in an AWS environment. By listing the IAM roles in an account, an attacker can gain insight into the p

## Description

# Description

AWS IAM Role Enumeration is a technique used to discover the IAM roles present in an AWS account. IAM roles are used to grant permissions to an AWS resource, and can be used to escalate privileges in an AWS environment. By listing the IAM roles in an account, an attacker can gain insight into the permissions granted to resources and potentially identify roles that can be abused to escalate privileges. This technique can be used as a precursor to other attacks, such as privilege escalation or resource exploitation.

Technical Explanation: The AWS IAM ListRoles API can be used to list all IAM roles in an account. This API requires valid AWS credentials with the necessary permissions to list IAM roles. An attacker can use this API to retrieve a list of IAM roles in an account and analyze the permissions granted to each role. This technique can also be performed using various AWS CLI commands.

Business Value: By discovering the IAM roles in an AWS account, an attacker can gain insight into the permissions granted to resources and potentially identify roles that can be abused to escalate privileges. This information can be used to plan further attacks and gain unauthorized access to sensitive data or resources.

## Requirements

1. Valid AWS credentials with permissions to list IAM roles

## Defense

1. Ensure that IAM roles are granted the least privilege necessary to perform their intended function

1. Monitor IAM role usage and permissions for suspicious activity

1. Use AWS CloudTrail to log and audit IAM role activity

## Objectives

1. Discover IAM roles in an AWS account

1. Identify permissions granted to each IAM role

1. Identify roles that can be abused to escalate privileges

# Instructions

1. To list all the IAM roles in your AWS account, run the following command:

**Code**: [[aws iam list-roles]]

> This command will return a list of all the IAM roles that have been created in your AWS account. IAM roles are used to delegate permissions to AWS services and resources, and are an important part of AWS security and access management. The output of this command will include the role name, the role ARN (Amazon Resource Name), and the role creation date.

**Command** ([[List IAM Roles]]):

```bash
aws iam list-roles
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List IAM Roles]]

## Tags

- [[3. Enumeratig Roles]]
- [[Cloud - AWS]]
- [[Listing IAM Roles]]
