---
type: tool
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - vulnerability-scanning
  - certificate-management
  - openvas
url: >-
  https://greenbone.github.io/docs/latest/22.4/source-build/html/chapter-setup.html
validated: true
---

# openvas-manage-certs

**Status**: Unverified

## Overview

openvas-manage-certs is a utility script for managing SSL/TLS certificates in OpenVAS (Open Vulnerability Assessment System), a full-featured vulnerability scanner. It handles the creation, deletion, and maintenance of self-signed certificates needed for secure HTTPS communication between OpenVAS services like the Greenbone Security Assistant (GSA) web interface and the scanner backend. This tool is essential during initial setup and reconfiguration to ensure encrypted connections.

## Description

As part of the OpenVAS framework, which is an open-source fork of Nessus, openvas-manage-certs simplifies certificate lifecycle management. It generates a Certificate Authority (CA) and service-specific certificates (for GSA, scanner, and user access), stores them in standard locations like /var/lib/gvm/CA/, and integrates with OpenVAS services. Commonly used in penetration testing and vulnerability assessment environments to set up secure scanning infrastructures without relying on external certificate authorities.

## Features

- **Certificate Generation**: Creates self-signed CA and service certificates with appropriate key lengths and validity periods.
- **Certificate Deletion**: Safely removes all managed certificates for cleanup or reset.
- **Integration**: Automatically configures paths for OpenVAS components like GSA and gvmd.
- **Help and Validation**: Provides usage help and verifies certificate status during operations.

## Installation

### Requirements

- OpenVAS or GVM (Greenbone Vulnerability Management) packages installed.
- Root or sudo access for certificate file operations.
- Perl (as the script is Perl-based).

### Install Commands

```bash
# On Kali Linux (pre-installed with OpenVAS)
sudo apt update && sudo apt install openvas

# On Ubuntu
sudo add-apt-repository ppa:mrazavi/gvm
sudo apt update
sudo apt install gvm

# Post-installation setup (includes running openvas-manage-certs)
sudo gvm-setup
```

After installation, openvas-manage-certs is available in /usr/sbin/. Run `sudo gvm-setup` to initialize, which invokes this tool.

## Basic Usage

```bash
openvas-manage-certs --help
```

Displays available options for certificate management.

### Common Options

| Option | Description |
|--------|-------------|
| `-c, --create` | Generate new self-signed certificates |
| `-D, --delete` | Delete all existing certificates |
| `-h, --help` | Show usage help |

## Examples

### Example 1: Basic Usage - Create Certificates

```bash
sudo openvas-manage-certs -c
```

This generates all necessary certificates. Expected output confirms creation or skips if already present.

### Example 2: Advanced Usage - Delete and Recreate

```bash
sudo openvas-manage-certs -D
sudo openvas-manage-certs -c
```

Deletes old certificates and creates fresh ones, useful for troubleshooting connection issues.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning: Used to set up vulnerability scanning infrastructure, enabling reconnaissance techniques like [[Search Open Technical Databases]] Network Trust Dependencies for certificate validation in scans.

### Tactics

- [[Reconnaissance]] Reconnaissance: Facilitates secure setup for vulnerability assessment tools.

## Detection

Indicators and methods for detecting this tool's usage:

- Log entries in /var/log/gvm/gvmd.log for certificate operations.
- Presence of certificate files in /var/lib/gvm/CA/ with recent timestamps.
- Process monitoring for openvas-manage-certs executions via ps aux | grep openvas.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/openvas]]
- [[tools/gvm]]

## References

- Official Greenbone Documentation: https://greenbone.github.io/docs/
- OpenVAS Setup Guide: https://greenbone.github.io/docs/latest/22.4/source-build/html/chapter-setup.html
