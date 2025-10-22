---
id: 3a361207-6eeb-4937-a163-8043d40ec9d6
name: AWS IAM Policy Information Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.739566+00:00'
updated_at: '2023-04-10T20:20:09.051857+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Accessing more credentials]]'
- '[[Cloud - AWS]]'
- '[[Persistence & Backdooring]]'
- '[[Retrieving information about an specific policy]]'
commands:
- '[[Get IAM policy]]'
---

# AWS IAM Policy Information Retrieval

## Summary

The AWS IAM Policy Information Retrieval procedure is used to retrieve information about a specific policy in an AWS environment. This procedure can be used by an attacker who has already gained access to an AWS environment and wants to gather more information about the policies that are in place. 

## Description

# Description

The AWS IAM Policy Information Retrieval procedure is used to retrieve information about a specific policy in an AWS environment. This procedure can be used by an attacker who has already gained access to an AWS environment and wants to gather more information about the policies that are in place. By understanding the policies, the attacker can better plan their next move and potentially escalate their privileges.

Technical: The attacker can use the 'Retrieve AWS IAM Policy' command to retrieve information about a specific policy. This command will return the policy document, which contains information about the permissions granted to the associated AWS resources. The attacker can then analyze this information to better understand the AWS environment and plan their next move.

Business Value: By understanding the policies in an AWS environment, an attacker can potentially escalate their privileges and gain access to more sensitive data. This can lead to data theft, data manipulation, and other malicious activities that can harm the business.

## Requirements

1. Access to an AWS environment

1. Valid credentials with appropriate permissions

1. Access to the 'Retrieve AWS IAM Policy' command

## Defense

1. Implement strict access controls and permissions for AWS resources

1. Monitor for unusual activity and unauthorized access to AWS resources

1. Regularly review and update AWS IAM policies to ensure they are up-to-date and secure

## Objectives

1. Retrieve information about a specific AWS IAM policy

1. Understand the permissions granted to associated AWS resources

1. Plan next steps for escalating privileges

# Instructions

1. To retrieve an AWS IAM policy, use the following command:

This command retrieves the policy document for the specified IAM policy ARN. The policy document contains the permissions that are granted to the policy. The ARN of the policy is required as an argument for the command.

**Command** ([[Get IAM policy]]):

```bash
aws iam get-policy --policy-arn ARN
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Get IAM policy]]

## Tags

- [[5. Exploitation Scenario]]
- [[Accessing more credentials]]
- [[Cloud - AWS]]
- [[Persistence & Backdooring]]
- [[Retrieving information about an specific policy]]
