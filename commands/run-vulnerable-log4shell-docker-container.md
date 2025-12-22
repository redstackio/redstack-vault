---
id: 50de325e-3382-43b1-bb3d-ed3626a6c7c6
name: run-vulnerable-log4shell-docker-container
type: command
executor: bash
data: >-
  docker run --name vulnerable-log4shell-app -p 8080:8080
  ghcr.io/christophetd/log4shell-vulnerable-app
output: null
created_at: '2023-04-06T03:55:56.831624+00:00'
updated_at: '2023-04-06T03:55:56.838440+00:00'
platforms:
  - Linux
tags:
  - docker
  - vulnerable-app
verified: true
validated: true
---

# run-vulnerable-log4shell-docker-container

## Command

```bash
docker run --name vulnerable-log4shell-app -p 8080:8080 ghcr.io/christophetd/log4shell-vulnerable-app
```

## Description

This command pulls and starts a Docker container running a vulnerable Spring Boot application affected by Log4Shell (CVE-2021-44228). It simulates a public-facing web app for testing exploitation. Use this in local environments to deploy the target before sending payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--name vulnerable-log4shell-app` | Assigns a name to the container for easy management | Yes |
| `-p 8080:8080` | Maps host port 8080 to container port 8080 for access via localhost | Yes |
| `ghcr.io/christophetd/log4shell-vulnerable-app` | The image repository and tag for the vulnerable app | Yes |

## Examples

### Basic Usage

```bash
docker run --name vulnerable-log4shell-app -p 8080:8080 ghcr.io/christophetd/log4shell-vulnerable-app
```

Run this to start the container. Access the app at http://localhost:8080.

### Advanced Usage

```bash
docker run --name vulnerable-log4shell-app -p 8080:8080 -d ghcr.io/christophetd/log4shell-vulnerable-app
```

Add `-d` to run in detached mode.

## Expected Output

The command outputs Docker pull progress if the image is not cached, then:

```
Unable to find image 'ghcr.io/christophetd/log4shell-vulnerable-app:latest' locally
latest: Pulling from christophetd/log4shell-vulnerable-app
...
Status: Downloaded newer image for ghcr.io/christophetd/log4shell-vulnerable-app:latest
...
Hello World!
```

Success: Container runs and app responds on port 8080. Check with `docker ps` to confirm it's active.

## Related

- [[procedures/Log4Shell-Exploitation-via-Docker]]
- [[commands/curl-send-log4shell-payload]]
