---
tags:
  - docker
  - pull
  - cli
  - image
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/docker-pull-run]]'
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:31:30.927Z'
sub_techniques: []
id: 71cb2738-9e55-4289-8fde-6cefd8ad7886
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Pull Full Docker Image with CLI

## Summary

This procedure uses the Docker CLI to pull an entire image from an unauthenticated registry and run it for inspection, providing an alternative to manual layer downloads for full repository access.

## Description

Specify the registry/repo:tag in docker pull/run commands to fetch and execute the image. In the .mil scenario, this dumps all contents without auth. Requires Docker installed; allows interactive access to source code and tools.

## Requirements

1. Docker CLI installed
2. Registry, repo, and tag known
3. Network access to registry

## Defense

Defensive measures and detection strategies:

- Enforce auth in Docker daemon config
- Block unauthorized pulls via firewall
- Log Docker API interactions

## Objectives

1. Pull complete image layers
2. Run container for content inspection
3. Dump full repository

## Instructions

### Step 1: Pull Image

**Context**: Download the full image using Docker.

**Command** ([[commands/docker-pull-run]]):
```bash
docker pull TARGET_IP/NAMESPACE/REPO:3.0.1
```

> Fetches all layers and manifest.

### Step 2: Run and Inspect

**Context**: Start a container to explore contents.

**Command** ([[commands/docker-pull-run]]):
```bash
docker run --rm -it TARGET_IP/NAMESPACE/REPO:3.0.1 /bin/sh
```

> Enters interactive shell; use ls, cat to inspect files.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used

- [[commands/docker-pull-run]]

## Tools Used

- [[tools/Docker]]

## Tags

- docker
- pull
- cli
