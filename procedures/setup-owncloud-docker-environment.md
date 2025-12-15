---
id: proc-setup-owncloud-docker
tags:
  - docker
  - setup
  - environment
type: procedure
tools:
  - '[[tools/docker-compose]]'
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
updated_at: '2025-12-14T17:27:57.732Z'
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
# Setup ownCloud Docker Environment

## Summary

This procedure sets up a vulnerable ownCloud 10.12.2 instance using Docker Compose, including dependencies like Redis and MariaDB, to prepare for CSRF exploitation testing.

## Description

The ownCloud environment is deployed via Docker to replicate the vulnerable setup where CSRF token validation fails due to improper Authorization header handling in SecurityMiddleware. This allows testing POST requests without tokens. Prerequisites include Docker and Docker Compose installed on the host system.

## Requirements

1. Docker and Docker Compose installed
2. Access to create and run containers on localhost
3. Basic knowledge of YAML configuration for docker-compose

## Defense

Defensive measures and detection strategies:

- Monitor Docker container deployments for unauthorized ownCloud instances
- Use network segmentation to limit exposure of development environments
- Implement container scanning for known vulnerabilities

## Objectives

1. Deploy a functional ownCloud instance with the specified version
2. Ensure dependencies (Redis, MariaDB) are operational
3. Verify accessibility on port 8080

## Instructions

### Step 1: Create Docker Compose Configuration

**Context**: Define the services in a docker-compose.yml file to orchestrate ownCloud, Redis, and MariaDB.

**Command** (docker-compose-up):
```bash
docker-compose up -d
```

> This starts the containers in detached mode using the configuration for owncloud/server:10.12.2, Redis, and MariaDB. Expected output: Containers running, ownCloud accessible at http://localhost:8080.

### Step 2: Verify Deployment

**Context**: Check if the services are up and the web interface loads.

**Command** (docker-compose-ps):
```bash
docker-compose ps
```

> Lists running services. Expected output: All three services (owncloud, redis, mariadb) in 'Up' state.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/docker-compose]]

## Tags

- docker
- setup
- owncloud
