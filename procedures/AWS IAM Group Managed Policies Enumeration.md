---
id: 86b36d12-a435-45c5-8618-b46b95af71cb
name: AWS IAM Group Managed Policies Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.139389+00:00'
updated_at: '2023-04-10T20:19:46.663635+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Application Access Token|T1527 - Application Access Token]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[2. Enumerating Groups IAM]]'
- '[[Cloud - AWS]]'
- '[[Listing all managed policies that are attached to the specified IAM Group]]'
commands:
- '[[List Attached Group Policies]]'
---

# AWS IAM Group Managed Policies Enumeration

## Summary

The AWS Identity and Access Management (IAM) service enables you to manage access to AWS services and resources securely. One of the key features of IAM is the ability to create and manage IAM groups that contain IAM users. This procedure focuses on enumerating all managed policies that are attache

## Description

# Description

The AWS Identity and Access Management (IAM) service enables you to manage access to AWS services and resources securely. One of the key features of IAM is the ability to create and manage IAM groups that contain IAM users. This procedure focuses on enumerating all managed policies that are attached to a specified IAM group. An attacker could use this procedure to identify permissions that are granted to a specific group of users, and potentially use this information to escalate privileges or perform lateral movement within the target environment.

To execute this procedure, the user needs to have valid AWS credentials with permissions to call the ListAttachedGroupPolicies API. The procedure returns a list of managed policies that are attached to the specified IAM group.

## Requirements

1. Valid AWS credentials with permissions to call the ListAttachedGroupPolicies API

## Defense

1. Ensure that users have the minimum necessary permissions to access AWS resources

1. Implement access controls to limit who can modify IAM groups and policies

1. Monitor IAM activity logs for suspicious activity

## Objectives

1. Identify all managed policies that are attached to a specific IAM group

1. Understand the permissions granted to the members of the IAM group

1. Identify potential privilege escalation paths within the target environment

# Instructions

1. To list the attached policies of a specific group in AWS Identity and Access Management (IAM), use the following command:

This command will list all the policies that are attached to the specified IAM group. The --group-name parameter is used to specify the name of the group for which you want to list the attached policies. If successful, the command will return a JSON object containing the details of each attached policy, including the policy name, policy ARN, and the name of the attached entity (in this case, the group name).

**Command** ([[List Attached Group Policies]]):

```bash
aws iam list-attached-group-policies --group-name group-name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Application Access Token|T1527 - Application Access Token]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Attached Group Policies]]

## Tags

- [[2. Enumerating Groups IAM]]
- [[Cloud - AWS]]
- [[Listing all managed policies that are attached to the specified IAM Group]]
