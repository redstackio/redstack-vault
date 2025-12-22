---
id: 2886ade7-75e1-4fe7-9cd8-077bba4a2a79
name: guymager
type: tool
verified: true
created_at: '2019-08-28T21:17:28.523056+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - forensics
  - disk-imaging
  - media-acquisition
  - incident-response
url: 'http://guymager.org/'
validated: true
---

# guymager

**Status**: Unverified

## Overview

Guymager is an open-source digital forensic tool designed for efficient acquisition of storage media images. It is commonly used in incident response, digital investigations, and red team operations requiring preservation of compromised systems for offline analysis. Category: Digital Forensics.

## Description

Guymager provides a user-friendly GUI for creating forensic-quality images of hard drives, USB devices, and other media. It supports multiple output formats and leverages multi-threading for speed, making it suitable for time-sensitive acquisitions. While primarily defensive, it can be used offensively to image targets during post-exploitation for data extraction or evidence planting simulations.

## Features

- Easy-to-use GUI supporting multiple languages for accessibility.
- Optimized for Linux environments with multi-threaded imaging and compression.
- Full utilization of multi-core processors for faster acquisition times.
- Support for flat (dd/raw), EWF (EnCase E01), and AFF image formats.
- Disk cloning capabilities for direct duplication.
- Completely free and open-source under GNU GPL.
- Hash verification (MD5, SHA1, etc.) during imaging for integrity.

## Installation

### Requirements

- Linux distribution (e.g., Ubuntu, Kali, Debian).
- Sufficient disk space for output images (at least as large as the source media).
- Root privileges for accessing raw devices.

### Install Commands

```bash
# On Ubuntu/Debian/Kali
sudo apt update
sudo apt install guymager
```

For building from source:

```bash
# Install dependencies
sudo apt install qt5-default libewf-dev libafflib-dev
# Clone and build (from official repo)
git clone https://github.com/recovered/guymager.git
cd guymager
qmake
gmake
sudo make install
```

## Basic Usage

```bash
guymager --help
```

This displays available command-line options. Typically launched via GUI for interactive selection of devices.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -c, --config | Load configuration from file |
| -l, --logfile | Enable logging to specified file |
| -v, --version | Display version information |

## Examples

### Example 1: Basic Usage

```bash
guymager
```

Launches the GUI. Select a device (e.g., /dev/sda), choose output format (e.g., E01), specify destination, and start imaging.

### Example 2: Advanced Usage

```bash
guymager -c /path/to/config.ini -l /var/log/forensic.log
```

Loads custom settings and logs the session for audit purposes.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System (for acquiring system images in post-exploitation)
- [[Data from Removable Media]] Data from Removable Media (for imaging external drives)

### Tactics

- [[Collection]] Collection
- [[Exfiltration]] Exfiltration (when used to prepare data for transfer)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'guymager' executable.
- File system changes: Creation of large .E01, .dd, or .aff files in unusual locations.
- Disk I/O spikes on raw devices (/dev/sd*).
- Log entries in /var/log for guymager sessions.
- Network tools may not detect it directly, but monitor for USB/external drive mounts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/DD]] (command-line alternative for raw imaging)
- [[tools/ewf-tools]] (for handling EWF formats post-acquisition)
- [[tools/testdisk]] (for disk recovery and analysis)

## References

- Official website: http://guymager.org/
- GitHub repository: https://github.com/recovered/guymager
- Documentation: Included in the tool or available on SourceForge
