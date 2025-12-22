---
type: command
executor: bash
data: 'docker tag $_IMAGE_NAME $_ECR_ADDR:$_TAG_NAME'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Docker
tags:
  - docker
  - ecr
  - tagging
verified: true
validated: true
---

# docker-tag-image-for-ecr

## Command

```bash
docker tag $_IMAGE_NAME $_ECR_ADDR:$_TAG_NAME
```

## Description

This command creates a new tag for an existing Docker image, referencing an AWS ECR repository URI. It is used to prepare images for pushing to ECR, enabling cloud deployment or evasion by renaming images to avoid pattern-based detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IMAGE_NAME | Source image name and tag (e.g., my_image:latest) | Yes |
| $_ECR_ADDR | ECR repository address (e.g., 123456789012.dkr.ecr.us-west-2.amazonaws.com) | Yes |
| $_TAG_NAME | New tag name for the image (e.g., production-app:v1) | Yes |

## Examples

### Basic Usage

```bash
docker tag my_image:latest 123456789012.dkr.ecr.us-west-2.amazonaws.com:new_image
```

### Advanced Usage

```bash
docker tag nginx:alpine 123456789012.dkr.ecr.us-west-2.amazonaws.com:web-server:v1.0
```

## Expected Output

The command produces no stdout output on success. Verify by running `docker images`, which should list the image with the new tag alongside the original, both sharing the same IMAGE ID (e.g., REPOSITORY: 123456789012.dkr.ecr.us-west-2.amazonaws.com/new_image, TAG: latest, IMAGE ID: sha256:abc123...).

## Related

- [[procedures/Tag-Docker-Image-for-AWS-ECR]]
