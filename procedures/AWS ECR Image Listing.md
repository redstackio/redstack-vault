---
id: 1b17d7a5-3f28-4fc6-b02b-d326f1a64feb
name: AWS ECR Image Listing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.617909+00:00'
updated_at: '2023-04-10T20:20:42.049170+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[ECR]]'
- '[[Enumeration]]'
- '[[Listing information about an image]]'
commands:
- '[[Describe ECR image]]'
---

# AWS ECR Image Listing

## Summary

The AWS ECR Image Listing procedure involves enumerating information about an image within an Amazon Elastic Container Registry (ECR). This can be useful for an attacker who is trying to gain a better understanding of the target environment, particularly in the case of containerized applications. B

## Description

# Description

The AWS ECR Image Listing procedure involves enumerating information about an image within an Amazon Elastic Container Registry (ECR). This can be useful for an attacker who is trying to gain a better understanding of the target environment, particularly in the case of containerized applications. By listing the information about an image, an attacker can gain insight into the operating system, application dependencies, and other details that can be used to further the attack. Technical details of this procedure include using the 'ECR Image Description' command to retrieve metadata about an image stored in an ECR repository. The business value of this procedure is that it can help organizations identify potential vulnerabilities in their containerized applications before they are exploited by attackers.

 

## Requirements

1. Valid AWS credentials with permissions to access ECR repositories

1. Access to the target ECR repository

 

## Defense

1. Ensure that AWS credentials are stored securely and not shared among users

1. Implement access controls to limit who can access ECR repositories

1. Regularly monitor ECR repositories for unauthorized access or changes

 

## Objectives

1. To gather information about an image stored in an ECR repository

1. To identify potential vulnerabilities in containerized applications

 

# Instructions

1. This command provides a detailed description of the specified ECR image.

 

The 'aws ecr describe-images' command is used to retrieve metadata about the specified images in an Amazon Elastic Container Registry (ECR) repository. The '--repository-name' option specifies the ECR repository name and the '--image-ids' option specifies the image tag (name) for which the description is required. The output of this command includes image details such as image size, image tags, creation time, and more. This command can be used to retrieve information about a single image or multiple images by specifying multiple image IDs.



**Command** ([[Describe ECR image]]):

```bash
aws ecr describe-images --repository-name name --images-ids imageTag=name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Describe ECR image]]

## Tags

- [[Cloud - AWS]]
- [[ECR]]
- [[Enumeration]]
- [[Listing information about an image]]


