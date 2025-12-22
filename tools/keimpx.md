---
id: 6db19644-6e79-4844-bee4-7a244ceab6b9
name: keimpx
type: tool
verified: true
created_at: '2019-08-28T21:17:34.886856Z'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - smb
  - credentials
  - validation
  - lateral-movement
url: 'https://github.com/marcsello/keimpx'
validated: true
---

# keimpx

**Status**: Unverified

## Overview

keimpx is an open-source Python tool for rapidly validating credentials across a network via SMB. It supports plaintext passwords, NTLM hashes, and NTLM logon session tokens. Ideal for offensive security operations like credential testing during lateral movement or post-exploitation. Released under a modified Apache License 1.1.

## Description

keimpx leverages Impacket libraries to perform SMB authentication checks on multiple hosts. Upon finding valid credentials, it provides an interactive SMB shell for further actions such as file manipulation, service deployment (e.g., backdoors), user enumeration, and domain policy inspection. Commonly used in red team engagements to confirm dumped credentials and pivot to new systems.

## Features

- Feature 1: Multi-credential validation (password, NTLM hash, session token) against IP ranges or host lists.
- Feature 2: Interactive SMB shell for file upload/download, directory navigation, and command execution.
- Feature 3: Service deployment/undeployment capabilities for persistence.
- Feature 4: Enumeration of users, domains, and password policies.
- Feature 5: Verbose logging and output for failed/successful authentications.

## Installation

### Requirements

- Python 3.6+
- Impacket library (pip install impacket)
- Git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/marcsello/keimpx.git
cd keimpx

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (often pre-configured with Impacket)
apt update && apt install python3-impacket
```

## Basic Usage

```bash
python3 keimpx.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for detailed logging |
| -u | Specify username |
| -p | Specify password |
| -H | Specify NTLM hash |
| -d | Specify domain |
| -t | Specify target (IP, range, or file) |
| --shell | Launch interactive SMB shell after validation |

## Examples

### Example 1: Basic Usage

```bash
python3 keimpx.py -u administrator -p Summer18! -d . 192.168.1.0/24
```

### Example 2: Advanced Usage

```bash
python3 keimpx.py -u user -H aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 -d DOMAIN 192.168.1.100 --shell -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Unsecured Credentials]] Unsecured Credentials
- [[SMB-Windows Admin Shares]] SMB/Windows Admin Shares

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual SMB authentication attempts from a single source (monitor Event ID 4625 in Windows logs).
- Detection method 2: Network traffic spikes on port 445 (SMB) with failed logons.
- Detection method 3: Presence of Python processes invoking Impacket libraries (e.g., via Sysmon or EDR).
- Detection method 4: Anomalous file uploads/downloads over SMB shares.

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
- [[tools/CrackMapExec]]

## References

- Official GitHub: https://github.com/marcsello/keimpx
- Impacket Documentation: https://github.com/fortra/impacket

## Related Commands

- [[commands/keimpx-validate-password-credentials]]
- [[commands/keimpx-validate-ntlm-hash]]
- [[commands/keimpx-interactive-smb-shell]]
