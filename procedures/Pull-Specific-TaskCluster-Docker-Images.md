---
tags:
  - docker
  - pull
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/docker-pull-taskcluster]]'
platforms:
  - Docker
  - Linux
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 308a9322-149b-4b65-ad3c-b75b12068002
created_at: '2025-12-14T17:31:42.963Z'
updated_at: '2025-12-14T17:31:42.963Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Pull-Specific-TaskCluster-Docker-Images

## Summary

This procedure pulls specific Docker images from the TaskCluster repository on Docker Hub to acquire artifacts containing potential secrets.

## Description

Public Docker images can inadvertently include sensitive data like API tokens if not properly scrubbed during builds. This step targets known vulnerable tags to download the images locally for further inspection, simulating an attacker's reconnaissance phase.

## Requirements

1. Docker installed and running
2. Sufficient disk space (~500MB per image)
3. Internet access

## Defense

Defensive measures and detection strategies:

- Scan images for secrets before publishing
- Rate-limit pulls on public registries
- Use vulnerability scanners like Clair

## Objectives

1. Download vulnerable images
2. Prepare for filesystem inspection
3. Avoid detection by using standard pull commands

## Instructions

### Step 1: Pull Individual Images

**Context**: Download each selected tag to local Docker daemon.

**Command** ([[commands/docker-pull-taskcluster]]):
```bash
docker pull taskcluster/taskcluster:v15.0.0-20-g0eca18b7c
docker pull taskcluster/taskcluster:c061025dc
docker pull taskcluster/taskcluster:ba7958766
docker pull taskcluster/taskcluster:v16.2.0-77-gd8577f62a
```

> Each command fetches the image layer by layer. Verify with `docker images | grep taskcluster`. Expected output: Image IDs and sizes.

### Step 2: Verify Pull Success

**Context**: Confirm images are available locally.

**Command**:
```bash
docker images | grep taskcluster
```

> Lists pulled images.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/docker-pull-taskcluster]]

## Tools Used

- [[tools/Docker]]

## Tags

- image-pull
- taskcluster
