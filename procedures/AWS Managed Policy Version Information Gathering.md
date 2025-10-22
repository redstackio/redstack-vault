---
id: e5179d86-a4d9-4aaf-900f-91e68e7344fa
name: AWS Managed Policy Version Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.027273+00:00'
updated_at: '2023-04-10T20:20:35.200603+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Getting information about the version of the managed policy]]'
- '[[Persistence]]'
commands:
- '[[Get IAM policy version]]'
---

# AWS Managed Policy Version Information Gathering

## Summary

The AWS Managed Policy Version Information Gathering procedure involves retrieving information about the version of a managed policy in AWS Identity and Access Management (IAM). This information can be used to determine if a policy has been updated or if a specific version of a policy is being used

## Description

# Description

The AWS Managed Policy Version Information Gathering procedure involves retrieving information about the version of a managed policy in AWS Identity and Access Management (IAM). This information can be used to determine if a policy has been updated or if a specific version of a policy is being used. An attacker could use this information to identify potential vulnerabilities in the policy and plan their attack accordingly.

To retrieve the version of a managed policy, the attacker would use the 'Retrieve IAM Policy Version' command. This command will return the version number of the specified policy. This information can be used to determine if the policy has been updated or if a specific version of the policy is being used. 

This procedure can be used by attackers to gather information about the target's AWS environment, which could be used to plan future attacks.

## Requirements

1. Access to the AWS IAM console or API

1. Valid AWS IAM credentials

## Defense

1. Regularly review and update managed policies to ensure they are up-to-date and secure

1. Enable logging and monitoring of AWS IAM activity to detect and respond to suspicious behavior

1. Implement strong authentication and access controls for AWS IAM accounts to prevent unauthorized access

## Objectives

1. Retrieve the version of a managed policy in AWS IAM

1. Identify potential vulnerabilities in the policy

1. Plan future attacks based on the retrieved information

# Instructions

1. To retrieve a specific version of an IAM policy, use the 'aws iam get-policy-version' command.

This command requires the policy ARN and version ID as arguments. The ARN uniquely identifies the policy, while the version ID specifies the particular version to retrieve. The command returns the policy version details in JSON format.

**Command** ([[Get IAM policy version]]):

```bash
aws iam get-policy-version --policy-arn arn --version-id id
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get IAM policy version]]

## Tags

- [[Cloud - AWS]]
- [[Getting information about the version of the managed policy]]
- [[Persistence]]
