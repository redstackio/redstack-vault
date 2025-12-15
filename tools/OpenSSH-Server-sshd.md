---
id: tool-openssh-sshd-001
url: 'https://www.openssh.com/'
tags:
  - ssh
  - demo-service
  - ssrf-target
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:10.132Z'
validated: true
submitted: true
---
# OpenSSH-Server-sshd

**Status**: Unverified

## Overview

OpenSSH Server (sshd) is a secure shell server for remote login and command execution, used here as a demo internal service on localhost port 2222 to demonstrate SSRF detection and version leakage in phpBB exploitation scenarios.

## Description

sshd provides encrypted SSH connections and can be configured in debug mode to log or respond with version information upon connection attempts. In security testing, it's hosted internally to simulate vulnerable internal resources that SSRF can probe, revealing open ports and banners via error responses. Common in Linux environments, it's ideal for port scanning demos due to its standard deployment.

## Features

- Feature 1: Secure remote access via SSH protocol
- Feature 2: Debug mode for verbose logging of incoming connections
- Feature 3: Version banner exposure in responses for enumeration

## Installation

### Requirements

- Linux OS (e.g., Ubuntu)
- Root or sudo access

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install openssh-server

# Start and enable
sudo systemctl start ssh
sudo systemctl enable ssh
```

## Basic Usage

```bash
sshd -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Debug mode for verbose output |
| `-p 2222` | Bind to specific port |
| `-f /path/to/sshd_config` | Custom config file |

## Examples

### Example 1: Basic Usage

```bash
sudo sshd -p 2222
```

Run on localhost to listen on port 2222.

### Example 2: Advanced Usage

```bash
sudo sshd -d -p 2222 -f /etc/ssh/sshd_config_debug
```

Debug mode to log connections and expose versions.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (as target for scanning)

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing connections to port 2222
- Process monitoring for sshd instances on non-standard ports
- Debug logs revealing unauthorized probes

## Related Procedures

- [[procedures/Analyze-SSRF-Response-for-Service-Detection]]

## Related Tools

- [[tools/MySQL-Server]] (alternative demo service)

## References

- Official documentation: https://www.openssh.com/manual.html
- Related resources: SSH configuration for security testing
