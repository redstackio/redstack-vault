---
id: proc-uuid-002
name: Access-GitLab-Container-Shell
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.902Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - docker
  - shell-access
  - gitlab
commands:
  - '[[commands/docker-exec-gitlab-bash]]'
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

# Access-GitLab-Container-Shell

## Summary

This procedure provides interactive shell access to the running GitLab Docker container, enabling installation of tools and setup of listeners for SSRF exploitation.

## Description

Using Docker's exec command, this step attaches an interactive bash session to the container named 'gitlab'. This is essential for modifying the internal environment, such as installing netcat, in a Debian-based GitLab image. The target is a running container from the previous setup step.

## Requirements

1. Running GitLab Docker container named 'gitlab'
2. Docker CLI access on the host
3. Bash shell available in the container (default in GitLab image)

## Defense

Defensive measures and detection strategies:

- Enable Docker content trust to prevent unauthorized images
- Log and alert on docker exec commands via auditd or Falco
- Use read-only containers where possible to limit shell access

## Objectives

1. Establish shell session inside the GitLab container
2. Prepare for internal tool installation
3. Enable manipulation of the container environment for testing

## Instructions

### Step 1: Execute Interactive Shell

**Context**: Connect to the container to gain root-level access for subsequent commands.

**Command** ([[commands/docker-exec-gitlab-bash]]):
```bash
docker exec -it gitlab /bin/bash
```

> The -it flags enable interactive mode with a pseudo-TTY. Expected output is a root shell prompt inside the container, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/docker-exec-gitlab-bash]]

## Tools Used

- [[tools/Docker]]

## Tags

- docker
- shell-access
- gitlab
