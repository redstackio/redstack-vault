---
id: uuid-1
tags:
  - setup
  - docker
  - nextcloud
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/docker-run-nextcloud]]'
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.344Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Nextcloud-Instance-with-Docker

## Summary

This procedure deploys a local Nextcloud instance using Docker to create a controlled environment for testing the user_oidc stored XSS vulnerability.

## Description

Nextcloud is a self-hosted file sync and share platform. This setup uses the official Docker image to run it locally on port 8081, allowing access to the web interface for configuration and exploitation. The instance must be accessible via http://localhost:8081, and initial admin setup may be required on first access.

## Requirements

1. Docker installed on the host machine
2. Local network access
3. No prior Nextcloud installation

## Defense

Defensive measures and detection strategies:

- Monitor Docker container startups for unauthorized images
- Restrict port mappings to trusted hosts
- Use container scanning tools like Trivy to check for vulnerabilities in images

## Objectives

1. Establish a reproducible testing environment
2. Ensure Nextcloud is running with default configurations
3. Prepare for OIDC app integration

## Instructions

### Step 1: Run Nextcloud Container

**Context**: Launch the official Nextcloud Docker image, mapping host port 8081 to container port 80 for web access.

**Command** ([[commands/docker-run-nextcloud]]):
```bash
docker run -p 8081:80 nextcloud:latest
```

> This command pulls and starts the latest Nextcloud image. Expected output includes logs showing Apache starting and the app initializing. Access http://localhost:8081 to verify; complete the setup wizard if prompted.

### Step 2: Verify Accessibility

**Context**: Confirm the instance is running and responsive.

**Instructions**: Open a browser and navigate to http://localhost:8081. Log in or set up admin credentials.

> No command needed; success if the login page loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/docker-run-nextcloud]]

## Tools Used

- [[tools/Docker]]

## Tags

- setup
- docker
- nextcloud
