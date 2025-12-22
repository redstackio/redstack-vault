---
id: e3856426-3066-4792-90a5-52d630af9a46
type: tool
verified: true
created_at: '2019-08-28T21:17:21.974131+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - openvas
  - vulnerability-management
  - feed-sync
  - scanning
url: 'https://www.openvas.org/'
validated: true
---

# openvas-feed-update

**Status**: Unverified

## Overview

openvas-feed-update is a utility script within the OpenVAS (Open Vulnerability Assessment System) framework used to synchronize and update the vulnerability feeds. OpenVAS is an open-source vulnerability scanner that provides comprehensive scanning and management capabilities. This specific tool ensures that the scanner's database of Network Vulnerability Tests (NVTs), SCAP data, and CERT feeds remains current, enabling detection of the latest vulnerabilities.

It is commonly used in security operations to maintain an up-to-date vulnerability assessment environment before running scans.

## Description

OpenVAS is a full-featured vulnerability scanner developed as part of the Greenbone Community Edition. The openvas-feed-update script handles the periodic synchronization of over 50,000 NVTs from the Greenbone Community Feed. These feeds include vulnerability tests, security content automation protocol (SCAP) data for compliance checks, and CERT advisories for emerging threats.

The tool is essential for environments using OpenVAS for regular vulnerability assessments, as outdated feeds can lead to false negatives in scans. It supports automated updates and is typically run as a cron job in production setups. All components are licensed under the GNU General Public License (GPL).

## Features

- Automatic synchronization of NVT feeds (vulnerability tests)
- Updates SCAP data for configuration and compliance auditing
- Syncs CERT data for the latest security advisories
- Progress reporting during downloads
- Integration with OpenVAS scanner for seamless use
- Support for community and enterprise feeds

## Installation

### Requirements

- OpenVAS framework installed (version 9 or later; note: newer versions use greenbone-feed-sync)
- Root or sudo access for writing to /var/lib/openvas/
- Internet access to https://feed.community.greenbone.net/
- Approximately 1-2 GB of free disk space for feeds

### Install Commands

OpenVAS installation is required first. On Debian/Ubuntu-based systems (e.g., Kali Linux):

```bash
# Update system and install OpenVAS
sudo apt update
sudo apt install openvas

# Initialize OpenVAS (includes setup of openvas-feed-update)
sudo openvas-setup

# The openvas-feed-update script is installed as part of the openvas package
```

For manual installation or verification:

```bash
# Check if script exists
which openvas-feed-update

# If missing, ensure openvas is fully installed
sudo apt install --reinstall openvas
```

On other Linux distributions, use the appropriate package manager or compile from source via the official Greenbone repository.

## Basic Usage

```bash
openvas-feed-update --help
```

This displays available options (though the command is primarily parameterless for full sync).

### Common Options

| Option | Description |
|--------|-------------|
| None (default) | Performs full sync of all feeds |
| --help | Shows usage information |
| --verbose | Increases output verbosity (if supported in version) |

## Examples

### Example 1: Basic Usage

```bash
sudo openvas-feed-update
```

This downloads and updates all feeds. Run as root to ensure proper permissions.

### Example 2: Advanced Usage

For logging the update process:

```bash
sudo openvas-feed-update > /var/log/openvas-feed-update.log 2>&1
```

Schedule via cron for daily updates:

```bash
# Edit crontab
sudo crontab -e

# Add line for daily update at 2 AM
0 2 * * * /usr/sbin/openvas-feed-update > /var/log/openvas-feed.log 2>&1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information (used in reconnaissance phases for vulnerability assessment)
- [[Active Scanning]] Active Scanning (facilitates vulnerability scanning by maintaining feed data)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for openvas-feed-update executions
- Network traffic to feed.community.greenbone.net on port 443
- Log entries in /var/log/openvas/ for feed sync activities
- Disk I/O in /var/lib/openvas/ directories during updates
- Cron job entries referencing the script

## Related Procedures

- [[procedures/Update-Vulnerability-Feeds-for-Scanning]]
- [[procedures/Configure-OpenVAS-Scanner]]

## Related Tools

- [[tools/openvas]]
- [[tools/greenbone-feed-sync]] (successor in newer versions)

## References

- Official OpenVAS Documentation: https://docs.greenbone.net/
- Greenbone Community Feed: https://feed.community.greenbone.net/
- GitHub Repository: https://github.com/greenbone/openvas-scanner
