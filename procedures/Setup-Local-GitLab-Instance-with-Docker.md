---
id: uuid-setup-gitlab
tags:
  - setup
  - docker
  - gitlab
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/docker-run-gitlab-instance]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:24.532Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Setup-Local-GitLab-Instance-with-Docker

## Summary

This procedure deploys a local GitLab Community Edition instance using Docker, providing a controlled environment to reproduce the stored XSS vulnerability without affecting production systems.

## Description

The procedure uses the official GitLab CE Docker image to spin up a full GitLab installation with PostgreSQL, Redis, and Git services. It maps necessary ports for web access and SSH, allowing interaction via the UI and console. This setup is essential for enabling feature flags and testing the vulnerability in isolation. Expected outcomes include a running GitLab instance accessible at localhost, ready for user account creation and payload injection.

## Requirements

1. Docker installed on a Linux host
2. Available ports 80, 443, 22
3. Sufficient resources (at least 4GB RAM for the container)
4. Internet access to pull the Docker image

## Defense

Defensive measures and detection strategies:

- Monitor Docker container creations and port bindings for unauthorized setups
- Use container orchestration tools like Kubernetes with network policies to restrict local deployments
- Scan for anomalous Docker runs in logs

## Objectives

1. Establish a reproducible GitLab environment
2. Ensure all services (DB, cache, Git) are operational
3. Prepare for feature flag modifications and UI interactions

## Instructions

### Step 1: Run GitLab Container

**Context**: Launch the detached GitLab CE container with hostname and port configurations to mimic a standard installation.

**Command** ([[commands/docker-run-gitlab-instance]]):
```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
```

> This command pulls and starts the latest GitLab CE image in the background, naming the container 'gitlab' and mapping ports for HTTP/HTTPS/SSH. Expected output includes the container ID and startup logs; full initialization takes 5-10 minutes. Verify with `docker logs -f gitlab` until the web interface is ready.

### Step 2: Verify Startup

**Context**: Confirm the instance is running and accessible.

**Command** (docker ps):
```bash
docker ps
```

> Lists running containers; look for 'gitlab' in UP status. Access http://localhost in a browser to complete initial root password setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used

- [[commands/docker-run-gitlab-instance]]

## Tools Used

- [[tools/Docker]]

## Tags

- setup
- docker
- gitlab
