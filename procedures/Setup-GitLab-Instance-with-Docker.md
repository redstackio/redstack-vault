---
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
  - '[[commands/gitlab-rake-env-info]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:44.381Z'
sub_techniques: []
id: ebdde3ec-9b50-4875-be1b-9feb5809c4e1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-GitLab-Instance-with-Docker

## Summary

This procedure deploys a local GitLab Community Edition instance using Docker, providing a controlled environment to reproduce the Stored XSS vulnerability in merge requests.

## Description

The attack requires a running GitLab instance vulnerable to the branch name XSS (e.g., version 12.4.0). Docker simplifies setup by pulling the official image and exposing necessary ports for web access and Git operations. After startup, verify the environment with rake tasks to confirm versions.

## Requirements

1. Docker installed on a Linux host
2. Root or sudo access for container management
3. Available ports 80, 443, 22
4. Internet access to pull GitLab image

## Defense

Defensive measures and detection strategies:

- Use official Docker images from trusted registries
- Monitor container startups with tools like Docker Scout
- Restrict port exposures in production

## Objectives

1. Deploy functional GitLab CE instance
2. Expose services for UI and Git access
3. Verify environment for vulnerability reproduction

## Instructions

### Step 1: Run GitLab Container

**Context**: Start the detached container with custom hostname and port mappings.

**Command** ([[commands/docker-run-gitlab-instance]]):
```bash
docker run --detach --hostname gitlab.example.com --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab gitlab/gitlab-ce:latest
```

> This command pulls and runs the latest GitLab CE image in background mode, setting hostname for internal resolution and publishing ports for external access. Expected output: Container ID and startup logs.

### Step 2: Verify Environment

**Context**: Check GitLab versions and services post-initialization (wait ~5-10 minutes).

**Command** ([[commands/gitlab-rake-env-info]]):
```bash
docker exec -it gitlab gitlab-rake gitlab:env:info
```

> Runs the rake task inside the container to display system info, GitLab version (e.g., 12.4.0), Ruby, PostgreSQL, Redis. Expected output: Detailed environment summary confirming services like PostgreSQL 10.9, Redis 3.2.12.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/docker-run-gitlab-instance]]
- [[commands/gitlab-rake-env-info]]

## Tools Used

- [[tools/Docker]]

## Tags

- setup
- docker
- gitlab
