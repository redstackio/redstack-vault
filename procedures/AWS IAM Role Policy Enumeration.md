---
id: 69758664-7766-4ad2-a8b1-cd62527e7c5c
name: AWS IAM Role Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.219518+00:00'
updated_at: '2023-04-10T20:19:47.011470+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[3. Enumerating Roles]]'
- '[[Cloud - AWS]]'
- '[[Listing all managed policies that are attached to the specified IAM role]]'
commands:
- '[[List Attached Role Policies]]'
---

# AWS IAM Role Policy Enumeration

## Summary

The AWS IAM Role Policy Enumeration procedure involves listing all managed policies that are attached to a specific IAM role. This technique can be used by an attacker to gather information about the permissions granted to a specific role, which can help them to identify potential attack paths and 

## Description

# Description

The AWS IAM Role Policy Enumeration procedure involves listing all managed policies that are attached to a specific IAM role. This technique can be used by an attacker to gather information about the permissions granted to a specific role, which can help them to identify potential attack paths and targets within the AWS environment. To perform this procedure, the attacker needs to have valid AWS credentials with the necessary permissions to access IAM services.

 

## Requirements

1. Valid AWS credentials with the necessary permissions to access IAM services

 

## Defense

1. Ensure that IAM roles have the least privilege necessary to perform their intended function

1. Monitor IAM role activity and review policies regularly to ensure they are up to date and accurate

1. Implement multi-factor authentication and strong password policies to protect AWS credentials

 

## Objectives

1. To gather information about the permissions granted to a specific IAM role

1. To identify potential attack paths and targets within the AWS environment

 

# Instructions

1. To list the attached policies for a specific IAM role, use the following command:

 

The 'aws iam list-attached-role-policies' command is used to list all the policies that are attached to a specific IAM role. This command requires the name of the IAM role as an argument. The output of this command will include the policy name, policy ARN, and the policy attachment date. This command can be useful when you need to review the policies that are attached to a role or when you need to remove a policy from a role.



**Command** ([[List Attached Role Policies]]):

```bash
aws iam list-attached-role-policies --role-name role-name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Attached Role Policies]]

## Tags

- [[3. Enumerating Roles]]
- [[Cloud - AWS]]
- [[Listing all managed policies that are attached to the specified IAM role]]


