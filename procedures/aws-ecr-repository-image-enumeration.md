---
id: 047275eb-e913-495c-b52e-944c1387a2f8
name: aws-ecr-repository-image-enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.591886+00:00'
updated_at: '2023-04-10T20:20:30.908750+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - aws
  - ecr
  - enumeration
  - cloud-discovery
commands:
  - '[[commands/aws-ecr-list-images]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS ECR Repository Image Enumeration

## Summary

The AWS ECR Repository Image Enumeration procedure uses the AWS CLI to list all images within a specific Amazon Elastic Container Registry (ECR) repository. This allows attackers or security testers to gain visibility into the container images deployed in the environment, potentially revealing vulnerabilities, outdated software, or sensitive artifacts embedded in the images.

## Description

In cloud environments, ECR serves as a managed Docker container registry for storing, managing, and deploying container images. Enumerating images in a repository provides insights into the target's container ecosystem, such as image versions, sizes, and digests, which can inform further attacks like image exploitation or supply chain compromise. This technique is particularly useful during discovery phases to map out container assets without direct access to the underlying infrastructure. The procedure relies on AWS API permissions for ECR and assumes the attacker has compromised credentials with read access to the target repository. Expected outcomes include a JSON-formatted list of images that can be analyzed for weaknesses using tools like Trivy or Clair for vulnerability scanning.

## Requirements

1. Valid AWS credentials with permissions to call the ECR ListImages API (e.g., attached policy including "ecr:ListImages" action on the target repository).
2. AWS CLI installed and configured with the appropriate profile (e.g., via `aws configure`).
3. Network access to AWS endpoints (no VPC endpoints required unless in a private subnet).
4. Knowledge of the target ECR repository name, which may be obtained from prior enumeration of ECR repositories.

## Defense

- Implement principle of least privilege by restricting ECR permissions to only necessary roles and users, using IAM policies to deny ListImages actions where possible.
- Enable AWS CloudTrail logging for ECR API calls to detect unauthorized enumeration attempts.
- Use AWS Organizations SCPs to limit ECR access across accounts and regularly rotate credentials.
- Monitor for anomalous API activity using Amazon GuardDuty or custom CloudWatch alarms on ECR events.

## Objectives

1. List all container images in a target ECR repository to identify potential vulnerabilities or misconfigurations.
2. Gather metadata on image digests, tags, and push times to support further analysis or targeting of specific images.
3. Map the container deployment landscape for escalation or lateral movement in the AWS environment.

## Instructions

### Step 1: List Images in the ECR Repository

**Context**: This step retrieves a list of all images stored in the specified ECR repository, providing details like image digests, tags, and sizes. It is the core action for enumeration and requires knowing the repository name in advance. Run this from a machine with AWS CLI access; output is in JSON format for easy parsing or piping to other tools.

**Command** ([[commands/aws-ecr-list-images]]):
```bash
aws ecr list-images --repository-name $_REPOSITORY_NAME
```

> This command queries the AWS ECR service and returns a JSON object containing an array of image identifiers. If the repository contains multiple images, each will include attributes like imageDigest (SHA256 hash), imageTag (e.g., 'latest'), and imageSizeInBytes. Success is indicated by a non-empty imageIds array; errors may occur if credentials lack permissions or the repository does not exist. For large repositories, consider adding `--max-results 1000` to paginate results.

### Step 2: Parse and Analyze Output

**Context**: After retrieving the list, parse the JSON output to extract actionable details, such as identifying untagged or old images that might be vulnerable. This step adds value by verifying the enumeration and preparing data for vulnerability scanning.

**Command** ([[commands/aws-ecr-describe-images]]):
```bash
aws ecr describe-images --repository-name $_REPOSITORY_NAME --image-ids imageTag=$_IMAGE_TAG
```

> Use this follow-up command to get detailed manifests for specific images identified in Step 1. It provides layer details and scan findings if ECR image scanning is enabled. Expected output includes image manifests in JSON, revealing OS/packages for vulnerability assessment. If no images are present, the response will be an empty array, indicating a potentially unused or cleaned repository.
