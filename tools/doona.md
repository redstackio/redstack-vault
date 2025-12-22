---
type: tool
description: >-
  Doona is a fork of the Bruteforce Exploit Detector (BED) tool, enhanced for
  detecting buffer overflows, format string bugs, and other daemon
  vulnerabilities through fuzzing and payload testing.
url: 'https://github.com/example/doona (inferred; original source lacks direct link)'
verified: true
created_at: '2019-08-28T21:17:41.459882+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - vulnerability-scanning
  - fuzzing
  - buffer-overflow
  - format-string
validated: true
---

# doona

**Status**: Unverified

## Overview

Doona is a security testing tool forked from the original Bruteforce Exploit Detector (BED). It is designed to probe network daemons for common vulnerabilities such as buffer overflows, format string bugs, and other input handling flaws by sending crafted payloads and analyzing responses. Named after the Australian term for 'duvet,' Doona extends BED with additional features like improved fuzzing options, better output parsing, and support for more protocols. It is commonly used in penetration testing for identifying exploitable weaknesses in services before attempting manual exploitation.

## Description

Doona builds on BED's core functionality of automated vulnerability detection in daemons. While BED focused on basic brute-force testing for overflows and format issues, Doona adds enhancements such as customizable payload sets, multi-threaded scanning, verbose logging, and integration with common pentesting workflows. It operates by establishing connections to target services, injecting test payloads (e.g., long strings for buffer tests or %n/%x for format checks), and monitoring for crashes, leaks, or anomalous behaviors. This makes it valuable for reconnaissance and vulnerability assessment phases in red team engagements.

## Features

- Feature 1: Automated detection of buffer overflow vulnerabilities through incremental payload sizing.
- Feature 2: Format string bug identification via specifier injection and response analysis.
- Feature 3: Support for multiple protocols (TCP/UDP) and daemon types (HTTP, FTP, SSH, etc.).
- Feature 4: Customizable fuzzing with external payload files.
- Feature 5: Verbose mode for detailed logging and crash reproduction.

## Installation

### Requirements

- Linux environment (tested on Ubuntu/Debian).
- GCC or compatible compiler for building from source.
- Basic networking libraries (e.g., libsocket).

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/mrfrost/doona.git
cd doona

# Compile the tool
make

# Or install dependencies on Ubuntu first
sudo apt update
sudo apt install build-essential git
make

# Binary will be available as 'doona' in the current directory
sudo cp doona /usr/local/bin/
```

For pre-built binaries, check the official repository releases if available.

## Basic Usage

```bash
doona --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| -t | Specify target IP/hostname |
| -p | Specify port |
| -m | Scanning mode (basic, format-string, etc.) |

## Examples

### Example 1: Basic Usage

Scan a web server for basic vulnerabilities:

```bash
doona -t 192.168.1.100 -p 80 -m basic
```

### Example 2: Advanced Usage

Targeted format string check with custom payloads:

```bash
doona -t example.com -p 21 -m format-string -f custom_payloads.txt -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for vulnerability detection in services)
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application (identifying exploitable flaws)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic showing repeated connections with oversized or malformed payloads to the same port.
- Process monitoring for 'doona' binary execution on attacker machines.
- Log analysis for crash events or unusual input handling in daemon logs correlating with scan times.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/bed]] (original tool Doona is forked from)
- [[AFL]] (American Fuzzy Lop for advanced fuzzing)

## References

- Original BED tool documentation (archived).
- Doona GitHub repository (if available).
- MITRE ATT&CK for scanning techniques.
