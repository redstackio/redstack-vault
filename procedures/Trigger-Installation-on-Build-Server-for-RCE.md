---
id: proc-003
tags:
  - rce
  - execution
  - jenkins
  - pip
type: procedure
tools:
  - '[[tools/pip]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/pip-install-package]]'
verified: false
platforms:
  - Linux
  - Cloud (AWS)
  - Build Servers
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Python]]'
updated_at: '2025-12-14T17:24:17.653Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Python]]'
---
---
# Trigger-Installation-on-Build-Server-for-RCE

## Summary

This procedure exploits misconfigured pip settings on build servers to install a malicious package from public PyPI, executing embedded code in setup.py for remote code execution and data exfiltration.

## Description

Build servers like Jenkins on AWS use pip without specifying an internal index, causing fallback to public PyPI. When a project depends on an internal package like 'yelp-cgeom', it installs the attacker's version, running setup.py which sends a callback with server details (e.g., IP 54.71.19.248, hostname 10-81-21-60-uswest2bdevc.uswest2-devc.yelpcorp.com).

## Requirements

1. Malicious package already uploaded to PyPI.
2. Target build server with dependency on the unclaimed package.
3. Callback server to receive exfiltrated data.

## Defense

Defensive measures and detection strategies:

- Configure /etc/pip.conf with internal index-url and no public fallback.
- Use Docker images with pre-configured pip settings.
- Monitor for anomalous network calls from build servers (e.g., outbound to unknown IPs).

## Objectives

1. Force installation of malicious package during build.
2. Achieve RCE via setup.py execution.
3. Exfiltrate build server environment details.

## Instructions

### Step 1: Simulate or Wait for Build Trigger

**Context**: The installation happens automatically in CI/CD; no direct command from attacker.

On victim side (misconfigured): Use [[commands/pip-install-package]] in build script:

```bash
pip install yelp-cgeom
```

> Due to no --index-url, fetches from public PyPI, executes setup.py. Expected output: Callback to attacker server on Wed Jul 29 2020 04:27:23 GMT from /ephemeral/tmpdir/pip-install-o6jnSv/yelp-cgeom.

### Step 2: Monitor Callback

**Context**: Receive and log the exfiltrated data.

No command; use server logs.

> Success: Details include AWS IP and Yelp hostname.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Python]] Python

### Sub-Techniques


## Commands Used

- [[commands/pip-install-package]]

## Tools Used

- [[tools/pip]]

## Tags

- [[rce]]
- [[jenkins]]
---
