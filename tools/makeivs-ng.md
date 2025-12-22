---
id: fc4c7856-8022-4aa7-8082-0cd0f07386e5
name: makeivs-ng
type: tool
verified: true
created_at: '2019-08-28T21:17:32.655508+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wep
  - testing
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=makeivs-ng'
commands:
  - '[[commands/makeivs-ng-generate-ivs-dump]]'
validated: true
---

# makeivs-ng

**Status**: Unverified

## Overview

makeivs-ng is a utility from the aircrack-ng suite designed to generate synthetic IVS (Initialization Vector Statistics) dump files for WEP-encrypted WiFi networks. It allows security testers to create test data with a known encryption key, enabling offline testing of WEP cracking tools without capturing live traffic. Commonly used in wireless penetration testing for validating cracking algorithms and tool performance.

## Description

makeivs-ng simulates the generation of WEP-encrypted packets by producing an IVS file that mimics the output from real packet captures (e.g., from airodump-ng). This is particularly useful for controlled environments, educational purposes, or when real WEP traffic is unavailable or unethical to capture. The tool requires specifying the network ESSID and WEP key to encrypt the generated vectors accurately. It supports various WEP key lengths (64-bit, 128-bit) and can produce dumps of customizable sizes for thorough testing.

## Features

- Feature 1: Generates realistic IVS dumps with specified WEP keys for testing purposes.
- Feature 2: Supports multiple WEP key formats (hexadecimal, ASCII).
- Feature 3: Integrates seamlessly with other aircrack-ng tools for direct cracking tests.
- Feature 4: Lightweight and fast, producing large dumps quickly without network dependency.

## Installation

### Requirements

- Linux environment (Kali Linux recommended).
- aircrack-ng package (makeivs-ng is included).

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install aircrack-ng

# On macOS (via Homebrew)
brew install aircrack-ng

# Verify installation
makeivs-ng --help
```

## Basic Usage

```bash
makeivs-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage. |
| -e ESSID | Specify the network ESSID. |
| -p key | Provide the WEP key in hex or ASCII. |
| -f file | Output file for the IVS dump. |

## Examples

### Example 1: Basic Usage

Generate a simple IVS dump for a 64-bit WEP key:

```bash
makeivs-ng -e "TestWiFi" -p 616263646566 -f test.ivs
```

### Example 2: Advanced Usage

Create a dump for a 128-bit key and larger dataset:

```bash
makeivs-ng -e "SecureNet" -p 01:02:03:04:05:06:07:08:09:0A:0B:0C:0D:0E:0F:10 -f advanced_test.ivs
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless network testing).
- [[File and Directory Discovery]] File and Directory Discovery (in context of dump file generation for analysis).

### Tactics

- [[Reconnaissance]] Reconnaissance (wireless environment testing).

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of .ivs files in temporary directories or test environments.
- Detection method 2: Process monitoring for makeivs-ng execution in security logs.
- Detection method 3: Network-independent file generation patterns in forensic analysis.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]]
- [[tools/airodump-ng]]

## References

- Official documentation: https://www.aircrack-ng.org/doku.php?id=makeivs-ng
- Aircrack-ng project: https://www.aircrack-ng.org
