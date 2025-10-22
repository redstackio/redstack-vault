---
id: 61abeaec-a73b-4449-960b-f6875ca66278
name: AWS Account Identity Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.435351+00:00'
updated_at: '2023-04-10T20:20:47.783645+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Getting information about the key]]'
- '[[Privilege Escalation]]'
commands:
- '[[AWS STS Get Caller Identity]]'
---

# AWS Account Identity Enumeration

## Summary

The AWS Account Identity Enumeration procedure is used to obtain information about the AWS account identity, such as the AWS account ID, which is a crucial piece of information for an attacker. An attacker can use this information to launch further attacks such as privilege escalation, lateral move

## Description

# Description

The AWS Account Identity Enumeration procedure is used to obtain information about the AWS account identity, such as the AWS account ID, which is a crucial piece of information for an attacker. An attacker can use this information to launch further attacks such as privilege escalation, lateral movement, or data exfiltration. This procedure is performed by using the 'Get AWS Account Identity' command to obtain the AWS account ID.

## Requirements

1. Valid AWS credentials with permissions to call the 'Get AWS Account Identity' API

1. Access to the AWS Management Console or AWS CLI

## Defense

1. Ensure that AWS credentials are properly secured and rotated regularly

1. Enable multi-factor authentication (MFA) for AWS accounts to prevent unauthorized access

1. Monitor AWS CloudTrail logs for suspicious activity and unauthorized API calls

## Objectives

1. Obtain the AWS account ID

1. Identify potential vulnerabilities or misconfigurations in the AWS account

1. Use the obtained information for further attacks

# Instructions

1. The 'aws sts get-caller-identity' command is used to retrieve the details of the AWS account that is associated with the current IAM user or role. It returns the AWS account ID, the Amazon Resource Name (ARN) of the IAM entity making the request, and the AWS partition that the account is in.

**Code**: [[aws sts get-caller-identity]]

> The command does not require any arguments or options. Simply run the command and it will return the details of the AWS account associated with the current IAM user or role. This command is useful for verifying the identity of the user or role that is currently making requests to AWS services.

**Command** ([[AWS STS Get Caller Identity]]):

```bash
aws sts get-caller-identity
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[AWS STS Get Caller Identity]]

## Tags

- [[Cloud - AWS]]
- [[Exploitation]]
- [[Getting information about the key]]
- [[Privilege Escalation]]
