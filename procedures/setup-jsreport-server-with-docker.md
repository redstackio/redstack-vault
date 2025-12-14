---
tags:
  - docker
  - setup
type: procedure
tools:
  - '[[tools/docker]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/docker-run-jsreport-vulnerable]]'
platforms:
  - Linux
  - Docker
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f5578556-6d5a-406c-a4f6-5e2f6eefe5d7
created_at: '2025-12-14T17:23:25.006Z'
updated_at: '2025-12-14T17:23:25.006Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup jsreport Server with Docker

## Summary

This procedure deploys a vulnerable jsreport 2.5.0 instance using Docker, exposing the web interface for subsequent exploitation steps.

## Description

jsreport is a Node.js-based reporting server vulnerable to SSRF and RCE in version 2.5.0. This setup mounts a persistent volume and maps ports to allow access to the unauthenticated interface, simulating a production-like environment for testing the chained vulnerabilities.

## Requirements

1. Docker installed on a Linux host
2. Sudo privileges for Docker execution
3. Local directory /jsreport-home for volume mounting

## Defense

Defensive measures and detection strategies:

- Run jsreport in a container with network isolation to prevent external access
- Monitor Docker container startups for unauthorized images
- Use vulnerability scanners like Trivy to detect outdated jsreport versions

## Objectives

1. Start the vulnerable jsreport server
2. Ensure persistence for uploaded scripts and templates
3. Verify interface accessibility

## Instructions

### Step 1: Run Docker Container

**Context**: Launch the jsreport container with port mapping and volume mount to host the vulnerable application.

**Command** ([[commands/docker-run-jsreport-vulnerable]]):
```bash
sudo docker run -p 80:5488 -v /jsreport-home:/jsreport jsreport/jsreport:2.5.0
```

> This command pulls the jsreport:2.5.0 image, maps host port 80 to container port 5488, and mounts /jsreport-home for data storage. Expected output includes startup logs like "jsreport server started on port 5488".

### Step 2: Verify Access

**Context**: Confirm the server is running and the web interface is accessible.

**Command** (curl):
```bash
curl http://localhost
```

> Returns HTML of the jsreport dashboard if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/docker-run-jsreport-vulnerable]]

## Tools Used

- [[tools/docker]]

## Tags

- docker
- setup
