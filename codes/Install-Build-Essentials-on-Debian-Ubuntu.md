---
type: code
language: bash
verified: true
tags:
  - installation
  - dependencies
platforms:
  - Linux
validated: true
---

# Install-Build-Essentials-on-Debian-Ubuntu

## Code

```bash
apt update
apt install build-essential -y
```

## Description

This bash snippet updates the package repository and installs the build-essential meta-package, which includes gcc, g++, make, and other tools needed for compiling C/C++ programs like kernel exploits on Debian/Ubuntu systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; runs as-is with sudo if required | N/A |

## Usage

Execute this code directly in a terminal on the target system before compilation steps in privilege escalation procedures. Ideal for preparing environments for building POCs like Dirty Cow. If no sudo, it will prompt for password.

## Detection

- Package manager logs: Check /var/log/apt/history.log for build-essential installation.
- Process monitoring: apt processes running as non-root user.
- Network: Connections to Ubuntu/Debian mirrors for package downloads.

## Related

- [[procedures/Exploit-Dirty-Cow-Vulnerability]]
- [[commands/install-build-essential-debian-ubuntu]]
