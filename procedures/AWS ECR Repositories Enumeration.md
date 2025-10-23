---
id: 0aa57016-c479-4802-afa2-a26920935263
name: AWS ECR Repositories Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.049939+00:00'
updated_at: '2023-04-10T20:20:18.734154+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Getting information about the repositories in container registry]]'
- '[[Persistence]]'
commands:
- '[[List ECR Repositories]]'
---

# AWS ECR Repositories Enumeration

## Summary

The AWS Elastic Container Registry (ECR) is a managed container registry service that is used to store, manage, and deploy Docker container images. As a cloud service, ECR is a potential target for attackers seeking to gain access to sensitive information or to disrupt operations. This procedure in

## Description

# Description

The AWS Elastic Container Registry (ECR) is a managed container registry service that is used to store, manage, and deploy Docker container images. As a cloud service, ECR is a potential target for attackers seeking to gain access to sensitive information or to disrupt operations. This procedure involves getting information about the repositories in a container registry using the 'ECR Repositories Description' command. This command returns details about the specified repositories within an ECR registry, including their names, ARNs, and creation dates.

From an offensive perspective, this procedure can help an attacker identify sensitive repositories that may contain valuable data or code. From a defensive perspective, this procedure can be used by security teams to monitor for any unauthorized access or changes to ECR repositories.

 

## Requirements

1. Valid AWS credentials with permission to access ECR

1. Network access to the ECR service

 

## Defense

1. Ensure that AWS credentials are securely stored and not shared

1. Enable MFA for AWS accounts to prevent unauthorized access

1. Monitor ECR activity logs for any suspicious activity

 

## Objectives

1. Identify sensitive ECR repositories

1. Monitor for unauthorized access or changes to ECR repositories

 

# Instructions

1. This command is used to describe the repositories in the Amazon Elastic Container Registry (ECR).

 

The 'aws ecr describe-repositories' command is used to retrieve information about the ECR repositories in your AWS account. It returns a JSON object that contains details such as the repository name, registry ID, creation date, and the number of images in the repository. This command can be useful for managing your ECR repositories, such as checking if a repository exists or retrieving the number of images in a repository. Arguments are not required for this command.



**Command** ([[List ECR Repositories]]):

```bash
aws ecr describe-repositories
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List ECR Repositories]]

## Tags

- [[Cloud - AWS]]
- [[Getting information about the repositories in container registry]]
- [[Persistence]]


