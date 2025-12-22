---
id: 24d1fbde-3e82-4469-843f-bbf93ebdfc79
type: tool
verified: true
created_at: '2019-08-28T21:17:38.360098+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - scanning
  - service-identification
url: 'http://www.thc.org/thc-amap/'
validated: true
---

# amap

**Status**: Unverified

## Overview

Amap is an advanced application identification tool designed for penetration testers. It identifies services and applications running on network ports, even if they are not using standard ports or are non-ASCII based. Amap is useful during reconnaissance phases to map the attack surface by detecting misconfigurations or unexpected services.

Category: Reconnaissance

## Description

Amap operates by sending specially crafted trigger packets to target ports and matching the responses against a database of known application signatures. This allows it to detect applications like HTTP servers on non-standard ports or proprietary protocols. Unlike traditional port scanners like Nmap, Amap focuses on application-layer identification rather than just port status. It supports both TCP and UDP probing and can handle SSL/TLS connections. Note that Amap is an older tool (originally released around 2002) and may require compilation from source on modern systems, as it is not actively maintained.

Supported Platforms: Linux, Unix-like systems

## Features

- Application identification beyond standard ports
- Support for non-ASCII protocols
- Trigger-based response matching
- SSL/TLS probing
- Output to files for analysis
- Modular database for custom signatures

## Installation

### Requirements

- GCC compiler
- Make utility
- Standard Unix tools (awk, grep, etc.)

### Install Commands

Amap is not available in standard repositories like apt on Ubuntu. Download and compile from source:

```bash
# Download from official source (if available) or GitHub mirrors
wget http://www.thc.org/releases/amap-5.4.tar.gz

tar -xzf amap-5.4.tar.gz
cd amap-5.4
./configure
make
sudo make install

# On Kali Linux, it may be available via source compilation or third-party repos
# Alternative: Use a mirror like https://github.com/parsiya/amap
```

For Ubuntu/Debian:

```bash
# Install dependencies
sudo apt update
sudo apt install build-essential

# Then follow the download and compile steps above
```

## Basic Usage

```bash
amap --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -b | Probe both TCP and UDP |
| -S | Enable SSL probing |
| -p | Specify ports (e.g., -p 80,443) |
| -o | Output to file |
| -q | Quiet mode (suppress banner) |
| -d | Debug mode |

## Examples

### Example 1: Basic Usage

Scan common web ports on a target:

```bash
amap -b -p 80,443 target.example.com
```

### Example 2: Advanced Usage

Full port range scan with SSL support and output to file:

```bash
amap -b -S -o results.txt -p 1-1024 192.168.1.100
```

## Related Commands

- [[commands/amap-basic-application-scan]]
- [[commands/amap-ssl-application-scan]]
- [[commands/amap-output-to-file]]

## References

- Official THC page: http://www.thc.org/thc-amap/
- GitHub mirror: https://github.com/parsiya/amap (for modern compatibility patches)
