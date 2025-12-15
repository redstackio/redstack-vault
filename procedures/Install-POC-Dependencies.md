---
tags:
  - setup
  - dependencies
type: procedure
tools:
  - '[[tools/pip]]'
  - '[[tools/pycryptodome]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/pip3-install-pycryptodome]]'
  - '[[commands/pip3-install-pycryptodomex]]'
platforms:
  - Linux
techniques:
  - '[[Audio Capture]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4a1c2ab6-3266-48e9-853f-b01a9ee8a2b3
created_at: '2025-12-14T17:23:27.560Z'
updated_at: '2025-12-14T17:23:27.560Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Audio Capture]]'
---
# Install-POC-Dependencies

## Summary

This procedure installs the necessary Python libraries to resolve import errors in the PrimeFaces exploitation POC script, ensuring it can handle cryptographic operations like MD5 hashing for payload generation.

## Description

The primefaces.py script requires the Crypto.Hash module for deserialization payload crafting. On a Linux environment with Python 3.6+, use pip to install pycryptodome. If conflicts occur (e.g., with existing pycrypto), fall back to pycryptodomex. This setup is crucial before execution to avoid runtime errors during the RCE attempt on the target Tomcat server.

## Requirements

1. Python 3.6 or higher installed
2. pip package manager available
3. Local execution environment (e.g., Kali Linux)

## Defense

Defensive measures and detection strategies:

- Monitor package installations in controlled environments
- Use virtual environments to isolate dependency installs
- Scan for unauthorized Python library usage in attack toolchains

## Objectives

1. Resolve Crypto.Hash import dependencies
2. Ensure POC script compatibility
3. Minimize setup errors for smooth exploitation

## Instructions

### Step 1: Install Primary Dependency

**Context**: Install pycryptodome to provide the required Crypto module.

**Command** ([[commands/pip3-install-pycryptodome]]):
```bash
pip3 install pycryptodome
```

> This command fetches and installs the library; expect output confirming successful installation and no errors.

### Step 2: Alternative Installation if Needed

**Context**: If the primary install fails due to compatibility, use the alternative library.

**Command** ([[commands/pip3-install-pycryptodomex]]):
```bash
pip3 install pycryptodomex
```

> Similar output to primary; test by importing in Python to verify.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Audio Capture]]

### Sub-Techniques


## Commands Used

- [[commands/pip3-install-pycryptodome]]
- [[commands/pip3-install-pycryptodomex]]

## Tools Used

- [[tools/pip]]
- [[tools/pycryptodome]]

## Tags

- [[setup]]
- [[dependencies]]
