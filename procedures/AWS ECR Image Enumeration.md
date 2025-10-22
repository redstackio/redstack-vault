---
id: f1d49b37-c502-4900-bf43-6aeded77ed33
name: AWS ECR Image Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.073624+00:00'
updated_at: '2023-04-10T20:20:47.097975+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Listing all images in the repository]]'
- '[[Persistence]]'
commands:
- '[[List ECR Images]]'
---

# AWS ECR Image Enumeration

## Summary

AWS Elastic Container Registry (ECR) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. This procedure allows an attacker to enumerate all images in the ECR repository, providing valuable information about the target 

## Description

# Description

AWS Elastic Container Registry (ECR) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. This procedure allows an attacker to enumerate all images in the ECR repository, providing valuable information about the target environment. By listing all images in the repository, an attacker can gain insight into the types of applications and services that are running in the target environment, as well as the software versions and configurations that are in use. This information can be used to identify potential vulnerabilities and to plan further attacks.

Technical Description: The attacker uses the 'List ECR Images' command to list all images in the ECR repository. The command returns a list of image IDs, which can be used to obtain additional information about the images and the containers that they are associated with.

Business Value: This procedure can be used by an attacker to gain a better understanding of the target environment and identify potential vulnerabilities. By identifying vulnerabilities, the attacker can plan further attacks that can result in data theft, system compromise, or other types of damage.

## Requirements

1. Valid AWS credentials with permissions to list ECR images

1. Access to the AWS console or AWS CLI

## Defense

1. Limit access to the AWS console and AWS CLI to authorized personnel only

1. Implement multi-factor authentication (MFA) for AWS console and AWS CLI access

1. Monitor AWS CloudTrail logs for suspicious activity related to ECR image enumeration

## Objectives

1. Enumerate all images in the ECR repository

1. Identify potential vulnerabilities in the target environment

1. Plan further attacks based on the information obtained

# Instructions

1. To list all the images in a specified Amazon Elastic Container Registry (ECR) repository, use the following command:

The 'aws ecr list-images' command is used to list all the images in a specified ECR repository. The '--repository-name' argument specifies the name of the repository for which you want to list the images. This command returns a JSON object containing information about the images in the specified repository, including the image tags, creation dates, and sizes. You can use this command to get an overview of the images in your ECR repository and to determine which images are available for use in your container deployments.

**Command** ([[List ECR Images]]):

```bash
aws ecr list-images --repository-name name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List ECR Images]]

## Tags

- [[Cloud - AWS]]
- [[Listing all images in the repository]]
- [[Persistence]]
