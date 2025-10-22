---
id: 469ce460-c32b-40ef-a201-0fff1e324c24
name: AWS User Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.236626+00:00'
updated_at: '2023-04-10T20:20:29.222270+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Exfiltration]]'
- '[[Listing policies attached to an user]]'
commands:
- '[[List Attached User Policies]]'
---

# AWS User Policy Enumeration

## Summary

AWS User Policy Enumeration is a technique used by attackers to gather information about the permissions assigned to a specific AWS user. AWS IAM (Identity and Access Management) is a service that enables users to manage access to AWS resources. By listing the policies attached to an IAM user, atta

## Description

# Description

AWS User Policy Enumeration is a technique used by attackers to gather information about the permissions assigned to a specific AWS user. AWS IAM (Identity and Access Management) is a service that enables users to manage access to AWS resources. By listing the policies attached to an IAM user, attackers can identify which resources the user has access to and potentially escalate privileges. This technique can be used as part of a larger credential exfiltration attack.

To perform this technique, an attacker needs to have valid AWS credentials and access to the AWS Management Console or AWS CLI. By listing the policies attached to an IAM user, the attacker can gain insight into the level of access granted to the user and identify potential targets for further exploitation. This technique can be used to identify high-value targets or to gather information for lateral movement.

## Requirements

1. Valid AWS credentials

1. Access to the AWS Management Console or AWS CLI

## Defense

1. Implement the principle of least privilege for AWS IAM users

1. Monitor and log all IAM activity

1. Enable multi-factor authentication (MFA) for AWS IAM users

## Objectives

1. Identify the permissions assigned to a specific AWS user

1. Identify potential targets for further exploitation

1. Gather information for lateral movement

# Instructions

1. Use this command to list all the policies attached to a specific IAM user.

The 'aws iam list-attached-user-policies' command is used to list all the policies that are attached to a specific IAM user. The command takes one argument, which is the name of the user whose attached policies you want to list. Once you run the command, it will return a JSON object that contains information about the policies attached to the specified user, including the policy name, policy ARN, and the name of the user to which the policy is attached.

**Command** ([[List Attached User Policies]]):

```bash
aws iam list-attached-user-policies --user-name name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]

## Commands Used

- [[List Attached User Policies]]

## Tags

- [[Cloud - AWS]]
- [[Credential Exfiltration]]
- [[Listing policies attached to an user]]
