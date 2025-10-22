---
id: a2a13e91-7aa1-4d67-bfdc-398daf969b89
name: AWS ECR Repository Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.561780+00:00'
updated_at: '2023-04-10T20:20:34.870840+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Disabling Security Tools|T1089 - Disabling Security Tools]]'
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
sub_techniques:
- '[[Password Filter DLL|T1556.002 - Password Filter DLL]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECR]]'
- '[[Enumeration]]'
- '[[Listing information about repository policy]]'
commands:
- '[[Get ECR Repository Policy]]'
---

# AWS ECR Repository Policy Enumeration

## Summary

The AWS Elastic Container Registry (ECR) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. ECR Get Repository Policy command is used to list the JSON policy associated with a specified repository. An attacker can use

## Description

# Description

The AWS Elastic Container Registry (ECR) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. ECR Get Repository Policy command is used to list the JSON policy associated with a specified repository. An attacker can use this command to discover what permissions are granted to different AWS entities, such as users, roles or accounts. This information can be used to further the attacker's objectives, such as lateral movement or privilege escalation.

Technical Description: The ECR Get Repository Policy command is part of the AWS CLI and can be used to retrieve the JSON policy associated with a specified repository. The policy lists the permissions granted to different AWS entities, such as users, roles or accounts. An attacker can use this information to further their objectives, such as lateral movement or privilege escalation.

Business Value: An attacker with access to an AWS account can use this technique to gain a better understanding of the account's infrastructure and permissions. This information can be used to plan and execute further attacks, such as lateral movement or privilege escalation.

## Requirements

1. Valid AWS credentials with permission to execute the ECR Get Repository Policy command

## Defense

1. Limit the use of AWS credentials with the minimum required permissions

1. Monitor for unusual ECR repository policy changes

1. Implement network segmentation to limit lateral movement within the AWS environment

## Objectives

1. Discover AWS permissions associated with a specified ECR repository

1. Identify potential paths for lateral movement or privilege escalation

# Instructions

1. Use this command to retrieve the resource policy for a specified repository in Amazon Elastic Container Registry (ECR).

This command takes the repository name as an argument and returns the JSON-formatted resource policy for the specified repository. The resource policy controls who can access the repository and what actions they can perform. The policy can be used to grant permissions to specific users or roles, or to restrict access to a specific IP address range. The policy can also be used to enforce encryption requirements or to specify which Amazon S3 bucket should be used for storing images.

**Command** ([[Get ECR Repository Policy]]):

```bash
aws ecr get-repository-policy --repository-name name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Disabling Security Tools|T1089 - Disabling Security Tools]]
- [[Modify Authentication Process|T1556 - Modify Authentication Process]]

### Sub-Techniques

- [[Password Filter DLL|T1556.002 - Password Filter DLL]]

## Commands Used

- [[Get ECR Repository Policy]]

## Tags

- [[Cloud - AWS]]
- [[ECR]]
- [[Enumeration]]
- [[Listing information about repository policy]]
