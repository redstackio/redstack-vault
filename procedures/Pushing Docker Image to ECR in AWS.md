---
id: fcb55c75-a1cb-4c4b-bed6-463e5753061d
name: Pushing Docker Image to ECR in AWS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.189115+00:00'
updated_at: '2023-04-10T20:20:35.536203+00:00'
tags:
- '[[Cloud - AWS]]'
- '[[Persistence]]'
- '[[Pushing the image to ECR]]'
commands:
- '[[Push Docker Image to ECR]]'
---

# Pushing Docker Image to ECR in AWS

## Summary

Pushing Docker images to ECR is a common task in AWS environments. This procedure can be used by attackers to upload malicious images to an ECR repository, which can then be used as part of a larger attack. On the technical side, this procedure involves authenticating to AWS, building and tagging a

## Description

# Description

Pushing Docker images to ECR is a common task in AWS environments. This procedure can be used by attackers to upload malicious images to an ECR repository, which can then be used as part of a larger attack. On the technical side, this procedure involves authenticating to AWS, building and tagging a Docker image, and then pushing the image to the ECR repository. From a business perspective, this procedure can allow attackers to gain a foothold in an AWS environment and potentially move laterally to other systems.

 

## Requirements

1. Valid AWS credentials

1. Access to the internet

1. Docker installed on the local machine

 

## Defense

1. Implement strict access controls for AWS credentials and ECR repositories

1. Scan Docker images for vulnerabilities before pushing them to ECR

1. Monitor ECR repositories for suspicious activity

 

## Objectives

1. Gain access to an AWS environment

1. Upload a malicious Docker image to an ECR repository

1. Use the malicious image as part of a larger attack

 

# Instructions

1. To push a Docker image to ECR, use the following command:

docker push ecr_addr:Image_Name

Replace 'ecr_addr' with the address of the ECR repository and 'Image_Name' with the name of the Docker image you want to push.

 

This command pushes a Docker image to an Amazon Elastic Container Registry (ECR) repository. The 'docker push' command is used to push the Docker image to the specified ECR repository. The 'ecr_addr' is the address of the ECR repository where you want to push the Docker image. The 'Image_Name' is the name of the Docker image that you want to push.



**Command** ([[Push Docker Image to ECR]]):

```bash
docker push ecr_addr:Image_Name
```



## Commands Used

- [[Push Docker Image to ECR]]

## Tags

- [[Cloud - AWS]]
- [[Persistence]]
- [[Pushing the image to ECR]]


