---
id: 733dff2c-6ee8-48e7-b984-5cbf83d47655
name: AWS IAM Policy Version Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.763400+00:00'
updated_at: '2023-04-10T20:20:26.792790+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Accessing more credentials]]'
- '[[Cloud - AWS]]'
- '[[Listing information about the version of the policy]]'
- '[[Persistence & Backdooring]]'
commands:
- '[[List IAM Policy Versions]]'
---

# AWS IAM Policy Version Enumeration

## Summary

The AWS IAM Policy Version Enumeration procedure is used to discover information about the policy versions in use. This can be used to identify potential vulnerabilities and weaknesses in the system. By listing the policy versions, an attacker can determine if they are outdated or have known vulner

## Description

# Description

The AWS IAM Policy Version Enumeration procedure is used to discover information about the policy versions in use. This can be used to identify potential vulnerabilities and weaknesses in the system. By listing the policy versions, an attacker can determine if they are outdated or have known vulnerabilities. This procedure can also be used to identify the permissions granted to different users or roles.

To execute this procedure, the attacker uses the 'List IAM Policy Versions' command. This command returns a list of the policy versions and their creation dates.

The business value of this procedure is that it helps organizations identify potential security risks in their AWS environment and take appropriate action to mitigate them.

## Requirements

1. Valid AWS credentials with IAM permissions

## Defense

1. Regularly review and update the AWS policies to ensure they are up-to-date and secure

1. Implement multi-factor authentication to reduce the risk of unauthorized access to AWS resources

1. Monitor AWS logs and alerts for suspicious activity

## Objectives

1. Discover information about the policy versions in use

1. Identify potential vulnerabilities and weaknesses in the system

1. Identify the permissions granted to different users or roles

# Instructions

1. Use this command to list all the versions of an IAM policy.

The 'aws iam list-policy-versions' command lists all the versions of an IAM policy. The command requires the Amazon Resource Name (ARN) of the policy as an argument. The output of the command includes the version number, create date, and whether the version is the default version. This command is useful when you need to view the different versions of a policy and compare them to each other. You can also use this command to determine which version of a policy is currently set as the default version.

**Command** ([[List IAM Policy Versions]]):

```bash
aws iam list-policy-versions --policy-arn ARN
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List IAM Policy Versions]]

## Tags

- [[5. Exploitation Scenario]]
- [[Accessing more credentials]]
- [[Cloud - AWS]]
- [[Listing information about the version of the policy]]
- [[Persistence & Backdooring]]
