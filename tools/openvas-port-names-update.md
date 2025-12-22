---
id: e01390a7-7acc-44a0-8fbb-1710353e2f01
type: tool
verified: true
created_at: '2019-08-28T21:17:29.947202Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - vulnerability-scanning
  - openvas
  - nmap-sync
url: >-
  https://greenbone.github.io/docs/latest/22.4/source-build/html/chapter-manage.html
validated: true
---

# openvas-port-names-update

**Status**: Unverified

## Overview

openvas-port-names-update is a utility script within the OpenVAS (now part of Greenbone Vulnerability Management - GVM) framework. It updates the internal port names database by synchronizing with Nmap's official services file, ensuring that vulnerability scans accurately identify services running on discovered ports. This tool is essential for maintaining the precision of scan results in reconnaissance and vulnerability assessment phases of security testing.

## Description

OpenVAS is an open-source vulnerability scanner that relies on a comprehensive set of Network Vulnerability Tests (NVTs) for detecting weaknesses. The port names update script bridges OpenVAS with Nmap's port-service mappings, pulling the latest data to reflect new or renamed services. This prevents false negatives in service detection during scans. It is particularly useful in red team environments where accurate reconnaissance is critical before exploitation attempts. The script is Free Software under the GNU GPL and integrates seamlessly with GVM installations.

## Features

- Automatic synchronization with Nmap's services file
- Updates OpenVAS's internal port database without manual intervention
- Logging of update status and any discrepancies
- Integration with GVM's feed update processes
- Supports over 50,000 NVTs by ensuring service accuracy

## Installation

### Requirements

- OpenVAS/GVM installed (version 20.08 or later recommended)
- Root or sudo access for database modifications
- Internet access to fetch Nmap services file
- Python 3 and standard libraries (included in GVM)

### Install Commands

The script is included with OpenVAS/GVM installations. For a full setup on Ubuntu/Debian:

```bash
# Install GVM/OpenVAS
sudo apt update
sudo apt install gvm

# Initialize GVM (includes portnames-update script)
sudo gvm-setup

# The script is located at /usr/share/gvm/openvas-portnames-update or similar
```

For Kali Linux:

```bash
# Pre-installed or via
sudo apt install openvas
sudo gvm-setup
```

For manual installation from source:

```bash
# Clone GVM repositories
git clone https://github.com/greenbone/gvmd.git
cd gvmd
# Follow build instructions, script is in tools/
make install
```

## Basic Usage

```bash
openvas-portnames-update --help
```

This displays available options, though the script primarily runs without arguments.

### Common Options

| Option | Description |
|--------|-------------|
| `--help` or `-h` | Show help message and exit |
| `--verbose` or `-v` | Enable verbose logging during update |
| `--force` | Force update even if no changes detected |

## Examples

### Example 1: Basic Usage

```bash
sudo openvas-portnames-update
```

Runs the update as root, syncing the port names database.

### Example 2: Advanced Usage

```bash
sudo openvas-portnames-update --verbose --force
```

Performs a forced verbose update, useful for troubleshooting or ensuring latest data.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for accurate service enumeration in vulnerability assessment)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'openvas-portnames-update' execution
- Network traffic to Nmap services file sources (e.g., nmap.org)
- Log entries in GVM/OpenVAS sync logs indicating port database updates
- File modifications in OpenVAS data directories (e.g., /var/lib/openvas)

## Related Procedures

- [[procedures/update-openvas-feeds-and-sync]]
- [[procedures/run-openvas-vulnerability-scan]]

## Related Tools

- [[tools/openvas]]
- [[tools/Nmap]]

## References

- Official Greenbone Documentation: https://greenbone.github.io/docs/
- Nmap Services File: https://svn.nmap.org/nmap/nmap-services
- GVM Source Repository: https://github.com/greenbone
