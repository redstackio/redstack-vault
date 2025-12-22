---
id: proc-setup-mattermost-docker
tags:
  - setup
  - docker
  - mattermost
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/docker-run-mattermost]]'
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.365Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Mattermost-Docker-Environment

## Summary

This procedure deploys a Mattermost server instance in a Docker container with a 4GB memory limit to create a reproducible environment for testing the GIF upload DoS vulnerability.

## Description

The Mattermost preview image is run in Docker to simulate a server vulnerable to uncontrolled resource consumption during image uploads. The memory limit ensures the OOM crash is observable. This setup targets the upload API flaw where gif.DecodeAll is called without prior dimension checks, leading to excessive RAM usage from a small malformed GIF.

## Requirements

1. Docker installed on a Linux host
2. Access to pull the mattermost/mattermost-preview image
3. Port 8065 available on the host

## Defense

Defensive measures and detection strategies:

- Monitor Docker resource usage with tools like cAdvisor
- Limit container memory in production deployments
- Apply Mattermost patches for image upload validation

## Objectives

1. Establish a vulnerable Mattermost instance
2. Ensure memory constraints for OOM demonstration
3. Verify server accessibility for API interactions

## Instructions

### Step 1: Run Docker Container

**Context**: Start the Mattermost server in detached mode with port mapping and memory limit.

**Command** ([[commands/docker-run-mattermost]]):
```bash
docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview -m=4G
```

> This command pulls and runs the image, names the container, publishes port 8065, and sets a 4GB memory limit. Expected output: Container ID and running status.

### Step 2: Verify Setup

**Context**: Confirm the server is accessible.

**Command** (docker ps):
```bash
docker ps
```

> Lists running containers; look for mattermost-preview. Access http://localhost:8065 to confirm UI loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/docker-run-mattermost]]

## Tools Used

- [[tools/Docker]]

## Tags

- setup
- docker
- mattermost
