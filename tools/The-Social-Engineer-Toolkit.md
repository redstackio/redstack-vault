---
id: e3e522de-e9f1-430b-85e5-522952097714
type: tool
verified: true
created_at: '2019-08-28T21:17:31.295787+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - social-engineering
  - phishing
  - credential-harvesting
  - penetration-testing
url: 'https://github.com/trustedsec/social-engineer-toolkit'
validated: true
---

# The Social-Engineer Toolkit

**Status**: Unverified

## Overview

The Social-Engineer Toolkit (SET) is an open-source penetration testing framework specifically designed for social engineering engagements. It automates common attack vectors like phishing, credential harvesting, and infectious media creation, making it a go-to tool for red teamers simulating human-targeted attacks in controlled environments.

## Description

SET provides a user-friendly interface to launch sophisticated social engineering campaigns without requiring deep coding knowledge. It supports modules for email phishing, website cloning for credential capture, SMS spoofing, and integration with tools like Metasploit for payload delivery. Commonly used in ethical hacking to test employee awareness and organizational defenses against social engineering tactics.

## Features

- **Spear-Phishing Attack Vectors**: Create targeted email campaigns with attachments or links leading to malicious payloads.
- **Website Attack Vectors**: Clone legitimate sites to harvest credentials via JavaScript or form submissions.
- **Infectious Media Generator**: Generate autorun USB payloads for physical social engineering.
- **Mass Mailer**: Send bulk emails for large-scale phishing simulations.
- **Integration with Other Tools**: Works with Metasploit, BeEF, and custom payloads for advanced attacks.

## Installation

### Requirements

- Python 3.x
- Git
- pip and required libraries (e.g., pycrypto, requests)

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/trustedsec/social-engineer-toolkit.git setoolkit

# Navigate to the directory
cd setoolkit

# Install dependencies
sudo pip3 install -r requirements.txt

# Run setup
sudo python3 setup.py install
```

On Kali Linux, SET is pre-installed and can be updated via `apt update && apt upgrade setoolkit`.

For Windows/macOS, use a virtual environment or WSL for best compatibility.

## Basic Usage

```bash
setoolkit
```

This launches the interactive menu. Navigate using numbers to select modules (e.g., 1 for Social-Engineering Attacks, then 2 for Website Attack Vectors).

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message with basic options |
| No verbose flag | Output is menu-driven; use screen or tmux for long sessions |

## Examples

### Example 1: Basic Usage

```bash
setoolkit
```

Select option 1 (Social-Engineering Attacks), then 2 (Spear-Phishing Attack Vectors) to configure an email campaign.

### Example 2: Advanced Usage

Launch SET and integrate with Metasploit:

```bash
setoolkit
```

Within the phishing module, choose to use MSF payloads for reverse shells on successful credential capture.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing
- [[T1566.001]] Spearphishing Attachment
- [[T1566.002]] Spearphishing Link
- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to cloned phishing sites or unusual SMTP connections.
- Presence of SET directories or Python processes running setoolkit.py.
- Log entries for mass email sends or credential harvesting endpoints.
- Behavioral: Unusual USB autorun files or email attachments from testing domains.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit-Framework]]
- [[tools/beef]]

## References

- Official GitHub: https://github.com/trustedsec/social-engineer-toolkit
- Documentation: https://www.trustedsec.com/tools/

*Last updated: 2023-10-01*
