---
id: 62f3b5d9-da4b-4475-87c8-50720973f7df
name: AWS IAM Group Inline Policies Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.166554+00:00'
updated_at: '2023-04-10T20:20:11.138213+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[2. Enumerating Groups IAM]]'
- '[[Cloud - AWS]]'
- '[[Listing the names of the inline policies embedded in the specified IAM Group]]'
commands:
- '[[List IAM Group Policies]]'
---

# AWS IAM Group Inline Policies Enumeration

## Summary

The AWS Identity and Access Management (IAM) service is used to manage access to AWS resources. IAM Groups are a way to group IAM users and apply policies to them collectively. This procedure enables an attacker to enumerate the inline policies attached to a specified IAM group. By enumerating the 

## Description

# Description

The AWS Identity and Access Management (IAM) service is used to manage access to AWS resources. IAM Groups are a way to group IAM users and apply policies to them collectively. This procedure enables an attacker to enumerate the inline policies attached to a specified IAM group. By enumerating the inline policies, the attacker can gain a better understanding of the permissions assigned to the IAM group and potentially identify privilege escalation opportunities.

To list the names of the inline policies embedded in the specified IAM group, the attacker would use the 'List Group Policies' command. This will return the names of the inline policies associated with the IAM group.

## Requirements

1. Valid AWS credentials with IAM permissions

## Defense

1. Ensure that IAM permissions are properly configured and that users are only granted the permissions they require

1. Monitor IAM activity logs for suspicious activity

1. Implement multi-factor authentication (MFA) for IAM users to prevent unauthorized access

## Objectives

1. Enumerate the inline policies attached to a specified IAM group

1. Identify potential privilege escalation opportunities

# Instructions

1. Use the following AWS CLI command to list all policies attached to a specific IAM group:

This command will list the names of all policies attached to the specified IAM group. The policies can then be further examined to determine their permissions and access levels. The --group-name flag should be replaced with the name of the IAM group that you want to list the policies for.

**Command** ([[List IAM Group Policies]]):

```bash
aws iam list-group-policies --group-name group name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List IAM Group Policies]]

## Tags

- [[2. Enumerating Groups IAM]]
- [[Cloud - AWS]]
- [[Listing the names of the inline policies embedded in the specified IAM Group]]
