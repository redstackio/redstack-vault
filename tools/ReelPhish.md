---
id: 9b886a91-eeaf-4449-976f-4d014afec941
name: ReelPhish
type: tool
verified: true
created_at: '2019-08-28T21:17:22.188902+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - phishing
  - 2fa
  - social-engineering
url: 'https://github.com/chr1x0x/ReelPhish'
validated: true
---

# ReelPhish

**Status**: Unverified

## Overview

ReelPhish is a real-time two-factor authentication (2FA) phishing tool designed for capturing OTP codes and credentials during phishing attacks. It is commonly used in red team operations to simulate advanced phishing scenarios involving multi-factor authentication bypass.

## Description

ReelPhish operates by hosting a phishing page that mimics legitimate login portals, capturing user inputs including usernames, passwords, and real-time OTPs from 2FA prompts. The tool forwards captured data to the attacker's dashboard or specified endpoint in real-time, allowing immediate exploitation. It supports customizable templates and can integrate with reverse proxies for domain fronting. Primarily used in social engineering assessments to test 2FA resilience.

## Features

- Feature 1: Real-time OTP capture and forwarding via WebSockets
- Feature 2: Customizable HTML templates for various target services (e.g., Office 365, Gmail)
- Feature 3: Built-in dashboard for monitoring phishing sessions
- Feature 4: Support for SSL/TLS to mimic secure sites
- Feature 5: Report generation for captured data analysis

## Installation

### Requirements

- Python 3.6+
- pip-installed dependencies: flask, requests, websocket-client
- Git for cloning the repository

### Install Commands

```bash
# Clone the repository
git clone https://github.com/chr1x0x/ReelPhish.git
cd ReelPhish

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (pre-requisites often met)
sudo apt update && sudo apt install python3-pip git
```

## Basic Usage

```bash
python3 reelphish.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t, --template | Specify phishing template file |
| -p, --port | Set listening port |
| --ssl | Enable HTTPS support |
| --report | Generate session report |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```bash
python3 reelphish.py -t templates/office365.html -p 8080
```

Starts a phishing server on port 8080 using an Office 365 template.

### Example 2: Advanced Usage

```bash
python3 reelphish.py -t templates/custom.html -p 443 --ssl --dashboard
```

Launches an SSL-enabled server with a dashboard for real-time monitoring.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing
- [[Multi-Factor Authentication Request Generation]] Multi-Factor Authentication Request Generation

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP traffic to phishing domains with 2FA patterns
- Detection method 2: Anomalous WebSocket connections for real-time data exfiltration
- Detection method 3: Presence of Flask server signatures in network logs
- Detection method 4: Custom templates matching known phishing kits in endpoint security scans

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Gophish]]
- [[tools/Evilginx2]]

## References

- Official GitHub: https://github.com/chr1x0x/ReelPhish
- Related resources: Phishing framework comparisons on Pentest blogs
