---
id: c78e3206-6150-4b22-997f-77b9568303c6
type: tool
verified: true
created_at: '2019-08-28T21:17:19.706086+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - configuration-audit
  - network-security
  - device-audit
url: 'https://github.com/nipper-ng/nipper-ng'
validated: true
---

# nipper-ng

**Status**: Unverified

## Overview

Nipper-ng is an open-source security auditing tool for analyzing network device configurations, such as routers, firewalls, and switches. It identifies misconfigurations, weak security settings, and potential vulnerabilities by parsing config files from various vendors.

## Description

As a fork of the original Nipper tool (version 0.11.10 under GNUv3 GPL), Nipper-ng remains free and focuses on generating detailed reports on security observations. It supports multiple device types including Cisco IOS, Juniper Junos, Check Point, and more, making it ideal for red teamers to understand defensive postures or for blue teams to audit infrastructure.

## Features

- Feature 1: Parses configuration files from 20+ vendors and device types
- Feature 2: Generates reports in TXT, HTML, PDF, and CSV formats with risk ratings
- Feature 3: Highlights issues like weak authentication, open services, and access control problems
- Feature 4: Supports batch processing for multiple configs
- Feature 5: Customizable output with warnings, recommendations, and compliance checks

## Installation

### Requirements

- CMake 3.0+
- GCC or Clang compiler
- libxml2 development libraries

### Install Commands

```bash
# Clone the repository
sudo apt update
sudo apt install cmake build-essential libxml2-dev

git clone https://github.com/nipper-ng/nipper-ng.git
cd nipper-ng

# Build and install
mkdir build && cd build
cmake ..
make
sudo make install
```

For Kali Linux: Pre-built packages may be available via `apt install nipper-ng` if in repos; otherwise, build from source.

## Basic Usage

```bash
nipper-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --input | Specify input config file |
| -o, --output | Specify output report file |
| -f, --format | Output format (txt, html, pdf, csv) |
| -d, --device-type | Specify device type (e.g., cisco-ios) |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

```bash
nipper-ng --input device_config.txt --output report.txt
```

### Example 2: Advanced Usage

```bash
nipper-ng --input firewall.cfg --device-type checkpoint --format html --output audit.html --warnings-only
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information (for config reconnaissance)
- [[Network Service Scanning]] Network Service Scanning (indirect via config analysis)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: File system scans for nipper-ng binary or GitHub repo clones
- Detection method 2: Process monitoring for 'nipper-ng' executions
- Detection method 3: Network logs showing downloads from GitHub

## Related Procedures

- [[procedures/Audit-Network-Device-Config]]
- [[procedures/Generate-Config-Audit-Report]]

## Related Tools

- [[tools/Nessus]]
- [[tools/openvas]]

## References

- Official GitHub: https://github.com/nipper-ng/nipper-ng
- Original Nipper project: https://sourceforge.net/projects/nipper/

*Last updated: 2023-10-01*
