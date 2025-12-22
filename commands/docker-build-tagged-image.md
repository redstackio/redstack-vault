---
id: 49038211-6137-4642-85e7-b6de618d5c5c
name: docker-build-tagged-image
type: command
executor: bash
data: 'docker build -t $_IMAGE_NAME:$_TAG .'
output: null
created_at: '2023-04-06T03:56:13.138017+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - docker
  - build
  - container
verified: true
validated: true
---

# docker-build-tagged-image

## Command

```bash
docker build -t $_IMAGE_NAME:$_TAG .
```

## Description

This command builds a Docker image from a Dockerfile in the current directory, assigning it a specific name and tag for identification and versioning. It is essential for creating custom images, including those with embedded persistence mechanisms like backdoors, in offensive security operations targeting containerized environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IMAGE_NAME | The repository and image name (e.g., myregistry/myapp) | Yes |
| $_TAG | The version tag (e.g., latest, v1.0) | Yes |
| -t | Flag to specify the image name and tag | Built-in |
| . | Build context (current directory) | Yes |

## Examples

### Basic Usage

```bash
docker build -t myapp:latest .
```

Builds an image named 'myapp' with tag 'latest' from the current directory.

### Advanced Usage

```bash
docker build --no-cache -t myregistry/myapp:v1.0 --build-arg VERSION=1.0 .
```

Builds without cache and passes a build argument for dynamic configuration.

## Expected Output

The command outputs build progress for each layer:

```
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM ubuntu:20.04
 ---> 7e0aa2d69a15
Step 2/4 : RUN apt-get update && apt-get install -y curl
 ---> Running in abc123def456
...
Successfully built 789ghi012
Successfully tagged myapp:latest
```

Success is indicated by the "Successfully tagged" message. Errors appear as failed steps with details like missing files or syntax issues.

## Related

- [[related-procedure|Create-Backdoored-Docker-Image]]
- [[docker-push-image-to-registry]]
