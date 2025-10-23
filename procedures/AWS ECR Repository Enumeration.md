---
id: d4c5bebe-3612-4705-9418-75032b8a7d13
name: AWS ECR Repository Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.533403+00:00'
updated_at: '2023-04-10T20:19:57.949584+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECR]]'
- '[[Enumeration]]'
- '[[Listing all repositories in container registry]]'
commands:
- '[[List ECR Repositories]]'
---

# AWS ECR Repository Enumeration

## Summary

The AWS ECR Repository Enumeration procedure involves listing all the repositories in an AWS Elastic Container Registry (ECR) using the 'ECR Repository Details' command. This procedure can be used by an attacker to gain an understanding of the container images available in the ECR, which can be use

## Description

# Description

The AWS ECR Repository Enumeration procedure involves listing all the repositories in an AWS Elastic Container Registry (ECR) using the 'ECR Repository Details' command. This procedure can be used by an attacker to gain an understanding of the container images available in the ECR, which can be useful for further attacks. 

Technical Description: The procedure uses the 'ECR Repository Details' command to list all the repositories available in the ECR. The command requires AWS authentication credentials to be provided. The output of the command includes the repository name, URI, creation date, and the number of images in the repository. 

Business Value: An attacker can use this procedure to identify valuable container images that can be used for further attacks, such as running malicious code or exfiltrating data from the container.

 

## Requirements

1. Valid AWS authentication credentials.

 

## Defense

1. Ensure that AWS authentication credentials are kept secure and not shared.

1. Implement least privilege access controls to limit access to the ECR.

1. Monitor ECR activity using AWS CloudTrail logs.

 

## Objectives

1. List all the repositories in an AWS ECR.

1. Identify valuable container images for further attacks.

 

# Instructions

1. This command is used to retrieve details of all the repositories in Amazon Elastic Container Registry (ECR).

 

The 'aws ecr describe-repositories' command is used to list all the available repositories in ECR. This command does not require any arguments. It returns a JSON object containing the details of all the repositories such as repository name, ARN, creation date, and more. This information can be useful to get an overview of all the available repositories in ECR and to choose the appropriate repository for your container images. 



**Command** ([[List ECR Repositories]]):

```bash
aws ecr describe-repositories
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[List ECR Repositories]]

## Tags

- [[Cloud - AWS]]
- [[ECR]]
- [[Enumeration]]
- [[Listing all repositories in container registry]]


