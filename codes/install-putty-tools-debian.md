---
type: code
language: bash
verified: true
platforms:
  - Linux
tags:
  - install
  - putty
  - debian
validated: true
---

# install-putty-tools-debian

## Code

```bash
apt update && apt install putty-tools -y
```

## Description

This bash snippet updates the package index and installs the putty-tools package on Debian-based Linux distributions like Ubuntu or Kali Linux. Putty-tools provides utilities including puttygen for key management and conversion tasks in SSH workflows.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | No variables; runs as-is on systems with apt | N/A |

## Usage

Execute this code as root or with sudo in a terminal before using puttygen for key conversions. It is a prerequisite for procedures involving PuTTY key handling on Linux, such as preparing SSH keys for remote access in security testing.

## Detection

- Package manager logs (e.g., /var/log/apt/history.log) showing putty-tools installation.
- Process monitoring for apt processes during execution.
- Endpoint detection rules for unauthorized package installations.

## Related

- [[procedures/Convert-PuTTY-PPK-to-OpenSSH-PEM]]
- [[tools/puttygen]]
