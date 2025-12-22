---
id: 48c68642-611b-410c-aa8e-96bd2bf67926
name: psexec-py-Impacket
type: tool
verified: true
created_at: '2019-08-28T21:17:26.315589+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/impacket-psexec-spawn-remote-shell]]'
platforms:
  - Linux
  - Windows
tags:
  - administrator
  - network
  - ntlm
  - lateral-movement
  - smb
url: 'https://github.com/SecureAuthCorp/impacket'
validated: true
---

# psexec-py-Impacket

**Status**: Unverified

## Overview

psexec.py is part of the Impacket suite, providing a Python implementation of Microsoft's PSExec tool. It enables remote command execution on Windows systems by leveraging SMB to upload a service executable to the ADMIN$ share, starting it via the Service Control Manager, and connecting through named pipes for an interactive shell. Commonly used in penetration testing for lateral movement with valid administrative credentials.

## Description

This tool mimics the functionality of Sysinternals PSExec, allowing attackers or testers with admin rights to spawn remote shells without needing to install additional software on the target. It targets Windows environments over port 445 (SMB) and requires write access to administrative shares. The process involves temporary file upload, service creation/startup, and pipe-based communication for command execution. It's particularly useful in domain environments for privilege escalation or pivoting.

## Features

- Feature 1: Remote service deployment via SMB without physical access
- Feature 2: Interactive command shell support with named pipes
- Feature 3: Credential passing for authenticated access (NTLM or Kerberos)
- Feature 4: Temporary cleanup of uploaded files and services post-execution
- Feature 5: Support for domain or local accounts

## Installation

### Requirements

- Python 3.6+
- pip package manager
- Network access to target SMB port (445)

### Install Commands

```bash
# Install Impacket suite which includes psexec.py
pip3 install impacket

# Or clone from GitHub for latest version
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket
pip3 install .
```

For Kali Linux, Impacket is often pre-installed or available via `apt install python3-impacket`.

## Basic Usage

```bash
psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -debug | Enable debug output for troubleshooting |
| -hashes | Use LM/NT hashes instead of password (format: lmhash:nthash) |
| -k | Use Kerberos authentication (requires tickets) |
| -no-pass | Prompt for password interactively |

## Examples

### Example 1: Basic Usage

```bash
psexec.py DOMAIN/admin:Password123@192.168.1.100
```

This spawns an interactive shell on the target.

### Example 2: Advanced Usage

```bash
psexec.py -hashes :a1b2c3d4e5f6g7h8i9j0 WORKGROUP/user@10.10.10.10 cmd /c "whoami /all"
```

Executes a single command remotely using NTLM hashes.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[SMB-Windows Admin Shares]] SMB/Windows Admin Shares
- [[Service Execution]] Service Execution

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor SMB traffic for unusual ADMIN$ share writes and service creations (Event ID 7045 for new services)
- Detection method 2: Log named pipe connections (e.g., \pipe\cmd) and temporary .exe uploads to %TEMP%
- Detection method 3: Enable SMB signing and restrict admin share access; watch for Impacket user-agent strings in logs
- Detection method 4: Behavioral analytics for anomalous service starts from remote initiators

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/smbclient]]
- [[tools/wmiexec-py-Impacket]]
- [[tools/Evil-WinRM]]

## References

- Official GitHub: https://github.com/SecureAuthCorp/impacket
- Impacket Documentation: https://www.secureauth.com/labs/impacket
- Sysinternals PSExec: https://docs.microsoft.com/en-us/sysinternals/downloads/psexec
