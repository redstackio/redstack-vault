---
id: a7574334-36e9-49db-a6ef-a99b1209a1ac
type: tool
description: >-
  A phishing framework using Flask and Jinja2 for capturing credentials and 2FA
  tokens.
verified: true
url: 'https://github.com/ltoddis/credSniper'
created_at: '2019-08-28T21:17:32.971985+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - phishing
  - credentials
  - 2fa
  - mfa
validated: true
---

# CredSniper

**Status**: Unverified

## Overview

CredSniper is a phishing framework developed in Python using the Flask micro-framework and Jinja2 templating. It specializes in creating realistic phishing pages that can capture user credentials, including two-factor authentication (2FA) tokens, making it useful for social engineering simulations in red team operations.

## Description

The tool allows for quick setup of phishing servers that mimic popular login portals. It handles form submissions, logs captured data to files, and supports dynamic content generation. Commonly used in penetration testing to demonstrate phishing risks, especially in environments with MFA enabled.

## Features

- Flask-based web server for hosting phishing pages
- Jinja2 templating for customizable and dynamic content
- Built-in support for capturing 2FA/MFA tokens
- Automatic logging of credentials to ./loots/ directory
- Easy integration with tunneling tools like ngrok for external access
- Pre-built templates for common targets (e.g., Office 365, Gmail)

## Installation

### Requirements

- Python 3.6+
- pip-installed dependencies: Flask, Jinja2

### Install Commands

```bash
# Clone the repository
git clone https://github.com/ltoddis/credSniper.git
cd credSniper

# Install Python dependencies
pip3 install -r requirements.txt
```

On Kali Linux, it may require additional setup for HTTPS support if using SSL.

## Basic Usage

```bash
python3 credSniper.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --lhost | Bind address for the server (default: 127.0.0.1) |
| --lport | Port to listen on (default: 80) |
| --2fa | Enable 2FA token capture |
| --template | Specify a custom Jinja2 template directory |
| --generate-template | Create a new template for a target service |

## Examples

### Example 1: Basic Usage

```bash
python3 credSniper.py --lhost 0.0.0.0 --lport 8080
```

This starts a phishing server accessible on all interfaces at port 8080.

### Example 2: Advanced Usage

```bash
python3 credSniper.py --lhost 0.0.0.0 --lport 443 --2fa --template office365
```

Launches with 2FA support using an Office 365 template.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment
- [[Multi-Factor Authentication Request Generation]] Multi-Factor Authentication Request Generation
- [[Reversible Encryption]] Password Guessing (in context of credential capture)

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of Flask processes with unusual web paths
- Outbound traffic to tunneling services (e.g., ngrok)
- Log files in ./loots/ containing captured data
- Network traffic patterns mimicking legitimate login portals but logging to local files
- Python processes executing credSniper.py

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/SEToolkit]]
- [[tools/Gophish]]
- [[tools/Evilginx2]]

## References

- Official GitHub: https://github.com/ltoddis/credSniper
- Flask Documentation: https://flask.palletsprojects.com/
- Jinja2 Templating: https://jinja.palletsprojects.com/
