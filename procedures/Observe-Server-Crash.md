---
id: proc-observe-crash
tags:
  - dos
  - monitoring
  - oom
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:32:20.350Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Observe-Server-Crash

## Summary

This procedure monitors the Docker container for out-of-memory termination following the malicious GIF upload.

## Description

After upload, the server attempts to decode the GIF, consuming over 4GB RAM, causing Docker to kill the container. This confirms the DoS impact of the vulnerability in the upload API's handling.

## Requirements

1. Running Docker container from prior steps
2. Access to host for monitoring

## Defense

Defensive measures and detection strategies:

- Enable OOM killer logs in Docker
- Alert on container restarts
- Use resource quotas in orchestration

## Objectives

1. Track RAM usage post-upload
2. Confirm container kill
3. Validate DoS success

## Instructions

### Step 1: Monitor Resources

**Context**: Watch usage in real-time.

**Command** (docker stats):
```bash
docker stats mattermost-preview
```

> Shows CPU/RAM; expect RAM to spike >4GB.

### Step 2: Check Logs and Status

**Context**: Inspect for OOM evidence.

**Command** (docker logs):
```bash
docker logs mattermost-preview
```

> Look for errors; then `docker ps` to see container stopped.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- dos
- monitoring
- oom
