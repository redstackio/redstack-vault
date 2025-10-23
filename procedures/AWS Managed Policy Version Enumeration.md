---
id: 55a170d6-a8d3-4429-a7b5-4396ae0a74af
name: AWS Managed Policy Version Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.343952+00:00'
updated_at: '2023-04-10T20:20:26.081272+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
tags:
- '[[4. Enumerating Policies]]'
- '[[Cloud - AWS]]'
- '[[Retrieving information about the specific version of the specified managed policy]]'
commands:
- '[[Get IAM Policy Version]]'
---

# AWS Managed Policy Version Enumeration

## Summary

AWS Managed Policy Version Enumeration is a technique used to gather information about the specific version of the specified managed policy. This technique can be used by an attacker to gain a better understanding of the permissions granted by the policy and to identify potential areas of weakness 

## Description

# Description

AWS Managed Policy Version Enumeration is a technique used to gather information about the specific version of the specified managed policy. This technique can be used by an attacker to gain a better understanding of the permissions granted by the policy and to identify potential areas of weakness within the policy. To retrieve the version information, the attacker can use the 'Retrieve IAM Policy Version' command. This command will return the policy version and the policy document for the specified policy.

 

## Requirements

1. Valid AWS credentials with IAM permissions

1. Access to the AWS console or CLI

1. Knowledge of the policy name and version to retrieve

 

## Defense

1. Regularly review and update policies to ensure they are granting the appropriate level of access

1. Implement the principle of least privilege to minimize the impact of a compromised policy

1. Enable AWS CloudTrail to monitor and log all API activity

 

## Objectives

1. Identify the version of a specific managed policy

1. Understand the permissions granted by the policy

1. Identify potential areas of weakness within the policy

 

# Instructions

1. To retrieve a specific version of an IAM policy, use the `aws iam get-policy-version` command.

 

This command requires the `policy-arn` and `version-id` arguments to specify which policy version to retrieve. The `policy-arn` argument is the Amazon Resource Name (ARN) of the policy you want to retrieve the version for. The `version-id` argument is the identifier for the version of the policy you want to retrieve. This command returns the policy version in JSON format.



**Command** ([[Get IAM Policy Version]]):

```bash
aws iam get-policy-version --policy-arn policy-arn --version-id version-id
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]

## Commands Used

- [[Get IAM Policy Version]]

## Tags

- [[4. Enumerating Policies]]
- [[Cloud - AWS]]
- [[Retrieving information about the specific version of the specified managed policy]]


