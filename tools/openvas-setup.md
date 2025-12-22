---
id: ee83131e-ed5e-4e9d-aeba-a856385817a6
type: tool
verified: true
description: >-
  The openvas-setup script initializes and configures the OpenVAS vulnerability
  scanning framework, including feed synchronization and database setup.
url: 'https://greenbone.github.io/docs/latest/22.4/source-build/index.html'
created_at: '2019-08-28T21:17:33.260288+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - vulnerability-scanning
  - setup
  - openvas
  - gvm
commands:
  - '[[commands/openvas-setup-run]]'
validated: true
---

# openvas-setup

**Status**: Unverified

## Overview

openvas-setup is a command-line script used to initialize and configure the OpenVAS (Open Vulnerability Assessment System) framework, which is part of the Greenbone Vulnerability Management (GVM) suite. It performs essential setup tasks such as downloading and synchronizing vulnerability test feeds (NVTs), configuring the PostgreSQL database, creating system users and roles, and generating an administrative account for the web interface. This tool is crucial for preparing OpenVAS for vulnerability scanning operations in security assessments, typically run once after installation.

## Description

OpenVAS provides a comprehensive, open-source vulnerability scanning and management solution. The openvas-setup script automates the initial configuration, ensuring that the scanner has up-to-date vulnerability data from over 50,000 Network Vulnerability Tests (NVTs). It integrates services like the OpenVAS Scanner, Greenbone Vulnerability Manager (GVMd), and Greenbone Security Assistant (GSA) for web-based management. Developments are contributed from Greenbone Networks' commercial products, and all components are licensed under the GNU GPL. This setup tool is particularly useful in red teaming for reconnaissance and vulnerability identification phases.

## Features

- Automatic synchronization of vulnerability feeds (NVTs, SCAP, CERT data)
- Database initialization and user/role creation for GVM services
- Generation of secure admin credentials for GSA access
- Integration with system services (systemd on modern Linux)
- Support for full or incremental feed updates post-setup

## Installation

### Requirements

- Linux distribution with PostgreSQL support (e.g., Ubuntu, Kali Linux)
- Root or sudo access
- Internet connection for feed downloads
- Approximately 2-5 GB of disk space for feeds and database

### Install Commands

OpenVAS and openvas-setup are typically installed via package managers. On Debian-based systems:

```bash
# Update package list
sudo apt update

# Install OpenVAS (includes openvas-setup)
sudo apt install openvas

# Or for the full GVM suite (recommended for newer versions)
sudo apt install gvm
```

On Kali Linux, OpenVAS is available in the repositories:

```bash
sudo apt update
sudo apt install openvas
```

After installation, run the setup:

```bash
sudo openvas-setup
```

For source builds, follow the official Greenbone documentation, which involves compiling GVM components.

## Basic Usage

```bash
sudo openvas-setup
```

This runs the full initialization process. Monitor the output for progress on feed downloads and service configuration.

### Common Options

The script itself has no command-line options; it is a non-interactive setup process. For feed management post-setup, use companion tools like `greenbone-nvt-sync`.

| Option | Description |
|--------|-------------|
| N/A | The script runs without flags; use `--help` not applicable |

## Examples

### Example 1: Basic Usage

```bash
sudo openvas-setup
```

Expected result: Setup completes with admin login details printed to the console.

### Example 2: Post-Setup Feed Update

After initial setup, update feeds manually if needed:

```bash
sudo greenbone-nvt-sync
sudo greenbone-feed-sync --type SCAP
sudo greenbone-feed-sync --type CERT
```

Then restart services:

```bash
sudo gvm-stop
sudo gvm-start
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information (via vulnerability scanning setup)
- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of OpenVAS services in process lists (e.g., `ps aux | grep openvas`)
- PostgreSQL databases named `gvmd` or `openvas`
- Network traffic to Greenbone feed servers (e.g., feed.community.greenbone.net)
- Log entries in `/var/log/gvm/` for setup activities

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]] (for complementary port scanning)
- [[tools/nessus]] (commercial alternative vulnerability scanner)

## References

- Official Greenbone Documentation: https://greenbone.github.io/docs/
- OpenVAS User Manual: https://docs.greenbone.net/
- GitHub Repository: https://github.com/greenbone/gvm-libs
