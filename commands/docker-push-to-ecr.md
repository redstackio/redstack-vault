---
id: 2e7c095b-ebd1-4265-a2ed-e767215745f8
name: docker-push-to-ecr
type: command
executor: bash
data: 'docker push $_ECR_REGISTRY/$_REPO:$_TAG'
output: null
created_at: '2023-04-06T03:56:13.184456+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - docker
  - ecr
  - push
verified: true
validated: true
---

# docker-push-to-ecr

## Command

```bash
docker push $_ECR_REGISTRY/$_REPO:$_TAG
```

## Description

This command uploads a tagged Docker image to the specified AWS ECR repository, transferring image layers and metadata for storage and later deployment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ECR_REGISTRY | ECR registry URI (e.g., 123456789012.dkr.ecr.us-west-2.amazonaws.com) | Yes |
| $_REPO | Repository name within ECR (e.g., backdoor-repo) | Yes |
| $_TAG | Specific image tag to push (e.g., latest) | Yes |

## Examples

### Basic Usage

```bash
docker push 123456789012.dkr.ecr.us-west-2.amazonaws.com/backdoor-repo:latest
```

### Advanced Usage

Push with progress output:

```bash
docker push --quiet $_ECR_REGISTRY/$_REPO:$_TAG
```

## Expected Output

The push dry run succeeded
latest: digest: sha256:abc123... size: 1.23MB
total: digest: sha256:def456... size: 4.56MB

Progress bars show layer uploads; errors indicate authentication issues or quota limits.

## Related

- [[procedures/Upload-Malicious-Docker-Image-to-AWS-ECR-for-Persistence]]
- [[commands/docker-tag-for-ecr]]
