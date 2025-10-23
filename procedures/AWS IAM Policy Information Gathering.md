---
id: d0328dbb-8175-4f32-8e91-d6260eb99b45
name: AWS IAM Policy Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.672409+00:00'
updated_at: '2023-04-10T20:20:38.936107+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Archive Collected Data|T1560 - Archive Collected Data]]'
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
tags:
- '[[Checking informations about a specific policy]]'
- '[[Cloud - AWS]]'
- '[[Persistence]]'
commands:
- '[[Retrieve IAM policy version]]'
---

# AWS IAM Policy Information Gathering

## Summary

The AWS IAM Policy Information Gathering procedure is used to retrieve information about a specific policy in an AWS account. This procedure can be used to gain insight into the permissions granted by a policy and identify potential areas for privilege escalation. The technique involves retrieving 

## Description

# Description

The AWS IAM Policy Information Gathering procedure is used to retrieve information about a specific policy in an AWS account. This procedure can be used to gain insight into the permissions granted by a policy and identify potential areas for privilege escalation. The technique involves retrieving the version of the policy using the 'Retrieve IAM Policy Version' command and analyzing the policy document to identify the permissions granted. This procedure can be used by attackers to gather intelligence on an AWS environment and identify potential targets for further exploitation.

From a technical perspective, this procedure involves making a call to the AWS API to retrieve the specified policy document. The policy document is then analyzed to identify the permissions granted by the policy. From a business perspective, this procedure can help identify potential areas of risk in an AWS environment and inform security teams of areas that may require additional attention.

 

## Requirements

1. Valid AWS credentials with appropriate permissions

1. Access to the AWS API

1. AWS CLI or SDK installed

 

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Monitor AWS CloudTrail logs for suspicious activity related to IAM policies

1. Implement the principle of least privilege by only granting the necessary permissions to IAM policies

 

## Objectives

1. Retrieve information about a specific policy in an AWS account

1. Identify potential areas for privilege escalation

1. Gather intelligence on an AWS environment

 

# Instructions

1. To retrieve a specific version of an IAM policy, use the 'aws iam get-policy-version' command.

 

This command requires two arguments: 'policy-arn' (the Amazon Resource Name (ARN) of the policy) and 'version-id' (the policy version to retrieve). The command will return the policy version specified by the 'version-id' argument. If the version is not found, an error message will be returned. This command can be useful for auditing and tracking changes to IAM policies over time.



**Command** ([[Retrieve IAM policy version]]):

```bash
aws iam get-policy-version --policy-arn arn --version-id ID
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Archive Collected Data|T1560 - Archive Collected Data]]
- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]

## Commands Used

- [[Retrieve IAM policy version]]

## Tags

- [[Checking informations about a specific policy]]
- [[Cloud - AWS]]
- [[Persistence]]


