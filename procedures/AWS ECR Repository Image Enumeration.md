---
id: 047275eb-e913-495c-b52e-944c1387a2f8
name: AWS ECR Repository Image Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.591886+00:00'
updated_at: '2023-04-10T20:20:30.908750+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECR]]'
- '[[Enumeration]]'
- '[[Listing all images in a specific repository]]'
commands:
- '[[List ECR images]]'
---

# AWS ECR Repository Image Enumeration

## Summary

The AWS ECR Repository Image Enumeration procedure involves listing all images in a specific repository in order to gain a better understanding of the target environment. This procedure can be used to identify potential vulnerabilities in the images, or to discover additional repositories that may 

## Description

# Description

The AWS ECR Repository Image Enumeration procedure involves listing all images in a specific repository in order to gain a better understanding of the target environment. This procedure can be used to identify potential vulnerabilities in the images, or to discover additional repositories that may contain sensitive information. 

Technical Description: The AWS CLI command 'List ECR Repository Images' is used to list all images in a specified ECR repository. This command requires valid AWS credentials and access to the target ECR repository. 

Business Value: This procedure can help organizations identify potential security risks in their AWS environment and take appropriate steps to mitigate them.

## Requirements

1. Valid AWS credentials

1. Access to the target ECR repository

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Implement access controls to limit access to sensitive ECR repositories

1. Regularly monitor ECR repositories for unauthorized access or changes

## Objectives

1. Identify potential vulnerabilities in ECR repository images

1. Discover additional ECR repositories that may contain sensitive information

# Instructions

1. To list the images in an Amazon Elastic Container Registry (ECR) repository, use the following command:

The 'aws ecr list-images' command is used to list all the images in a specified ECR repository. The '--repository-name' option is used to specify the name of the repository. This command returns a list of image details, including the image digest, size, and push time. You can use this information to manage your ECR repository and its images.

**Command** ([[List ECR images]]):

```bash
aws ecr list-images --repository-name name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List ECR images]]

## Tags

- [[Cloud - AWS]]
- [[ECR]]
- [[Enumeration]]
- [[Listing all images in a specific repository]]
