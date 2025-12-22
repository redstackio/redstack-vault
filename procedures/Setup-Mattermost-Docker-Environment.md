---
id: proc-mmw-docker-setup-001
tags:
  - setup
  - docker
  - mattermost
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/docker-run-mattermost]]'
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T05:32:10.477Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Setup-Mattermost-Docker-Environment

## Summary

This procedure deploys a Mattermost server instance in a Docker container with a 4GB memory limit to create a controlled environment for reproducing the GIF upload DoS vulnerability.

## Description

The Mattermost preview image is run in Docker to simulate a production-like setup with resource constraints. This allows observation of the OOM crash when the malicious GIF is uploaded, as the server allocates excessive RAM during GIF decoding without prior dimension checks in the upload path.

## Requirements

1. Docker installed and running on the host system
2. Access to pull the mattermost/mattermost-preview image
3. Local port 8065 available

## Defense

Defensive measures and detection strategies:

- Monitor Docker container memory usage with tools like docker stats
- Implement image upload size and type restrictions in Mattermost config
- Use resource limits and alerts for OOM events in container orchestration

## Objectives

1. Deploy a vulnerable Mattermost instance for testing
2. Ensure memory is capped at 4GB to trigger OOM
3. Verify server accessibility before exploitation

## Instructions

### Step 1: Pull and Run Mattermost Container

**Context**: Start the Docker container with specified limits to host the vulnerable Mattermost server.

**Command** ([[commands/docker-run-mattermost]]):
```bash
docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview -m=4G
```

> This command pulls the preview image if needed, runs it detached (-d), names the container, publishes port 8065, and sets a 4GB memory limit (-m=4G). Expected output includes the container ID; verify with `docker ps`.

### Step 2: Verify Server Accessibility

**Context**: Confirm the server is running and responsive.

**Command**:
```bash
docker logs mattermost-preview
```

> Check logs for startup messages. Access http://localhost:8065 in a browser to see the login page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (adapted for Linux/Docker setup)

### Sub-Techniques


## Commands Used

- [[commands/docker-run-mattermost]]

## Tools Used

- [[tools/Docker]]

## Tags

- setup
- docker
- mattermost
