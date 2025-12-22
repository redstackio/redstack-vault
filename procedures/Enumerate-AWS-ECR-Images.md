---
id: f1d49b37-c502-4900-bf43-6aeded77ed33
name: Enumerate-AWS-ECR-Images
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.073624+00:00'
updated_at: '2023-04-10T20:20:47.097975+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Listing all images in the repository]]'
  - '[[tags/Persistence]]'
commands:
  - '[[commands/aws-ecr-list-images]]'
platforms:
  - AWS
  - Cloud
tools: []
validated: true
---

# Enumerate-AWS-ECR-Images

## Summary

This procedure enables an attacker with AWS credentials to list all Docker container images stored in an Amazon Elastic Container Registry (ECR) repository, revealing details about deployed applications, software versions, and potential vulnerabilities in the target cloud environment.

## Description

Amazon Elastic Container Registry (ECR) is AWS's managed Docker container service for storing, managing, and deploying container images. In an attack scenario, an attacker who has obtained valid AWS credentials (e.g., via credential dumping or misconfiguration) can enumerate ECR images to map the target's containerized infrastructure. This discovery step provides insights into running services, image tags, creation dates, and sizes, which can inform targeted exploits such as vulnerability scanning on specific image versions or identifying outdated software for further compromise. The procedure relies on the AWS CLI to query the ECR API, returning structured JSON data that can be parsed for actionable intelligence. This is particularly useful in cloud persistence or lateral movement phases where understanding container deployments aids in maintaining access or escalating privileges.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least `ecr:ListImages` permission on the target repository.
2. AWS CLI installed and configured with the target account's credentials (e.g., via `aws configure`).
3. Network access to AWS endpoints (no VPC restrictions blocking ECR API calls).
4. Knowledge of the target ECR repository name (discoverable via other AWS enumeration procedures like listing repositories).

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict `ecr:ListImages` access to only necessary roles or users.
- Enable AWS CloudTrail logging for ECR API calls and monitor for anomalous `ListImages` requests from unexpected IPs or users.
- Use AWS Organizations SCPs to deny ECR actions in sensitive environments.
- Integrate with SIEM tools to alert on unusual ECR enumeration patterns, such as rapid API calls during off-hours.

## Objectives

1. Retrieve a complete list of images in the specified ECR repository, including tags, digests, and metadata.
2. Identify software versions and configurations for vulnerability assessment in the target's container ecosystem.
3. Gather intelligence to support further attacks, such as targeting known CVEs in enumerated images or planning persistence via modified containers.

## Instructions

### Step 1: List Images in ECR Repository

**Context**: This step queries the ECR repository to fetch all available images, providing an overview of the container assets. It assumes you have identified the repository name beforehand; if not, use a separate procedure to list repositories first. The command authenticates via your configured AWS credentials and returns JSON output that can be piped to tools like `jq` for parsing.

**Command** ([[commands/aws-ecr-list-images]]):
```bash
aws ecr list-images --repository-name $_REPOSITORY_NAME
```

> This command invokes the ECR `ListImages` API, specifying the repository via the `--repository-name` flag. Replace `$_REPOSITORY_NAME` with the actual repository name (e.g., `my-app-repo`). If the repository is in a specific registry, add `--registry-id $_REGISTRY_ID` for cross-account access. Success is indicated by a JSON response with an `imageIds` array; errors like `AccessDenied` suggest insufficient permissions. Pipe output to `jq '.imageIds[] | .imageTag'` to extract tags for quick review.
