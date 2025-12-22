---
id: proc-uuid-001
name: Setup-GitLab-Docker-Container
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.905Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - docker
  - setup
  - gitlab
commands:
  - '[[commands/docker-run-gitlab-setup]]'
platforms:
  - Linux
  - Docker
tools:
  - '[[tools/Docker]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Setup-GitLab-Docker-Container

## Summary

This procedure launches a GitLab Community Edition instance in a Docker container, providing a controlled environment to reproduce the blind SSRF vulnerability in the FogBugz project import feature.

## Description

The procedure uses the official GitLab CE Docker image to spin up an instance with exposed ports for HTTP, HTTPS, and SSH. This setup mimics a production-like GitLab deployment vulnerable to SSRF, allowing subsequent steps to access internal services. Prerequisites include Docker installed on a Linux host; the container runs in detached mode with a custom hostname.

## Requirements

1. Docker engine installed and running on the host machine
2. Sufficient resources (at least 4GB RAM, 2 CPUs) for GitLab startup
3. Network access to pull the gitlab/gitlab-ce:latest image

## Defense

Defensive measures and detection strategies:

- Monitor Docker container creations with tools like Docker Bench for Security
- Restrict Docker daemon access to privileged users only
- Use container scanning tools like Trivy to check for known vulnerabilities in images

## Objectives

1. Deploy a functional GitLab instance for vulnerability testing
2. Ensure ports are mapped for external access to the UI
3. Verify the instance is ready for import feature exploitation

## Instructions

### Step 1: Run GitLab Container

**Context**: Initiate the Docker container with necessary port mappings and hostname to host the vulnerable GitLab application.

**Command** ([[commands/docker-run-gitlab-setup]]):
```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
```

> This command pulls and starts the latest GitLab CE image in the background, mapping host ports 80, 443, and 22 to the container. Expected output includes a container ID; monitor startup with `docker logs gitlab` until GitLab is accessible.

### Step 2: Verify Container Startup

**Context**: Confirm the container is running and GitLab services are operational.

**Command** (docker logs):
```bash
docker logs -f gitlab
```

> Tail the logs to watch for initialization; success is indicated by messages like "GitLab is running" and no fatal errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/docker-run-gitlab-setup]]

## Tools Used

- [[tools/Docker]]

## Tags

- docker
- setup
- gitlab
