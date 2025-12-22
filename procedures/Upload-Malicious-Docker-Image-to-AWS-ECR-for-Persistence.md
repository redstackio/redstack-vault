---
id: fcb55c75-a1cb-4c4b-bed6-463e5753061d
name: Upload-Malicious-Docker-Image-to-AWS-ECR-for-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.189115+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[T1078.004]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Persistence]]'
  - '[[tags/Container]]'
  - '[[tags/ECR]]'
commands:
  - '[[commands/aws-ecr-get-login-password]]'
  - '[[commands/docker-tag-for-ecr]]'
  - '[[commands/docker-push-to-ecr]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/Docker]]'
  - '[[tools/AWS-CLI]]'
validated: true
---

# Upload-Malicious-Docker-Image-to-AWS-ECR-for-Persistence

## Summary

This procedure outlines how to authenticate to AWS Elastic Container Registry (ECR), tag a local Docker image (potentially containing malicious payloads for persistence), and push it to an ECR repository. In an attack context, this allows adversaries with compromised AWS credentials to upload backdoored container images that can be deployed in cloud environments for long-term access, lateral movement, or command-and-control.

## Description

Uploading a malicious Docker image to AWS ECR enables persistence in cloud infrastructures by storing executable code in a trusted registry. Attackers can use stolen AWS credentials to push images that include reverse shells, credential dumpers, or other implants. Once uploaded, these images can be pulled and run in ECS tasks, EKS clusters, or EC2 instances controlled by the attacker. This technique assumes the attacker has initial access to AWS via valid accounts and a local Docker environment. The process involves AWS CLI for authentication, Docker for tagging and pushing, and targets ECR repositories with push permissions. Successful execution results in the image being available for deployment, evading some detection if the repository is not monitored closely.

## Requirements

1. Valid AWS credentials with ECR push permissions (e.g., IAM role or access keys configured via AWS CLI).
2. Internet access to reach AWS services.
3. Docker installed and running on the local machine (Linux, macOS, or Windows with Docker Desktop).
4. AWS CLI installed and configured with the target region.
5. A pre-built local Docker image containing the malicious payload.
6. ECR repository URI (e.g., account-id.dkr.ecr.region.amazonaws.com/repo-name).

## Defense

- Implement least-privilege IAM policies restricting ECR push actions to trusted users/services.
- Enable ECR image scanning with Amazon Inspector to detect vulnerabilities and malware in pushed images.
- Monitor CloudTrail logs for unauthorized ECR API calls (e.g., PutImage, InitiateLayerUpload).
- Use repository policies to require image signing and block unsigned pushes.
- Regularly audit ECR repositories for unexpected images and integrate with SIEM for anomaly detection.

## Objectives

1. Authenticate securely to ECR using AWS credentials to enable Docker pushes.
2. Tag and upload a malicious container image to maintain persistence in the AWS environment.
3. Establish a foothold for deploying the image in production workloads like ECS or EKS.

## Instructions

### Step 1: Authenticate to ECR

**Context**: Obtain a temporary authentication token for Docker to interact with ECR, ensuring secure login without exposing long-term credentials. This step uses AWS CLI to generate a password for Docker login.

**Command** ([[commands/aws-ecr-get-login-password]]):
```bash
aws ecr get-login-password --region $_AWS_REGION | docker login --username AWS --password-stdin $_ECR_REGISTRY
```

> This command retrieves a base64-encoded password from AWS and pipes it to Docker login. Replace placeholders with your region (e.g., us-west-2) and ECR registry URI (e.g., 123456789012.dkr.ecr.us-west-2.amazonaws.com). Expected output is a success message like "Login Succeeded". If it fails, check credentials and permissions.

### Step 2: Tag the Local Image for ECR

**Context**: Assign the correct ECR repository URI to your local Docker image, preparing it for push. This ensures the image is associated with the target repository and version.

**Command** ([[commands/docker-tag-for-ecr]]):
```bash
docker tag $_LOCAL_IMAGE:$_TAG $_ECR_REGISTRY/$_REPO:$_TAG
```

> Tag your local image (e.g., mymaliciousimage:latest) with the ECR URI (e.g., 123456789012.dkr.ecr.us-west-2.amazonaws.com/backdoor-repo:latest). This creates a new tag without altering the original image. Expected output confirms the tagging, verifiable via `docker images` showing the new entry.

### Step 3: Push the Image to ECR

**Context**: Upload the tagged image to the ECR repository, making it available for deployment. This final step transfers layers and metadata to AWS.

**Command** ([[commands/docker-push-to-ecr]]):
```bash
docker push $_ECR_REGISTRY/$_REPO:$_TAG
```

> Push the tagged image to ECR. Progress will show layer uploads (e.g., "Pushing layer sha256:..."). Expected output ends with "latest: digest: sha256:... size: ..." indicating successful upload. Verify in the AWS console under ECR repositories.
