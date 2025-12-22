---
type: tool
description: >-
  A tool from the SIPVicious suite designed to disrupt and stop unauthorized SIP
  scanning attempts by sending malformed packets to crash scanners like svwar
  and svcrack.
url: 'https://github.com/EnableSecurity/sipvicious'
verified: true
created_at: '2019-08-28T21:17:29Z'
updated_at: '2023-05-29T16:48:53Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - voip
  - sip
  - disruption
  - auditing
validated: true
---

# svcrash

**Status**: Unverified

## Overview

svcrash is part of the SIPVicious suite, a set of open-source tools for auditing SIP-based VoIP systems. Specifically, svcrash is used to detect and disrupt unauthorized scanning activities targeting SIP devices, such as those performed by svwar (extension war dialing) or svcrack (password cracking). It sends specially crafted, malformed SIP packets to crash or halt these scans, making it useful for testing scan evasion, defensive simulations, or VoIP security assessments.

## Description

The SIPVicious suite audits VoIP systems by identifying vulnerabilities in SIP configurations, extensions, and authentication. svcrash focuses on the defensive aspect within offensive testing: it attempts to stop scans by exploiting weaknesses in the scanning tools themselves or by overwhelming the scanner with invalid requests. This can help red teams understand how scans can be detected and disrupted in real environments, or blue teams to simulate attacks and improve monitoring.

## Features

- Feature 1: Sends disruptive SIP packets to target scanners or devices.
- Feature 2: Targets specific IP ranges to halt ongoing svwar/svcrack operations.
- Feature 3: Integrates with other SIPVicious tools for comprehensive VoIP audits.

## Installation

### Requirements

- Python 3.x
- pip package manager

### Install Commands

```bash
# Install via pip (recommended)
pip install sipvicious

# Or install from source
git clone https://github.com/EnableSecurity/sipvicious.git
cd sipvicious
pip install .
```

On Kali Linux, it may be available via apt: `sudo apt install sipvicious`.

## Basic Usage

```bash
svcrash --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v, --verbose` | Enable verbose output for debugging |
| `--target` | Specify target IP or range |

## Examples

### Example 1: Basic Usage

```bash
svcrash 192.168.1.100
```

This disrupts scans on the specified IP.

### Example 2: Advanced Usage

```bash
svcrash --verbose 192.168.1.0/24
```

Targets a subnet with detailed logging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service (for disrupting scanners)
- [[Archive Collected Data]] Archive Collected Data (in context of VoIP data handling)

### Tactics

- [[Impact]] Impact (denial of scanning operations)
- [[Initial Access]] Initial Access (VoIP-specific reconnaissance disruption)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual SIP traffic spikes with malformed packets on network monitors like Wireshark.
- Detection method 2: Logs of failed SIP requests or scanner crashes in VoIP PBX systems.
- Detection method 3: Process monitoring for 'svcrash' or Python scripts sending SIP INVITEs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/svmap]]
- [[tools/svwar]]
- [[tools/svcrack]]
- [[tools/svreport]]

## References

- Official GitHub: https://github.com/EnableSecurity/sipvicious
- SIPVicious Documentation: https://sipvicious.readthedocs.io/
- VoIP Security Best Practices: OWASP VoIP Guide
