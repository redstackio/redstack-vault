---
id: proc-uuid-003
name: Install-Netcat-in-GitLab-Container
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.898Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - netcat
  - installation
  - apt
  - gitlab
commands:
  - '[[commands/apt-install-netcat]]'
platforms:
  - Linux
  - Docker
tools:
  - '[[tools/Apt]]'
  - '[[tools/Netcat]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Install-Netcat-in-GitLab-Container

## Summary

This procedure installs the netcat utility inside the GitLab Docker container using the apt package manager, preparing the environment for an internal TCP listener to detect SSRF connections.

## Description

Netcat is installed on the Debian-based GitLab image to listen for incoming SSRF requests. The procedure updates the package index first to ensure availability, then installs without prompts. This step assumes shell access from the prior procedure and targets GitLab CE 12.3.5.

## Requirements

1. Interactive shell in the GitLab container
2. Internet access from the container for package downloads
3. Root privileges (default in Docker exec)

## Defense

Defensive measures and detection strategies:

- Implement package manager whitelisting to block unauthorized installations
- Monitor apt logs for unexpected updates in containers
- Use minimal base images without package managers if possible

## Objectives

1. Install netcat for network listening capabilities
2. Update container packages to avoid dependency issues
3. Verify tool availability for SSRF confirmation

## Instructions

### Step 1: Update and Install Netcat

**Context**: Refresh package lists and install netcat to enable TCP listening inside the container.

**Command** ([[commands/apt-install-netcat]]):
```bash
apt update && apt install -y netcat
```

> This chained command updates the apt cache and installs netcat non-interactively. Expected output includes download progress and a success message like "netcat is already the newest version" or installation confirmation.

### Step 2: Verify Installation

**Context**: Confirm netcat is usable post-installation.

**Command** (nc version):
```bash
nc --version
```

> Output should display netcat version details, indicating successful installation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/apt-install-netcat]]

## Tools Used

- [[tools/Apt]]
- [[tools/Netcat]]

## Tags

- netcat
- installation
- apt
- gitlab
