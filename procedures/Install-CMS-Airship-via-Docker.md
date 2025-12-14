---
id: proc-install-airship-docker
tags:
  - installation
  - docker
  - cms-airship
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:20.823Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Install-CMS-Airship-via-Docker

## Summary

This procedure sets up a local instance of CMS Airship version 1.1.0 using Docker, enabling registration and vulnerability exploration for stored XSS testing.

## Description

CMS Airship is a PHP-based CMS using Twig templating. The installation via Docker creates a containerized environment on ports 8080 and 8081, with default settings that allow user registration. This is the foundational step for exploiting the author profiles XSS, as it provides a controlled vulnerable setup. Expected outcomes include a running application accessible via browser, ready for account creation and payload injection.

## Requirements

1. Docker installed on the host machine
2. Local network access (localhost)
3. No prior CMS installation needed

## Defense

Defensive measures and detection strategies:

- Use official Docker images from trusted sources to avoid tampered setups
- Monitor Docker container launches for unauthorized images
- Implement network segmentation to limit local access

## Objectives

1. Deploy a functional CMS Airship instance
2. Ensure registration is enabled for attacker simulation
3. Validate accessibility on required ports

## Instructions

### Step 1: Pull and Run Docker Image

**Context**: Download the CMS Airship image and start the container with default configuration.

No specific command; use Docker CLI or desktop to run the image `airshipcms/airship` (version 1.1.0) mapping ports 8080:80 and 8081:81, ensuring volume mounts for persistence if needed.

> Launch the container; wait for startup logs indicating PHP server readiness.

### Step 2: Verify Installation

**Context**: Confirm the application is running and registration is possible.

Access http://localhost:8080 in a browser.

> Expected: Main page loads; check config for registration enabled (default).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- installation
- docker
- cms-airship
