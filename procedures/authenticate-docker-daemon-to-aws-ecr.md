---
id: fc34ebd0-f2d3-4950-9108-23329a58f8da
name: Authenticate Docker Daemon to AWS ECR
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.120197+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[T1078.004]]'
sub_techniques: []
tags:
  - aws
  - ecr
  - docker
  - persistence
  - cloud
commands:
  - '[[commands/docker-login-to-aws-ecr]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/aws-cli]]'
  - '[[tools/Docker]]'
validated: true
---

# Authenticate Docker Daemon to AWS ECR

## Summary

This procedure authenticates a local Docker daemon to an Amazon Elastic Container Registry (ECR) repository using AWS credentials, enabling the push and pull of Docker images. In an offensive security context, an attacker with compromised AWS credentials can use this to access a victim's ECR registry, potentially stealing proprietary container images containing sensitive data or intellectual property, or uploading malicious images for persistence and further compromise.

## Description

Amazon ECR is a managed Docker container registry service in AWS that stores, manages, and deploys Docker container images. Authenticating the Docker daemon to ECR is essential for interacting with ECR repositories, such as pushing built images or pulling existing ones for deployment. The process leverages the AWS CLI to generate a temporary authentication token (valid for 12 hours) based on IAM permissions, which is then used by the Docker client to log in to the registry.

From an attacker's perspective, obtaining valid AWS credentials (e.g., via phishing, misconfiguration, or privilege escalation) allows unauthorized authentication to a target ECR. This can lead to data exfiltration by pulling sensitive images or persistence by pushing backdoored containers that could be deployed in the victim's environment. The technique aligns with using valid cloud accounts to maintain access without triggering immediate alerts, assuming the credentials have ecr:GetAuthorizationToken and related permissions.

This procedure assumes the target environment is an AWS account with ECR enabled, and the attacker has access to a machine with Docker and AWS CLI installed. Success enables full read/write access to specified repositories based on IAM policies.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least ecr:GetAuthorizationToken permission on the target ECR registry.
2. AWS CLI installed and configured with the credentials (via aws configure or environment variables).
3. Docker daemon running on the local machine with sufficient privileges to execute login commands.
4. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).
5. Knowledge of the target AWS region and ECR registry URI (e.g., account-id.dkr.ecr.region.amazonaws.com).

## Defense

- Implement least-privilege IAM policies for ECR access, restricting ecr:GetAuthorizationToken and repository actions to specific roles or users.
- Enable AWS CloudTrail logging for ECR API calls to monitor authentication attempts and detect anomalous logins from unusual IP addresses or user agents.
- Use AWS Organizations SCPs to deny cross-account ECR access and require MFA for credential usage.
- Scan ECR images with Amazon Inspector or third-party tools for vulnerabilities and monitor push/pull events via CloudWatch.
- Rotate credentials regularly and use temporary credentials via STS for short-lived access.

## Objectives

1. Generate a temporary authentication token for the ECR registry using AWS CLI.
2. Authenticate the local Docker daemon to the target ECR registry.
3. Verify successful authentication by querying repository access.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is properly configured with credentials that have ECR access. This step confirms the prerequisites are met before attempting authentication, preventing errors from misconfigured profiles.

Run the AWS CLI version check and test ECR access:

**Command** ([[commands/aws-cli-version-check]]):
```bash
aws --version
```

> This displays the installed AWS CLI version. Expected output: aws-cli/2.x.x Python/3.x.x Linux/x86_64.

**Command** ([[commands/aws-ecr-describe-repositories-test]]):
```bash
aws ecr describe-repositories --region $_REGION
```

> This tests if credentials can list ECR repositories. If successful, it returns a JSON list of repositories (or empty if none). If unauthorized, it errors with AccessDeniedException.

### Step 2: Retrieve ECR Login Password

**Context**: Use the AWS CLI to fetch the base64-encoded authorization token (password) for the specified region. This token is derived from the AWS credentials and is required for Docker login.

**Command** ([[commands/aws-ecr-get-login-password]]):
```bash
aws ecr get-login-password --region $_REGION
```

> This outputs the raw password token. Store it temporarily (e.g., in a variable) for the next step. Do not log or expose this token as it grants ECR access.

### Step 3: Authenticate Docker Daemon

**Context**: Pipe the retrieved password to the Docker login command, using AWS as the username and the ECR registry URI as the hostname. This updates the Docker config with the authentication details for 12 hours.

**Command** ([[commands/docker-login-to-aws-ecr]]):
```bash
aws ecr get-login-password --region $_REGION | docker login --username AWS --password-stdin $_ECR_URI
```

> Expected output: "Login Succeeded". This confirms the daemon is authenticated and can now interact with the ECR registry.

### Step 4: Verify Authentication

**Context**: Test the login by attempting a simple Docker operation against ECR, such as pulling a public image or listing tags if permissions allow. This validates the authentication without modifying the registry.

**Command** ([[commands/docker-pull-test-ecr]]):
```bash
docker pull $_ECR_URI/aws/nginx:latest
```

> If successful, it downloads the image layers. Expected output includes progress bars and "latest: Pulling from aws/nginx". Errors indicate failed auth or permissions.
