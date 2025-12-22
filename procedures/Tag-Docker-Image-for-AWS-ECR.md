---
type: procedure
description: >-
  Tagging Docker images for AWS Elastic Container Registry (ECR) to manage
  versions, organize images, or evade detection by altering identifiable tags.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Persistence]]'
  - '[[Defense Evasion]]'
techniques:
  - '[[Indicator Removal on Host]]'
sub_techniques: []
tags:
  - cloud-aws
  - persistence
  - docker
  - ecr
  - evasion
commands:
  - '[[commands/docker-tag-image-for-ecr]]'
platforms:
  - AWS
  - Linux
  - Docker
tools: []
validated: true
---

# Tag-Docker-Image-for-AWS-ECR

## Summary

This procedure tags a local Docker image with a new name and pushes it to an AWS ECR repository, enabling organized management, version control, or evasion of security tools that scan for specific image identifiers. In an attack context, attackers can retag malicious images to blend with legitimate ones, avoiding detection during container deployment in cloud environments.

## Description

Tagging Docker images for AWS ECR involves using the Docker CLI to assign a repository-specific tag to an existing image, preparing it for upload to ECR. This is essential for deploying containerized workloads in AWS but can be abused for persistence by maintaining backdoored images under innocuous tags or for evasion by obscuring the image's origin. The process requires authenticated AWS access and Docker installed on the host. Technically, the 'docker tag' command creates a new reference to the image without altering its content, allowing multiple tags for the same image ID. In offensive scenarios, this facilitates injecting persistence mechanisms into CI/CD pipelines or runtime environments while minimizing forensic footprints.

## Requirements

1. Docker CLI installed and accessible on the local machine.
2. AWS CLI configured with credentials that have ECR push permissions (e.g., AmazonEC2ContainerRegistryFullAccess policy).
3. The target ECR repository must exist; create it via AWS console or CLI if needed.
4. Network access to the AWS region hosting the ECR repository.

## Defense

- Implement least-privilege IAM policies to restrict ECR tagging and push actions to authorized roles only.
- Monitor ECR repositories for unexpected tag changes or pushes using AWS CloudTrail and GuardDuty, alerting on anomalous image metadata.
- Use image scanning tools like Amazon Inspector or Trivy to verify tagged images for vulnerabilities or tampering before deployment.
- Enforce tag naming conventions and validate them in CI/CD pipelines to prevent evasion via custom tags.

## Objectives

1. Assign a new tag to a Docker image compatible with an AWS ECR repository.
2. Facilitate identification and management of images in cloud deployments.
3. Enable automation of image versioning while potentially evading detection through tag manipulation.

## Instructions

### Step 1: Authenticate with AWS ECR

**Context**: Before tagging, ensure Docker is authenticated to push to ECR. This step uses AWS CLI to generate a login token for Docker.

Run the AWS CLI command to authenticate:

```bash
aws ecr get-login-password --region $_AWS_REGION | docker login --username AWS --password-stdin $_AWS_ACCOUNT_ID.dkr.ecr.$_AWS_REGION.amazonaws.com
```

> This command retrieves a temporary authentication token and logs Docker into the ECR registry. Replace $_AWS_REGION (e.g., us-west-2) and $_AWS_ACCOUNT_ID (e.g., 123456789012) with your values. Expected output: "Login Succeeded" if credentials are valid.

### Step 2: Tag the Docker Image for ECR

**Context**: Use the Docker tag command to create a new reference for the image, incorporating the ECR repository URI. This prepares the image for pushing without modifying its layers.

**Command** ([[commands/docker-tag-image-for-ecr]]):

```bash
docker tag $_IMAGE_NAME $_ECR_ADDR:$_TAG_NAME
```

> Execute this to tag the source image ($_IMAGE_NAME, e.g., my_image:latest) with the ECR address ($_ECR_ADDR, e.g., 123456789012.dkr.ecr.us-west-2.amazonaws.com) and desired tag ($_TAG_NAME, e.g., new_image). Verify with `docker images` to see the new tag. Expected output: No direct output, but `docker images` lists the image with both old and new tags pointing to the same ID.

### Step 3: Verify and Push the Tagged Image

**Context**: Confirm the tag was applied correctly and push to ECR for persistence in the cloud environment.

List images to verify:

```bash
docker images | grep $_TAG_NAME
```

Then push:

```bash
docker push $_ECR_ADDR:$_TAG_NAME
```

> The list command should show the new tag. The push uploads layers to ECR. Expected output for push: Progress bars for layer uploads, ending with "latest: digest: sha256:... size: ..." indicating success.
