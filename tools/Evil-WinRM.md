---
type: tool
verified: true
platforms:
  - Linux
  - Windows
tags:
  - '[[Defense Bypass]]'
  - '[[shell]]'
commands:
  - '[[commands/dump-process-memory-out-minidump]]'
url: 'https://github.com/Hackplayers/evil-winrm'
validated: true
---

# Evil-WinRM

**Status**: ✓ Verified

## Overview

Evil-WinRM is a Ruby-based tool for spawning interactive PowerShell sessions on remote Windows systems via the WinRM protocol (typically over port 5985). It is commonly used in penetration testing and red team operations to gain shell access to Windows hosts after obtaining valid credentials or hashes.

## Description

Evil-WinRM enables remote PowerShell execution on Windows targets using WinRM, supporting features like in-memory loading of scripts, DLLs, and C# assemblies to evade antivirus detection. It supports authentication methods including pass-the-hash, Kerberos, and SSL with certificates, as well as file upload/download capabilities.

## Features

- Load in-memory PowerShell scripts for stealthy execution
- Load in-memory DLL files to bypass some AV solutions
- Load in-memory C# code to bypass AV
- Bypass AMSI (Antimalware Scan Interface)
- Pass-the-hash support for credential reuse
- Kerberos authentication
- SSL support with certificates
- Upload and download files to/from the target

## Installation

### Requirements

- Ruby 2.3 or later
- Build tools (for gem compilation on Linux)

### Install on Debian/Ubuntu

1. Update system and install Ruby with build essentials:

```bash
sudo apt update
sudo apt install ruby ruby-dev build-essential
```

Note: When prompted by the installer to choose a toolchain, select either 1 or 3.

2. Install Evil-WinRM via RubyGems:

```bash
gem install evil-winrm
```

### Install on Windows

1. Download and install the latest Ruby + Devkit from [rubyinstaller.org](https://rubyinstaller.org/downloads/).

2. Open a command prompt and install Evil-WinRM:

```cmd
gem install evil-winrm
```

## Basic Usage

```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --ip IP` | Target IP address |
| `-u, --user USER` | Username for authentication |
| `-p, --password PASS` | Password (or use `-H` for hash) |
| `-H, --hash HASH` | NTLM hash for pass-the-hash |
| `-r, --realm REALM` | Kerberos realm |
| `-S, --ssl` | Enable SSL |
| `-c, --cert CERT` | Path to SSL certificate |
| `-P, --port PORT` | WinRM port (default 5985) |

## Examples

### Example 1: Basic Connection with Password

```bash
evil-winrm -i 192.168.1.100 -u administrator -p Password123
```

Once connected, you get an interactive PowerShell prompt where you can run commands like `whoami` or load modules.

### Example 2: Pass-the-Hash Authentication

```bash
evil-winrm -i 192.168.1.100 -u administrator -H aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```

### Example 3: SSL Connection

```bash
evil-winrm -i target.contoso.com -u user -p pass -S -c /path/to/cert.pem
```

## Related Commands

- [[commands/dump-process-memory-out-minidump]]

## References

- Official GitHub: https://github.com/Hackplayers/evil-winrm
- WinRM Protocol: https://docs.microsoft.com/en-us/windows/win32/winrm/portal
