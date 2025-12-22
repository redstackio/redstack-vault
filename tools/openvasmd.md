---
id: 2fb65b14-8cf1-48ae-bd0b-829eaa3dbfcb
type: tool
verified: true
description: >-
  The OpenVAS Manager Daemon (openvasmd) is the core service in the OpenVAS
  vulnerability scanning framework, responsible for managing scan tasks,
  handling the OpenVAS Management Protocol (OMP), and coordinating with other
  components like the scanner and feed synchronization services.
url: 'https://docs.greenbone.net/GSM-Manual/gos-22.04/en/starting-openvasmd.html'
created_at: '2019-08-28T21:17:28.746681+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - vulnerability-scanning
  - daemon
  - openvas
  - gvm
validated: true
---

# openvasmd

**Status**: Unverified

## Overview

openvasmd is the management daemon for OpenVAS (Open Vulnerability Assessment System), an open-source framework for vulnerability scanning and management. It handles the backend operations for creating, scheduling, and executing vulnerability scans, communicating via the OMP protocol. Commonly used in penetration testing and security assessments to identify vulnerabilities in networks and applications.

## Description

OpenVAS provides a comprehensive vulnerability management solution with over 50,000 Network Vulnerability Tests (NVTs) updated regularly. openvasmd serves as the central manager, integrating with components like ospd-openvas (the scanner) and gvmd (Greenbone Vulnerability Manager). It is part of the Greenbone Community Edition and is licensed under GNU GPL. Developments from Greenbone Networks' commercial products are contributed back to the open-source version.

## Features

- Management of scan tasks, targets, and credentials via OMP
- Integration with NVT feeds for up-to-date vulnerability checks
- Support for authenticated and unauthenticated scans
- Logging and reporting capabilities for scan results
- Configurable listening ports and IP bindings

## Installation

### Requirements

- Linux distribution (e.g., Ubuntu, Kali, Debian)
- PostgreSQL database for storing scan data
- Redis server for session management
- GVM libraries and dependencies (e.g., gvm-libs)

### Install Commands

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install gvm
# Or from source: follow Greenbone installation guide
sudo gvm-setup
```

On Kali Linux (pre-installed in some versions):

```bash
sudo apt install openvas
sudo gvm-setup
```

After installation, run `sudo gvm-setup` to initialize the database and create an admin user.

## Basic Usage

```bash
openvasmd --help
```

Typically, openvasmd is started as a system service:

```bash
sudo systemctl start openvasmd
sudo systemctl enable openvasmd
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--version` | Display version information |
| `--foreground` | Run in foreground for debugging |
| `--port=PORT` | Set listening port (default: 9390) |
| `--listen=IP` | Bind to specific IP address |
| `--http-only` | Use HTTP instead of HTTPS |

## Examples

### Example 1: Basic Usage

Start in foreground:

```bash
openvasmd --foreground
```

### Example 2: Advanced Usage

Start with custom port and IP binding:

```bash
openvasmd --foreground --port=9391 --listen=127.0.0.1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for openvasmd executable
- Network traffic on port 9390/TCP (OMP)
- Log entries in system journals for GVM services
- Database connections to PostgreSQL from gvmd/openvasmd

## Related Commands

- [[commands/openvasmd-start-foreground]]
- [[commands/openvasmd-version]]
- [[commands/openvasmd-help]]

## Related Tools

- [[tools/gvmd]]
- [[tools/ospd-openvas]]

## References

- Official documentation: https://docs.greenbone.net
- Greenbone Community Forum: https://forum.greenbone.net
- Source repository: https://github.com/greenbone/gvmd
