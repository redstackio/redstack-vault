---
id: proc-dump-images-docker-fetch
tags:
  - docker
  - image-dumping
  - registry
type: procedure
tools:
  - '[[tools/docker_fetch]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:32:57.736Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
---
# Dump-Images-with-Docker-Fetch

## Summary

This procedure uses the docker_fetch tool to pull and dump Docker images from the unauthenticated registry via the SSH-tunneled endpoint.

## Description

With the registry exposed at http://127.0.0.1:5555/, docker_fetch interacts with the v2 API to download manifests, layers, and configs for repositories like 'lgtm/top' without needing credentials, exploiting the improper access control.

## Requirements

1. Active SSH tunnel to registry
2. docker_fetch installed and configured
3. Target repository name known (e.g., 'lgtm/top')

## Defense

Defensive measures and detection strategies:

- Require authentication on all registry endpoints
- Log API access and monitor for bulk downloads
- Implement rate limiting on blob fetches

## Objectives

1. Extract sensitive Docker images
2. Analyze or exfiltrate image contents
3. Assess impact on site reliability and data

## Instructions

### Step 1: Configure and Run Docker Fetch

**Context**: Point the tool to the tunneled URL and target repo.

No command; use docker_fetch with options:

```bash
docker_fetch http://127.0.0.1:5555/ lgtm/top
```

> Downloads all image artifacts to local directory. Expected: Files like manifest.json, layer.tar.gz.

### Step 2: Verify Dump

**Context**: Inspect downloaded images.

Use docker load or tar to view contents.

> Expected: Access to image layers revealing potential secrets or configs.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage Object

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/docker_fetch]]

## Tags

- image-dumping

---
