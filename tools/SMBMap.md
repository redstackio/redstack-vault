---
type: tool
description: >-
  SMBMap is a command-line tool for enumerating SMB/CIFS shares on remote
  systems, including listing shares, checking permissions, browsing contents,
  file operations, and remote command execution.
url: 'https://github.com/ShawnDEvans/smbmap'
verified: true
platforms:
  - Linux
  - Windows
tags:
  - enumeration
  - ntlm
  - smb
commands:
  - '[[commands/smbmap-list-share-contents-recursively]]'
validated: true
---

# SMBMap

**Status**: Unverified

## Overview

SMBMap is a Python-based tool designed for SMB/CIFS enumeration in security testing and penetration engagements. It allows users to discover available shares on remote Windows or Samba systems, assess access permissions, recursively list directory contents, perform file uploads/downloads, search for files by name or content, and even execute commands remotely. It supports anonymous (NULL) sessions and authentication using plaintext passwords or NTLM hashes, making it versatile for both initial reconnaissance and post-exploitation scenarios.

Common use cases include mapping network shares during lateral movement discovery, identifying writable shares for payload deployment, and gathering file-based intelligence without full domain access.

## Description

SMBMap leverages the Impacket library to interact with SMB protocols (versions 1-3). It can enumerate shares without credentials in some cases (e.g., guest access) and provides detailed output on read/write/execute permissions. Beyond basic listing, it enables practical operations like downloading sensitive files (e.g., SAM hives) or uploading tools to writable locations. The tool is lightweight, cross-platform (via Python), and integrates well with other enumeration suites like enum4linux or CrackMapExec.

## Features

- **Share Enumeration**: List all accessible SMB shares and their permissions (READ, WRITE, EXECUTE).
- **Directory Browsing**: Recursively explore share contents with file sizes, timestamps, and paths.
- **File Operations**: Upload/download files or search by name/content using regex patterns.
- **Remote Execution**: Run commands on the target via SMBExec-like functionality.
- **Authentication Flexibility**: Supports NULL sessions, username/password, or NTLM hash auth.
- **Output Formatting**: Human-readable tree views or JSON for scripting.

## Installation

### Requirements

- Python 3.6+ (with pip)
- Impacket library (automatically installed via pip)
- For Windows: Python and dependencies like pywin32 (optional for native SMB).

### Install Commands

```bash
# On Kali Linux (pre-installed in many distros)
sudo apt update && sudo apt install smbmap

# On Ubuntu/Debian
sudo apt update && sudo apt install smbmap

# From PyPI (universal)
pip3 install smbmap

# From GitHub source (for latest features)
git clone https://github.com/ShawnDEvans/smbmap.git
cd smbmap
pip3 install .
```

For Windows, use Python installer from python.org, then run the pip or git method in Command Prompt or PowerShell.

## Basic Usage

```bash
smbmap -H <target_ip>
```

This performs anonymous enumeration of shares on the target.

### Common Options

| Option | Description |
|--------|-------------|
| `-H, --host` | Target IP or hostname (required) |
| `-u, --user` | Username for authentication |
| `-p, --pass` | Password or NTLM hash |
| `-r, --share` | Specific share to target |
| `-R` | Recursively list directory contents |
| `-x, --exec-method` | Execute command on target (e.g., `cmd.exe`) |
| `-F` | List shares only |
| `--dc-ip` | Domain controller IP for auth |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage (Anonymous Share Enumeration)

```bash
smbmap -H 192.168.1.100
```

This lists all shares accessible without credentials.

### Example 2: Advanced Usage (Authenticated Recursive Listing)

See the related command for details:

[[commands/smbmap-list-share-contents-recursively]]

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[External Remote Services]] Network Share Discovery
- [[T1087.001]] Account Discovery: Local Account (via share enumeration)
- [[SMB-Windows Admin Shares]] Remote Services: SMB/Windows Admin Shares

### Tactics

- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement

## Detection

- Monitor SMB traffic (port 445/TCP) for unusual enumeration patterns or failed logons.
- Enable SMB signing and auditing on domain controllers/shares.
- Look for Impacket/SMBMap signatures in network logs (e.g., multiple TREE_CONNECT requests).
- File integrity monitoring on shares for unexpected uploads/downloads.
- EDR alerts on command execution via SMB (e.g., psexec-like behavior).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/CrackMapExec]] (for broader SMB ops)
- [[Impacket-Suite]] (underlying library)
- [[tools/enum4linux]] (SMB enumeration alternative)

## References

- Official GitHub: https://github.com/ShawnDEvans/smbmap
- Impacket Documentation: https://github.com/SecureAuthCorp/impacket
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1133/
