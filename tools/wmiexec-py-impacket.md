---
type: tool
verified: true
platforms:
  - Linux
  - Windows
tags:
  - administrator
  - network
  - lateral-movement
  - post-exploitation
url: 'https://github.com/SecureAuthCorp/impacket'
validated: true
---

# wmiexec.py (Impacket)

**Status**: ✓ Verified

## Overview

wmiexec.py is a tool from the Impacket suite that uses Windows Management Instrumentation (WMI) to execute commands on remote Windows systems. It provides semi-interactive shell access, running commands as the Administrator user rather than SYSTEM (unlike smbexec.py), which results in fewer traces in event logs. However, it requires network access to the target's DCOM ports (typically TCP 135) in addition to SMB.

Common use cases include lateral movement in Active Directory environments, remote command execution during penetration tests, and post-exploitation activities where authenticated access to Windows hosts is available.

## Description

The tool authenticates to the target using provided credentials (username:password or NTLM hash) over SMB and leverages WMI to initiate command execution via the Windows Command Prompt (cmd.exe). It supports semi-interactive sessions where multiple commands can be entered, with output streamed back to the attacker. Key advantages include stealthier operation compared to tools that spawn full processes, but it may be detected by advanced endpoint monitoring due to WMI event generation.

## Features

- Semi-interactive command shell over WMI
- Support for NTLM authentication (password or hash)
- Output collection and display from remote cmd.exe
- Minimal local process creation on the target
- Integration with other Impacket tools for credential reuse

## Installation

### Requirements

- Python 3.6+
- pip package manager

### Install Commands

```bash
# Install Impacket suite (includes wmiexec.py)
pip3 install impacket
```

On Kali Linux, Impacket is often pre-installed or available via apt:

```bash
sudo apt update && sudo apt install impacket-scripts
```

## Basic Usage

```bash
wmiexec.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-d, --domain` | Domain for authentication (if not local) |
| `-hashes` | NTLM hash instead of password (format: LMHASH:NTHASH) |
| `-no-pass` | Use current user's credentials (Kerberos) |
| `-k` | Use Kerberos authentication |
| `--local-auth` | Use local authentication (no domain) |

## Examples

### Example 1: Basic Usage

Connect to a target using username and password to spawn a semi-interactive shell:

```bash
wmiexec.py username:password@target_ip
```

### Example 2: Advanced Usage

Connect using NTLM hashes and specify a domain:

```bash
wmiexec.py -d domain.com -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 username@target_ip
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Management Instrumentation]] Windows Management Instrumentation
- [[SMB-Windows Admin Shares]] SMB/Windows Admin Shares
- [[Windows Command Shell]] Windows Command Shell

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- WMI event logs (Event ID 5857 for WMI activity)
- Network traffic to TCP 135 (DCOM/RPC) followed by SMB (445)
- Command-line auditing showing cmd.exe spawned via WMI
- Anomalous Administrator logons from unexpected sources
- Use of Sysmon or EDR tools to monitor WMI queries and remote execution

## Related Procedures

- [[procedures/Execute-Remote-Commands-via-WMI]]
- [[procedures/Lateral-Movement-with-Impacket]]

## Related Tools

- [[smbexec-py-impacket]]
- [[tools/psexec-py-Impacket]]
- [[tools/CrackMapExec]]

## References

- Official Impacket GitHub: https://github.com/SecureAuthCorp/impacket
- WMI Execution Technique: https://attack.mitre.org/techniques/T1047/

## Commands (1)

- [[commands/wmiexec-py-spawn-semi-interactive-shell]]
