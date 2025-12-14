---
id: proc-mmw-observe-crash-001
tags:
  - dos
  - verification
  - oom
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T05:32:10.469Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Observe-Mattermost-Server-Crash

## Summary

This procedure monitors the Mattermost server post-upload to confirm the DoS impact through OOM-induced crash.

## Description

After the malicious GIF upload, the server's upload handling path (App.UploadData -> gif.DecodeAll) consumes >4GB RAM without checks, exceeding the Docker limit and killing the container. Logs and status checks verify the denial of service.

## Requirements

1. Docker container running with memory limit
2. Access to docker commands for logs and status
3. Upload completed from previous step

## Defense

Defensive measures and detection strategies:

- Enable Docker OOM notifications and auto-restart policies
- Integrate monitoring tools like Prometheus for RAM alerts
- Review server logs for decode errors and high memory events

## Objectives

1. Detect memory exhaustion during GIF processing
2. Confirm container termination
3. Validate DoS achievement

## Instructions

### Step 1: Monitor Docker Logs

**Context**: Watch for error messages indicating crash.

**Command**:
```bash
docker logs mattermost-preview
```

> Look for OOM killer messages or decode failures.

### Step 2: Check Container Status

**Context**: Verify if the container has been killed.

**Command**:
```bash
docker ps -a
```

> The mattermost-preview container should show exited status due to OOM.

### Step 3: Test Server Responsiveness

**Context**: Confirm service denial.

**Command**:

> Attempt access to http://localhost:8065; expect timeout or error.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- dos
- verification
- oom
