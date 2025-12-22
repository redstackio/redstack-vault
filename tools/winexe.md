---
type: tool
verified: true
created_at: '2019-08-28T21:17:37.286993+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Unix
tags:
  - lateral-movement
  - remote-execution
  - smb
url: 'https://sourceforge.net/projects/winexe/'
validated: true
---

# winexe

**Status**: Unverified

## Overview

Winexe is a command-line utility for remotely executing commands and launching interactive shells on Windows NT/2000/XP/2003 systems from GNU/Linux or other Unix-like environments. Built on the Samba 4 software package, it leverages SMB (Server Message Block) protocol for authentication and command execution, providing functionality similar to Microsoft's PsExec tool but cross-platform from Linux to Windows.

## Description

Winexe enables offensive security operators to perform lateral movement and post-exploitation tasks by connecting to remote Windows hosts over the network. It supports both single command execution and interactive sessions, making it valuable for red team engagements, penetration testing, and administrative remote management. Note that it targets older Windows versions (NT/2000/XP/2003) and may not work on modern systems without compatibility adjustments due to SMB protocol changes.

## Features

- Feature 1: Remote command execution via SMB without requiring agents on the target.
- Feature 2: Interactive shell support for ongoing sessions.
- Feature 3: Authentication using NTLM credentials (username/password).
- Feature 4: Cross-platform operation from Linux/Unix to Windows.

## Installation

### Requirements

- Samba 4 development libraries (libsmbclient-dev).
- GCC compiler and build tools.
- Supported on Linux distributions like Ubuntu, Kali.

### Install Commands

```bash
# On Kali Linux (pre-built package available)
sudo apt update
sudo apt install winexe

# On Ubuntu (compile from source if not in repos)
sudo apt update
sudo apt install git build-essential libsmbclient-dev

# Clone and build from source
git clone https://sourceforge.net/p/winexe/code/ci/master/tree/
cd winexe
./configure
make
sudo make install
```

For macOS, use Homebrew if available or compile similarly with Samba dependencies.

## Basic Usage

```bash
winexe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage. |
| -U, --user | Specify username (format: user%pass or domain\user%pass). |
| -i | Enable interactive shell mode. |
| --verbose, -v | Increase verbosity for debugging. |

## Examples

### Example 1: Basic Usage

Execute a simple command:

```bash
winexe -U admin%password //192.168.1.100 "dir"
```

### Example 2: Advanced Usage

Launch interactive shell:

```bash
winexe -i -U administrator%pass123 //target-server
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[SMB-Windows Admin Shares]] SMB/Windows Admin Shares
- [[Windows Command Shell]] Windows Command Shell

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor SMB traffic (port 445) for unusual logons from Linux hosts (e.g., via Windows Event ID 4624 with Logon Type 3).
- Detection method 2: Network logs showing winexe user-agent or anomalous command executions (e.g., cmd.exe spawning from SMB sessions).
- Detection method 3: Endpoint detection of unexpected remote command invocations without prior authentication context.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[psexec]]
- [[tools/smbclient]]

## References

- Official SourceForge project: https://sourceforge.net/projects/winexe/
- Samba documentation: https://www.samba.org/
- Kali Tools page: https://www.kali.org/tools/winexe/
