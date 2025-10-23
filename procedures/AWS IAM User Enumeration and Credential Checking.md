---
id: 8d633a6e-77ad-42da-9579-f8f57def9004
name: AWS IAM User Enumeration and Credential Checking
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.983289+00:00'
updated_at: '2023-04-10T20:19:45.955007+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
tags:
- '[[1. Enumerating IAM users]]'
- '[[Checking credentials for the user]]'
- '[[Cloud - AWS]]'
commands:
- '[[AWS STS Get Caller Identity]]'
---

# AWS IAM User Enumeration and Credential Checking

## Summary

This procedure involves enumerating the AWS Identity and Access Management (IAM) users and checking their credentials. This can be used by an attacker to gain access to sensitive data or resources within an AWS environment. The attacker can use the 'Get AWS Caller Identity' command to obtain the cu

## Description

# Description

This procedure involves enumerating the AWS Identity and Access Management (IAM) users and checking their credentials. This can be used by an attacker to gain access to sensitive data or resources within an AWS environment. The attacker can use the 'Get AWS Caller Identity' command to obtain the current user's identity and determine the level of access they have. The attacker can then use this information to attempt to escalate their privileges or access sensitive data.

From a technical standpoint, this procedure involves using the 'Get AWS Caller Identity' command to obtain the current user's identity. The attacker can then use this information to attempt to access other resources within the environment. The business value of this procedure is that it can help an attacker gain access to sensitive data or resources within an AWS environment.



 

## Requirements

1. Valid AWS credentials

 

## Defense

1. Ensure that IAM users have appropriate permissions and access controls in place

1. Implement multi-factor authentication (MFA) for IAM users

1. Monitor AWS CloudTrail logs for unusual activity

 

## Objectives

1. Enumerate IAM users within an AWS environment

1. Check the credentials of IAM users

1. Gain access to sensitive data or resources within an AWS environment

 

# Instructions

1. Use this command to retrieve the AWS account ID and the Amazon Resource Name (ARN) of the IAM user or role whose credentials are used to call the API.

 



**Code**: [[aws sts get-caller-identity]]



> The 'aws sts get-caller-identity' command is used to retrieve the AWS account ID and the Amazon Resource Name (ARN) of the IAM user or role whose credentials are used to call the API. This command does not require any arguments to be passed. It is useful in scenarios where you need to verify the identity of the user or role that is calling the API. The output of this command contains the AWS account ID and the ARN of the IAM user or role. The AWS account ID can be used in various other AWS commands to perform actions specific to that account. The ARN can be used to uniquely identify the user or role and can be used in various other AWS commands to perform actions specific to that user or role.



**Command** ([[AWS STS Get Caller Identity]]):

```bash
aws sts get-caller-identity
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]

## Commands Used

- [[AWS STS Get Caller Identity]]

## Tags

- [[1. Enumerating IAM users]]
- [[Checking credentials for the user]]
- [[Cloud - AWS]]


