---
id: new-uuid-1
name: aws-ecr-get-login-password
type: command
executor: bash
data: >-
  aws ecr get-login-password --region $_AWS_REGION | docker login --username AWS
  --password-stdin $_ECR_REGISTRY
output: null
created_at: '2023-04-06T03:56:13.184456+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - ecr
  - auth
verified: true
validated: true
---

# aws-ecr-get-login-password

## Command

```bash
aws ecr get-login-password --region $_AWS_REGION | docker login --username AWS --password-stdin $_ECR_REGISTRY
```

## Description

This command generates a temporary authentication token from AWS ECR and uses it to log in Docker, allowing subsequent pushes to private ECR repositories without exposing AWS access keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_AWS_REGION | AWS region for the ECR repository (e.g., us-west-2) | Yes |
| $_ECR_REGISTRY | Full ECR registry URI (e.g., 123456789012.dkr.ecr.us-west-2.amazonaws.com) | Yes |
| --region | Specifies the AWS region | Built-in |
| --username AWS | Fixed username for ECR authentication | Built-in |
| --password-stdin | Reads password from stdin for security | Built-in |

## Examples

### Basic Usage

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```

### Advanced Usage

For multi-account setups, combine with profile flags:

```bash
AWS_PROFILE=attacker aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-west-2.amazonaws.com
```

## Expected Output

Login Succeeded

If unsuccessful: "Error saving credentials: error storing credentials - err: exit status 1, out: `Cannot prompt because stdin is not a terminal`". Check AWS CLI config and IAM permissions.

## Related

- [[procedures/Upload-Malicious-Docker-Image-to-AWS-ECR-for-Persistence]]
- [[commands/docker-tag-for-ecr]]
