---
id: cmd-uuid-2
data: 'docker run --rm --name oc-eval -d -p8080:8080 owncloud-imagemagick:latest'
tags:
  - docker
  - run
  - container
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.573Z'
verified: false
validated: true
submitted: true
---
# docker-run-owncloud-container

## Command

```bash
docker run --rm --name oc-eval -d -p8080:8080 owncloud-imagemagick:latest
```

## Description

Starts a Docker container from the owncloud-imagemagick image in detached mode, mapping port 8080 for web access, and auto-removing on exit for clean testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--rm` | Remove container after exit | Yes |
| `--name` | Assign name 'oc-eval' to the container | Yes |
| `-d` | Run in detached background mode | Yes |
| `-p8080:8080` | Map host port 8080 to container port 8080 | Yes |
| `owncloud-imagemagick:latest` | Image to run | Yes |

## Examples

### Basic Usage

```bash
docker run --rm --name oc-eval -d -p8080:8080 owncloud-imagemagick:latest
```

### Advanced Usage

```bash
docker run --rm --name oc-eval -d -p8080:8080 -v /path/to/data:/mnt/data owncloud-imagemagick:latest
```

## Expected Output

Container ID (e.g., 'abc123def456') confirming the container is running. Access ownCloud at http://localhost:8080.

## Related

- [[commands/docker-build-owncloud-imagemagick]]
- [[procedures/Set-Up-Vulnerable-ownCloud-Environment-with-ImageMagick]]
