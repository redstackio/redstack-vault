---
id: a2aa9762-1897-40e4-9345-ac4dc7b3602c
name: Docker Login to AWS ECR
type: command
executor: bash
data: >-
  aws ecr get-login-password --region $_REGION | docker login --username AWS
  --password-stdin $_ECR_URI
output: null
created_at: '2023-04-06T03:56:13.114768+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - aws
  - ecr
  - docker
verified: true
validated: true
---

# Docker Login to AWS ECR

## Command

```bash
aws ecr get-login-password --region $_REGION | docker login --username AWS --password-stdin $_ECR_URI
```

## Description

This command retrieves a temporary authentication token from AWS ECR using the AWS CLI and pipes it to the Docker login utility to authenticate the Docker daemon to a specific ECR registry. It is used to enable pushing and pulling images from ECR repositories. In offensive scenarios, it allows attackers with stolen credentials to gain registry access for exfiltration or persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REGION | AWS region of the ECR registry (e.g., us-east-1) | Yes |
| $_ECR_URI | ECR registry URI (e.g., 123456789012.dkr.ecr.us-east-1.amazonaws.com) | Yes |
| --username AWS | Fixed username for ECR authentication | Built-in |
| --password-stdin | Reads password from stdin (piped from AWS CLI) | Built-in |

## Examples

### Basic Usage

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```

### Advanced Usage

For scripted use with environment variables:

```bash
export REGION=us-west-2
export ECR_URI=987654321098.dkr.ecr.us-west-2.amazonaws.com
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ECR_URI
```

## Expected Output

```
Login Succeeded
```

If failed, outputs errors like "Error saving credentials: error storing credentials - err: exit status 1, out: `Cannot connect to the Docker daemon`" or AWS-specific denial messages.

## Related

- [[Related Procedure]]: [[procedures/authenticate-docker-daemon-to-aws-ecr]]
- [[Related Tool]]: [[tools/aws-cli]], [[tools/Docker]]
