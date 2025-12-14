---
tags:
  - bitwarden
  - docker
  - self-hosted
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.260Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0430d6d6-89fd-4ef2-860a-c74a46569b63
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install Self-Hosted Bitwarden with Docker

## Summary

Deploy a self-hosted Bitwarden instance using Docker to replicate the vulnerable environment for SSRF testing in the icons service.

## Description

Bitwarden's on-premise installation includes the icons service (IconFetchingService.cs) vulnerable to SSRF due to incomplete IP checks. Use specific versions (core 1.35.1) to match the report.

## Requirements

1. Docker and Docker Compose installed
2. Server with sufficient resources (4GB RAM min)
3. Access to Bitwarden installation scripts

## Defense

Defensive measures and detection strategies:

- Keep Bitwarden updated beyond vulnerable versions
- Disable icon fetching or restrict to trusted domains
- Monitor Docker container logs for anomalous fetches

## Objectives

1. Replicate production-like Bitwarden setup
2. Enable icon fetching feature
3. Provide UI for credential addition

## Instructions

### Step 1: Download Installation Files

**Context**: Get official scripts.

```bash
git clone https://github.com/bitwarden/server.git
cd server
```

> Expected: Repository cloned.

### Step 2: Configure and Run Docker Compose

**Context**: Customize env vars for self-host.

Edit .env with global settings, then:

```bash
docker-compose up -d
```
Follow https://bitwarden.com/help/article/install-on-premise/ for full setup, including database init.

> Expected: Services running; access https://your-ip.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- bitwarden
- docker
- self-hosted
