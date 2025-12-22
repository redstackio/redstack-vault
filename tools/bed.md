---
id: 97a1655b-5249-40e5-acdd-47c847b296d6
type: tool
verified: true
created_at: '2019-08-28T21:17:37.105304+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - fuzzing
  - vulnerability-scanner
  - exploitation
url: 'https://github.com/infodox/bed'
validated: true
---

# bed

**Status**: Unverified

## Overview

BED (Bruteforce Exploit Detector) is a security tool designed to automatically detect potential vulnerabilities in network daemons, such as buffer overflows, format string issues, and other input-related flaws. It is commonly used in penetration testing for fuzzing services to identify exploitable conditions without manual payload crafting.

## Description

BED operates by sending a series of brute-force payloads to a target service over a specified port, monitoring responses for signs of crashes, memory leaks, or anomalous behavior. It supports various protocols and can be configured for specific vulnerability types. This tool is particularly useful during vulnerability assessment phases to quickly triage services for deeper exploitation attempts. Originally developed for Unix-like systems, it integrates well with Kali Linux environments.

## Features

- Feature 1: Automated fuzzing for buffer overflows with configurable payload sizes
- Feature 2: Format string vulnerability detection using specifiers like %x and %n
- Feature 3: Support for multiple protocols (TCP/UDP) and timeout handling
- Feature 4: Logging and output options for detailed analysis
- Feature 5: Scriptable for integration into larger testing suites

## Installation

### Requirements

- Linux environment (Kali recommended)
- Basic networking tools (netcat, etc.)
- Perl (for some dependencies)

### Install Commands

```bash
# On Kali Linux (pre-installed in some versions)
sudo apt update && sudo apt install bed

# Manual installation from source
wget https://github.com/infodox/bed/archive/master.zip
unzip master.zip
cd bed-master
make
sudo make install
```

## Basic Usage

```bash
bed --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| -t, --timeout | Set connection timeout in seconds |

## Examples

### Example 1: Basic Usage

```bash
bed -h 192.168.1.100 -p 21
```

### Example 2: Advanced Usage

```bash
bed -h target.example.com -p 80 -b -f -l results.log
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Endpoint Denial of Service]] Endpoint Denial of Service (for crash testing)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual high-volume connections to a single port from a scanning IP
- Detection method 2: Log entries showing malformed or oversized inputs causing service instability
- Detection method 3: Network IDS alerts for fuzzing patterns (e.g., repeated TCP SYN with varying payloads)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[metasploit]]
- [[tools/sqlmap]]

## References

- Official GitHub Repository: https://github.com/infodox/bed
- Kali Tools Documentation: https://www.kali.org/tools/bed
