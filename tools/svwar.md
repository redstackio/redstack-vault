---
id: 64394c5f-f137-4083-b578-f2e7cd0a4d5a
type: tool
verified: true
created_at: '2019-08-28T21:17:31.387964+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - voip
  - sip
  - auditing
  - reconnaissance
url: 'https://github.com/EnableSecurity/sipvicious'
commands:
  - '[[commands/svwar-enumerate-extensions]]'
validated: true
---

# svwar

**Status**: Unverified

## Overview

svwar is part of the SIPVicious suite, a set of open-source tools designed to audit SIP-based VoIP systems. Specifically, svwar functions as an extension war dialer, identifying active extensions on a PBX by systematically dialing a range of potential extensions. It is commonly used in penetration testing to map internal VoIP infrastructure and discover valid user accounts for further enumeration or exploitation.

## Description

The SIPVicious suite, including svwar, helps security professionals and researchers test the security of Session Initiation Protocol (SIP) devices and servers. svwar sends SIP INVITE requests to a target PBX across a specified extension range, analyzing responses to determine which extensions are active. This can expose sensitive information like user names or voicemail access points. The suite also includes complementary tools like svmap for device discovery, svcrack for password cracking, svreport for session management and reporting, and svcrash for disrupting unauthorized scans. svwar is particularly useful in red team engagements targeting enterprise VoIP systems to simulate attacker reconnaissance.

## Features

- Feature 1: Extension war dialing with customizable ranges (e.g., 100-9999)
- Feature 2: Support for multiple SIP methods (INVITE, OPTIONS, SUBSCRIBE)
- Feature 3: Rate limiting and multi-threading to avoid detection
- Feature 4: Output formatting for integration with reporting tools
- Feature 5: Proxy support for anonymizing scans

## Installation

### Requirements

- Python 2.7 or 3.x
- pip package manager
- Network access to target SIP servers (UDP/TCP port 5060 typically)

### Install Commands

```bash
# On Kali Linux (pre-installed in many distros)
sudo apt update && sudo apt install sipvicious

# Or install via pip
pip install sipvicious

# For development, clone the repo
git clone https://github.com/EnableSecurity/sipvicious.git
cd sipvicious
python setup.py install
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -e | Specify extension range |
| -m | Select SIP modules |
| -r | Set request rate (requests per second) |
| -t | Number of threads |

## Examples

### Example 1: Basic Usage

```bash
svwar -e 100-500 sip.example.com
```

This scans extensions 100 to 500 on the target SIP server.

### Example 2: Advanced Usage

```bash
svwar -e 1000-2000 -m INVITE,OPTIONS -r 10 -t 5 192.168.1.100
```

This performs a multi-module scan with rate limiting and threading.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Information Discovery]] System Information Discovery (for VoIP-specific discovery)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of SIP INVITE requests from a single source to sequential extensions
- Detection method 2: SIP server logs showing 200 OK responses to invalid extensions
- Detection method 3: Network IDS alerts on UDP/TCP 5060 traffic patterns
- Detection method 4: Use of svcrash to detect and block ongoing scans

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
- [[tools/svcrack]]
- [[tools/svreport]]

## References

- Official GitHub: https://github.com/EnableSecurity/sipvicious
- SIPVicious Documentation: https://sipvicious.org/
- VoIP Security Best Practices: OWASP VoIP Guide
