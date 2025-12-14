---
tags:
  - setup
  - gitlab
  - docker
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/Docker-Run-GitLab-Instance]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:44.273Z'
sub_techniques: []
id: dbbe5e80-d0af-41b9-939a-f55c52ace7c0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Set-Up-GitLab-Instance-with-Docker

## Summary

This procedure deploys a local GitLab Community Edition instance using Docker, providing a controlled environment to test and reproduce the stored XSS vulnerability in the CI/CD job page.

## Description

The procedure involves running the official GitLab CE Docker image with custom hostname and port mappings to expose web and SSH services. This setup mimics a production-like GitLab instance vulnerable to the Kubernetes namespace XSS issue. Once running, users can access the UI to configure projects and integrations. Prerequisites include Docker installed on the host machine and sufficient resources (at least 4GB RAM recommended for GitLab).

## Requirements

1. Docker installed and running on the host (Linux, macOS, or Windows with Docker Desktop)
2. Root or sudo access to execute Docker commands
3. Available ports 80, 443, and 22 on the host
4. Network access to resolve gitlab.example.com (or edit /etc/hosts if local)

## Defense

Defensive measures and detection strategies:

- Monitor Docker container creations for unauthorized GitLab instances
- Use container orchestration tools like Kubernetes for managed deployments instead of ad-hoc Docker runs
- Enable logging on Docker daemon to track image pulls and port bindings

## Objectives

1. Establish a functional GitLab test environment
2. Expose necessary ports for UI and SSH access
3. Prepare for subsequent project and integration setup

## Instructions

### Step 1: Run GitLab Container

**Context**: Launch the GitLab CE container in detached mode with specified configurations to make it accessible.

**Command** ([[commands/Docker-Run-GitLab-Instance]]):
```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
```

> This command pulls and starts the latest GitLab CE image, sets the hostname, maps ports for HTTP/HTTPS/SSH, and runs it in the background. Expected output includes the container ID. Wait 5-10 minutes for initialization, then access http://gitlab.example.com to set the root password.

### Step 2: Verify Instance Accessibility

**Context**: Confirm the instance is running and responsive before proceeding.

**Command** (docker ps):
```bash
docker ps
```

> Lists running containers; look for the 'gitlab' container in 'Up' status. Access the UI in a browser to complete setup if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/Docker-Run-GitLab-Instance]]

## Tools Used

- [[tools/Docker]]

## Tags

- setup
- gitlab
- docker
