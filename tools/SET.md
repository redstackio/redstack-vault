---
id: 291780d4-9a90-4d26-ae4f-e34784fceaf9
type: tool
verified: true
created_at: '2019-08-28T21:17:35.669388+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - social-engineering
  - phishing
  - credential-harvesting
url: 'https://github.com/trustedsec/social-engineer-toolkit'
validated: true
---

# SET

**Status**: Unverified

## Overview

The Social-Engineer Toolkit (SET) is an open-source penetration testing framework focused on social engineering attacks. It provides customizable attack vectors for scenarios like spear-phishing, infectious media generation, website cloning, and mass mailer campaigns, enabling testers to simulate realistic social engineering exploits efficiently.

## Description

SET streamlines the creation and execution of social engineering attacks by offering a menu-driven interface with pre-built templates and modules. It's particularly useful for red team operations involving human-targeted vectors, such as credential harvesting via fake login pages or payload delivery through email attachments. The tool integrates with other security tools like Metasploit for payload generation and supports both local and remote attack delivery. Common use cases include training exercises, awareness campaigns, and penetration testing to evaluate employee susceptibility to phishing.

## Features

- Spear-Phishing Attack Vectors: Create and send targeted emails with attachments or links.
- Website Attack Vectors: Clone sites for credential harvesting or drive-by downloads.
- Infectious Media Generator: Embed payloads in USB image files for physical social engineering.
- Mass Mailer: Send bulk emails for large-scale phishing simulations.
- Arduino-based Attack Vectors: HID keyboard attacks using compatible hardware.
- Integration with Metasploit: Leverage payloads and handlers for post-exploitation.
- Customizable Templates: Modify HTML, JavaScript, and email content for realism.

## Installation

### Requirements

- Python 2.7 or 3.x (depending on version)
- Git
- Dependencies like php, apache2 (for web vectors)
- Metasploit Framework (recommended for payloads)

### Install Commands

On Kali Linux (pre-installed in recent versions):

```bash
# If not present, install via apt
sudo apt update && sudo apt install set
```

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install git python3
git clone https://github.com/trustedsec/social-engineer-toolkit.git setoolkit
cd setoolkit
sudo python3 setup.py install
```

On other platforms, clone the repo and follow the setup.py instructions. Ensure web server (e.g., Apache) is installed for hosting cloned sites.

## Basic Usage

```bash
setoolkit
```

This launches the interactive menu. Navigate using numbers to select attack types, then follow prompts for configuration (e.g., IP addresses, payloads).

### Common Options

| Option | Description |
|--------|-------------|
| None (interactive) | Menu-driven; no CLI flags for core launch |
| `--help` | Not directly supported; use menu option 6 for help |

## Examples

### Example 1: Basic Usage (Launch and Select Phishing)

```bash
setoolkit
```

In the menu:
- Select 1) Social-Engineering Attacks
- Select 2) Website Attack Vectors
- Select 3) Credential Harvester Attack Method
- Select 2) Site Cloner
- Enter target URL and local host IP

This sets up a cloned phishing site.

### Example 2: Advanced Usage (Update and Launch)

First update:

```bash
git -C /usr/share/set pull
```

Then launch with [[commands/setoolkit-launch-interactive]] and proceed to spear-phishing setup.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing
- [[T1566.001]] Spearphishing Attachment
- [[T1566.002]] Spearphishing Link
- [[Drive-by Compromise]] Drive-by Compromise
- [[Forge Web Credentials]] Forge Web Credentials

### Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to cloned malicious sites or unusual outbound SMTP connections.
- Suspicious processes like python/setoolkit.py or apache serving phishing content.
- Log entries for mass email sends or USB autorun attempts.
- File artifacts: Temporary HTML clones in /var/www or SET directories.
- Behavioral: High volume of similar emails from internal tools.

## Related Procedures

- [[procedures/Spear-Phishing-Email-Campaign]]
- [[procedures/Website-Cloning-for-Credential-Harvesting]]

## Related Tools

- [[tools/Metasploit]]
- [[tools/Apache]]

## References

- Official GitHub: https://github.com/trustedsec/social-engineer-toolkit
- TrustedSec Documentation: https://www.trustedsec.com/tools/
- SET User Guide: Included in the repo under docs/
