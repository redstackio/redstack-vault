---
id: 99f1773a-1e65-4795-b456-1450696ee8a2
type: tool
verified: true
created_at: '2019-08-28T21:17:36.049571+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - vulnerability-scanner
  - reconnaissance
  - openvas
url: 'https://www.openvas.org/'
commands:
  - '[[commands/openvas-setup-initialize]]'
  - '[[commands/start-openvas-services]]'
  - '[[commands/create-openvas-admin-user]]'
validated: true
---

# openvassd

**Status**: Unverified

## Overview

openvassd is the core scanner daemon of the OpenVAS (Open Vulnerability Assessment System) framework, a full-featured vulnerability scanner used for identifying security issues in networks, hosts, and applications. It performs the actual scanning tasks based on Network Vulnerability Tests (NVTs) and is commonly used in penetration testing, compliance audits, and vulnerability management.

## Description

OpenVAS is an open-source framework consisting of multiple services and tools for comprehensive vulnerability scanning and management. The openvassd component specifically handles the execution of vulnerability tests, processing scan configurations from the Greenbone Vulnerability Manager (gvmd), and generating reports. Developments are contributed from Greenbone Networks' commercial solutions to the open-source community since 2009. It supports over 50,000 NVTs, regularly updated, and is licensed under GNU GPL. The tool is ideal for automated scanning in red team operations to discover exploitable weaknesses before manual exploitation.

## Features

- Feature 1: Executes thousands of NVTs for comprehensive vulnerability detection across protocols like HTTP, SSH, SMB, and more.
- Feature 2: Supports authenticated and unauthenticated scans for deeper host inspection.
- Feature 3: Integrates with GVM for task scheduling, report generation in various formats (PDF, XML, HTML), and web-based management via Greenbone Security Assistant (GSA).
- Feature 4: Scalable daemon architecture for handling multiple concurrent scans.

## Installation

### Requirements

- Linux distribution with package manager (e.g., Debian-based like Ubuntu or Kali Linux).
- Root or sudo access.
- Sufficient disk space for feed updates (several GB).
- PostgreSQL database support.

### Install Commands

```bash
# On Kali Linux (pre-built packages)
sudo apt update
sudo apt install gvm

# Initialize after installation
sudo openvas-setup
```

For Ubuntu:
```bash
sudo add-apt-repository ppa:mrazavi/gvm
sudo apt update
sudo apt install gvm
```

After installation, run `sudo openvas-setup` to download feeds and configure the database.

## Basic Usage

```bash
sudo gvm-start
```

This starts all services, including openvassd. Access the web interface at https://127.0.0.1:9392 using the admin credentials generated during setup.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help for the daemon or related tools |
| --verbose | Enable verbose logging for troubleshooting |
| --config-file=PATH | Specify custom configuration file |

## Examples

### Example 1: Basic Usage

After setup, start services:
```bash
sudo gvm-start
```

Log in to the web UI, create a scan task targeting a host, and launch it. openvassd will perform the scan in the background.

### Example 2: Advanced Usage

Create an admin user and start services:
```bash
sudo gvmd --create-user=admin --new-password=SecurePass123
sudo gvm-start
```

Configure a scheduled scan via the web interface for ongoing vulnerability monitoring.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic showing multiple TCP connections from the scanner IP to target ports (e.g., 22, 80, 443) with vulnerability probe signatures.
- Detection method 2: Process monitoring for openvassd or gvmd running on the attacker's system; log files in /var/log/gvm.
- Detection method 3: IDS/IPS alerts for known NVT probe patterns, such as specific HTTP User-Agent strings like "OpenVAS".

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[Nessus]]

## References

- Official documentation: https://docs.greenbone.net/
- GitHub repository: https://github.com/greenbone/openvas-scanner
