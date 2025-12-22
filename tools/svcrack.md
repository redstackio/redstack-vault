---
type: tool
verified: true
created_at: '2019-08-28T21:17:28.475471+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - voip
  - sip
  - brute-force
  - credential-access
url: 'https://github.com/EnableSecurity/sipvicious'
validated: true
---

# svcrack

**Status**: Unverified

## Overview

svcrack is a component of the SIPVicious suite, a set of open-source tools designed for auditing SIP-based VoIP systems. Specifically, svcrack performs online password cracking against SIP PBX servers by attempting authentication with single credentials or dictionary-based brute-force attacks. It is commonly used in penetration testing to identify weak or default credentials on VoIP infrastructure.

## Description

The SIPVicious suite, including svcrack, helps security professionals and researchers audit the security of Session Initiation Protocol (SIP) devices and PBX systems. svcrack focuses on credential brute-forcing by sending SIP REGISTER or INVITE requests with varying username/password combinations to a target server. It supports rate limiting to avoid detection and can output results in various formats for further analysis. Use it ethically in controlled environments to assess VoIP security postures, such as detecting exposed extensions with default passwords.

## Features

- Online brute-force attacks using single credentials or wordlists
- Support for SIP REGISTER and INVITE methods
- Rate limiting and delay options to mimic legitimate traffic
- Session management and result export via svreport (suite companion)
- Cross-platform compatibility via Python

## Installation

### Requirements

- Python 3.6 or higher
- pip package manager

### Install Commands

```bash
# Install via pip (recommended)
pip install sipvicious

# Or clone from GitHub
apt update && apt install git python3-pip  # On Debian/Ubuntu
mkdir -p ~/tools && cd ~/tools
git clone https://github.com/EnableSecurity/sipvicious.git
cd sipvicious
pip3 install -r requirements.txt
python3 setup.py install
```

For Kali Linux: The suite is available in the repositories.

```bash
apt update && apt install sipvicious
```

## Basic Usage

```bash
tool-name --help
svcrack -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| --rate | Set request rate (requests per second) |
| --sl | Set delay between requests in seconds |
| -m | Specify method (REGISTER or INVITE) |

## Examples

### Example 1: Basic Usage

```bash
svcrack -u admin -p password -e 100 -s 192.168.1.100
```

### Example 2: Advanced Usage

```bash
svcrack -U users.txt -P passes.txt -e 100 -s sip.example.com --rate 5 --sl 1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual SIP REGISTER/INVITE traffic spikes from a single source
- Failed authentication logs on SIP servers (e.g., Asterisk logs showing 401 Unauthorized)
- Network monitoring for SIP port 5060/5061 traffic patterns matching brute-force attempts
- IDS/IPS rules for high-volume SIP requests with varying credentials

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
- [[tools/svreport]]

## References

- Official GitHub: https://github.com/EnableSecurity/sipvicious
- SIPVicious Documentation: https://sipvicious.readthedocs.io/
- VoIP Security Auditing Guide: https://www.owasp.org/index.php/OWASP_VoIP_Project
