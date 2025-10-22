---
id: c1d206ae-038d-4990-8cdc-74b8ddf8cd5f
name: AWS IAM User Inline Policies Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.089333+00:00'
updated_at: '2023-04-10T20:20:04.453431+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
sub_techniques:
- '[[Domain Groups|T1069.002 - Domain Groups]]'
tags:
- '[[1. Enumerating IAM users]]'
- '[[Cloud - AWS]]'
- '[[Listing the names of the inline policies embedded in the specified IAM user]]'
commands:
- '[[List user policies for IAM user]]'
---

# AWS IAM User Inline Policies Enumeration

## Summary

This procedure focuses on identifying the inline policies embedded in a specified IAM user in AWS. An attacker can use this information to gain a better understanding of the permissions of the user and potentially identify areas of weakness. To accomplish this, the 'List User Policies' command is u

## Description

# Description

This procedure focuses on identifying the inline policies embedded in a specified IAM user in AWS. An attacker can use this information to gain a better understanding of the permissions of the user and potentially identify areas of weakness. To accomplish this, the 'List User Policies' command is used to list the names of the inline policies associated with the specified IAM user. This information can be used in conjunction with other procedures to further enumerate the permissions of the user and potentially escalate privileges.

From a technical perspective, this procedure involves making a request to the AWS API using the 'List User Policies' command. The response will contain a list of the names of the inline policies associated with the specified IAM user.

The business value of this procedure is that it allows an organization to identify potential weaknesses in their IAM policies and take steps to remediate them before an attacker can exploit them.

## Requirements

1. Valid AWS credentials with permission to access the 'List User Policies' command

1. Access to the AWS API

## Defense

1. Ensure that IAM policies are properly configured to limit the permissions of users to only what they need to perform their job functions

1. Implement multi-factor authentication for AWS accounts to prevent unauthorized access

1. Monitor AWS API activity for suspicious behavior

## Objectives

1. Identify the inline policies embedded in a specified IAM user in AWS

1. Enumerate the permissions of the specified IAM user

1. Identify potential areas of weakness in the IAM policies

# Instructions

1. Use this command to list all the managed policies that are attached to the specified IAM user.

The 'aws iam list-user-policies' command is used to retrieve a list of all the managed policies that are attached to the specified IAM user. The command requires the 'user-name' argument to be specified, which is the name of the IAM user for which you want to list the policies. The output of the command will be a JSON-formatted list of policy names, which can be used as input to other IAM commands that require policy names as arguments. If the specified user does not exist, the command will return an error. 

**Command** ([[List user policies for IAM user]]):

```bash
aws iam list-user-policies --user-name user-name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

### Sub-Techniques

- [[Domain Groups|T1069.002 - Domain Groups]]

## Commands Used

- [[List user policies for IAM user]]

## Tags

- [[1. Enumerating IAM users]]
- [[Cloud - AWS]]
- [[Listing the names of the inline policies embedded in the specified IAM user]]
