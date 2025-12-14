---
id: proc-nextcloud-docker-setup
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
  - '[[commands/docker-run-nextcloud-setup]]'
verified: false
platforms:
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.888Z'
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
# Setup-Nextcloud-Instance-with-Docker

## Summary

This procedure deploys a local Nextcloud instance using Docker, providing an isolated environment to test the user_oidc XSS vulnerability without affecting production systems.

## Description

The procedure involves running the official Nextcloud Docker image, mapping host port 8081 to the container's port 80 for web access. This creates a fresh instance accessible at http://localhost:8081, where initial admin setup can be completed. It is a prerequisite for enabling and configuring the vulnerable user_oidc app, simulating a self-hosted Nextcloud deployment vulnerable to the stored XSS flaw in the OIDC integration.

## Requirements

1. Docker installed on the host machine with sufficient privileges to run containers
2. Local network access (localhost) for testing
3. At least 2GB RAM and 10GB disk space for the container

## Defense

Defensive measures and detection strategies:

- Monitor Docker daemon logs for unauthorized container spins using tools like Docker Bench for Security
- Restrict Docker socket access to prevent privilege escalation from containers
- Use container scanning tools like Trivy to ensure the Nextcloud image is up-to-date and patched

## Objectives

1. Establish a running Nextcloud server for vulnerability reproduction
2. Ensure the instance is accessible via HTTP on a non-standard port to avoid conflicts
3. Prepare the environment for app installation and configuration

## Instructions

### Step 1: Run Nextcloud Container

**Context**: Launch the official Nextcloud image to create the target instance.

**Command** ([[commands/docker-run-nextcloud-setup]]):
```bash
docker run -p 8081:80 nextcloud:latest
```

> This command pulls and starts the Nextcloud container, binding host port 8081 to container port 80. Expected output includes logs like "AH00558: apache2: Could not reliably determine the server's fully qualified domain name" followed by the server listening on port 80. Access http://localhost:8081 to complete the web-based setup wizard, creating an admin user.

### Step 2: Verify Instance Accessibility

**Context**: Confirm the Nextcloud web interface is operational.

**Instructions**: Open a browser and navigate to http://localhost:8081. Complete any initial setup prompts.

> Expected output: Nextcloud login or setup page loads without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/docker-run-nextcloud-setup]]

## Tools Used

- [[tools/Docker]]

## Tags

- [[setup]]
- [[tools/Docker]]
- [[nextcloud]]
