---
id: 42de6dfd-2301-45b7-98d2-33f554cc9932
name: AWS IAM Group Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.115704+00:00'
updated_at: '2023-04-10T20:19:46.316605+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
tags:
- '[[2. Enumerating Groups IAM]]'
- '[[Cloud - AWS]]'
- '[[Listing IAM Groups]]'
commands:
- '[[List IAM Groups]]'
---

# AWS IAM Group Enumeration

## Summary

AWS IAM Group Enumeration is a technique used by attackers to discover the IAM groups in an AWS account. By listing the IAM groups, an attacker can gain a better understanding of the account's permissions and potentially identify high-value targets. To perform this technique, the attacker uses the 

## Description

# Description

AWS IAM Group Enumeration is a technique used by attackers to discover the IAM groups in an AWS account. By listing the IAM groups, an attacker can gain a better understanding of the account's permissions and potentially identify high-value targets. To perform this technique, the attacker uses the 'List AWS IAM Groups' command to retrieve a list of all IAM groups in the account. This information can be used to plan further attacks against the account.

From a technical perspective, this technique involves making API calls to the AWS IAM service. The attacker must have valid AWS API credentials to perform this technique. 

The business value of this technique is that it allows an attacker to identify high-value targets in an AWS account. By knowing which IAM groups have elevated permissions, the attacker can focus their efforts on compromising those groups and gaining access to sensitive data or resources.

## Requirements

1. Valid AWS API credentials

## Defense

1. Ensure that AWS API credentials are properly secured and rotated regularly

1. Implement least privilege access for IAM groups to limit the impact of a potential compromise

1. Monitor for suspicious API activity, such as repeated calls to the 'List AWS IAM Groups' command

## Objectives

1. Identify IAM groups in an AWS account

1. Gain a better understanding of the account's permissions

1. Identify high-value targets in the account

# Instructions

1. This command lists all the IAM groups present in your AWS account.

**Code**: [[aws iam list-groups]]

> The 'aws iam list-groups' command is used to list all the IAM groups present in your AWS account. This command does not require any arguments. It will return a JSON object that contains the details of all the groups in your account, including their names, ARNs, and creation dates. You can use this command to quickly get an overview of the IAM groups in your account and their properties.

**Command** ([[List IAM Groups]]):

```bash
aws iam list-groups
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

## Commands Used

- [[List IAM Groups]]

## Tags

- [[2. Enumerating Groups IAM]]
- [[Cloud - AWS]]
- [[Listing IAM Groups]]
