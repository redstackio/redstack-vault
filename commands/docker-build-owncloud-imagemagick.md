---
id: cmd-uuid-1
data: docker build . -t owncloud-imagemagick
tags:
  - docker
  - build
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.588Z'
verified: false
validated: true
submitted: true
---
# docker-build-owncloud-imagemagick

## Command

```bash
docker build . -t owncloud-imagemagick
```

## Description

Builds a custom Docker image for ownCloud with ImageMagick installed, using the current directory as context and tagging it for later use in vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `.` | Build context directory (current folder with Dockerfile) | Yes |
| `-t` | Tags the image with the name 'owncloud-imagemagick' | Yes |

## Examples

### Basic Usage

```bash
docker build . -t owncloud-imagemagick
```

### Advanced Usage

```bash
docker build -f Dockerfile . -t owncloud-imagemagick:v1
```

## Expected Output

Build logs showing layers being created, ending with 'Successfully tagged owncloud-imagemagick:latest'. The image is ready for running.

## Related

- [[commands/docker-run-owncloud-container]]
- [[procedures/Set-Up-Vulnerable-ownCloud-Environment-with-ImageMagick]]
