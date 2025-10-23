---
id: 4f97ebd4-9e5c-4546-b210-e4885b850a41
name: AWS IAM User Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.062479+00:00'
updated_at: '2023-04-10T20:20:25.735729+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[1. Enumerating IAM users]]'
- '[[Cloud - AWS]]'
- '[[Listing all manages policies that are attached to the specified IAM user]]'
commands:
- '[[List Attached User Policies]]'
---

# AWS IAM User Policy Enumeration

## Summary

AWS Identity and Access Management (IAM) is a powerful service that enables you to manage access to AWS resources. This procedure focuses on enumerating the managed policies that are attached to a specified IAM user. By doing so, an attacker can gain insight into the level of access granted to that

## Description

# Description

AWS Identity and Access Management (IAM) is a powerful service that enables you to manage access to AWS resources. This procedure focuses on enumerating the managed policies that are attached to a specified IAM user. By doing so, an attacker can gain insight into the level of access granted to that user and potentially identify other users with similar access. This procedure is typically used during the reconnaissance phase of an attack to gather intelligence on potential targets.

Technical Explanation: This procedure uses the AWS CLI command 'ListAttachedUserPolicies' to enumerate the managed policies that are attached to a specified IAM user.

Business Value: This procedure can be used by security teams to identify potential security risks and ensure that users are only granted the access they need to perform their job functions.

 

## Requirements

1. Valid AWS credentials with permissions to access IAM

1. Access to the AWS CLI

 

## Defense

1. Ensure that IAM users are only granted the access they need to perform their job functions

1. Implement the principle of least privilege to limit the potential impact of a compromised user

1. Monitor IAM activity for suspicious behavior

 

## Objectives

1. Enumerate the managed policies attached to a specified IAM user

1. Identify the level of access granted to the user

1. Gather intelligence on potential targets

 

# Instructions

1. Use this command to list all the policies that are attached to a specific IAM user.

 

The 'aws iam list-attached-user-policies' command is used to retrieve a list of policies that are attached to a specific IAM user. The '--user-name' argument is used to specify the name of the user whose attached policies you want to list. This command returns a JSON object that contains information about the policies that are attached to the specified user, including the policy name, policy ARN, and the name of the user to which the policy is attached. This command is useful for managing user permissions and understanding the access that users have to AWS resources.



**Command** ([[List Attached User Policies]]):

```bash
aws iam list-attached-user-policies --user-name user-name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Attached User Policies]]

## Tags

- [[1. Enumerating IAM users]]
- [[Cloud - AWS]]
- [[Listing all manages policies that are attached to the specified IAM user]]


