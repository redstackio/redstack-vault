---
id: proc-uuid-1
tags:
  - setup
  - docker
  - owncloud
  - imagemagick
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/docker-build-owncloud-imagemagick]]'
  - '[[commands/docker-run-owncloud-container]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:24.601Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Vulnerable-ownCloud-Environment-with-ImageMagick

## Summary

This procedure sets up a local Docker-based ownCloud instance with ImageMagick installed to replicate the vulnerable environment for testing RCE exploits via MSL and SVG files.

## Description

The setup uses a Dockerfile extending owncloud/server:10.11, installing ImageMagick without security policies. This allows simulation of the production scenario where ownCloud's preview generation processes user-uploaded files insecurely, leading to RCE. Prerequisites include Docker installed on a Linux host; the environment runs on port 8080 and uses default admin credentials.

## Requirements

1. Docker installed and running on the host machine.
2. Access to a Dockerfile that installs ImageMagick via apt-get update && apt-get install -y imagemagick.
3. Local network access to port 8080.
4. Basic knowledge of Docker commands.

## Defense

Defensive measures and detection strategies:

- Disable ImageMagick in ownCloud or configure policy.xml to restrict MSL/SVG processing.
- Monitor Docker container creations and port mappings for anomalous ownCloud setups.
- Use container scanning tools to detect vulnerable ImageMagick configurations.

## Objectives

1. Establish a running ownCloud instance with ImageMagick for exploit testing.
2. Ensure the environment matches the vulnerable state (no sandboxing).
3. Verify accessibility for file uploads.

## Instructions

### Step 1: Build the Docker Image

**Context**: Compile the custom ownCloud image with ImageMagick to prepare the vulnerable setup.

**Command** ([[commands/docker-build-owncloud-imagemagick]]):
```bash
docker build . -t owncloud-imagemagick
```

> This command builds from the current directory using the Dockerfile, tagging the image 'owncloud-imagemagick'. Expected output includes build logs ending with 'Successfully tagged owncloud-imagemagick:latest'.

### Step 2: Run the Container

**Context**: Start the ownCloud server in a detachable container, exposing it for web access.

**Command** ([[commands/docker-run-owncloud-container]]):
```bash
docker run --rm --name oc-eval -d -p8080:8080 owncloud-imagemagick:latest
```

> Runs in background mode (--d), auto-removes on exit (--rm), names it 'oc-eval', and maps ports. Expected output is the container ID; verify with docker ps.

### Step 3: Authenticate to ownCloud

**Context**: Access the web interface to confirm the setup and prepare for uploads.

**Instructions**: Open http://localhost:8080 in a browser and log in with 'admin'/'admin'. No command required; use the UI.

> Successful login grants file upload access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/docker-build-owncloud-imagemagick]]
- [[commands/docker-run-owncloud-container]]

## Tools Used

- [[tools/Docker]]

## Tags

- setup
- docker
- owncloud
