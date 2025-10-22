---
id: 8d65ddeb-6c70-4de3-85c7-b1b08db82405
name: AWS IAM Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.267207+00:00'
updated_at: '2023-04-10T20:19:47.421419+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[4. Enumerating Policies]]'
- '[[Cloud - AWS]]'
- '[[Listing of IAM Policies]]'
commands:
- '[[List IAM Policies]]'
---

# AWS IAM Policy Enumeration

## Summary

AWS IAM Policy Enumeration is a technique used to identify the permissions granted to different AWS roles and users within an AWS account. By listing the IAM policies, an attacker can identify potential paths to escalate privileges and gain access to sensitive data. This technique is commonly used 

## Description

# Description

AWS IAM Policy Enumeration is a technique used to identify the permissions granted to different AWS roles and users within an AWS account. By listing the IAM policies, an attacker can identify potential paths to escalate privileges and gain access to sensitive data. This technique is commonly used in reconnaissance and initial access phases of an attack.

To perform this technique, an attacker would use the 'List AWS IAM Policies' command to obtain a list of all IAM policies in the target AWS account. The attacker can then analyze the policies to identify any overly permissive permissions or potential paths to escalate privileges.

The business value of this technique is that by identifying and addressing overly permissive IAM policies, organizations can reduce the risk of privilege escalation attacks and unauthorized access to sensitive data.

## Requirements

1. Valid AWS credentials with appropriate permissions

1. Access to the AWS console or AWS CLI

## Defense

1. Regularly review and update IAM policies to ensure they are not overly permissive

1. Use AWS CloudTrail to monitor and log all IAM policy changes

1. Implement multi-factor authentication (MFA) for all IAM users and roles

## Objectives

1. Identify IAM policies in the target AWS account

1. Identify overly permissive IAM policies

1. Identify potential paths to escalate privileges

# Instructions

1. This command lists all IAM policies in your AWS account.

**Code**: [[aws iam list-policies]]

> The `aws iam list-policies` command is used to retrieve a list of all IAM policies in your AWS account. This command does not require any arguments, as it retrieves all policies by default. However, you can use optional parameters to filter the results. For example, you can use `--scope` to filter by policy scope (AWS or Local), `--only-attached` to retrieve only attached policies, and `--path-prefix` to filter by policy path. The output of this command includes the policy name, ID, and ARN.

**Command** ([[List IAM Policies]]):

```bash
aws iam list-policies
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List IAM Policies]]

## Tags

- [[4. Enumerating Policies]]
- [[Cloud - AWS]]
- [[Listing of IAM Policies]]
