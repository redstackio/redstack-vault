---
url: 'https://github.com/googleprojectzero/symboliclink-testing-tools/releases'
tags:
  - toctou
  - ntfs
  - file-swap
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.555Z'
id: 8d94f6d9-3a57-4a28-a9a0-a31473a87155
validated: true
submitted: true
---
# BaitAndSwitch

**Status**: Unverified

## Overview

BaitAndSwitch is a Windows tool for exploiting TOCTOU vulnerabilities by using NTFS opportunistic locks to detect file access and perform targeted file swaps during brief race windows.

## Description

Developed by Project Zero, this tool sets opportunistic locks (OpLocks) on a bait file, monitors for access breaks (indicating a read/check), and then swaps it with a malicious version before the use phase. It's ideal for scenarios like the NordVPN config swap, where timing is critical. The tool runs as a executable, requiring no installation, and supports custom swap paths and callbacks.

## Features

- Feature 1: NTFS OpLock monitoring for precise access detection
- Feature 2: Atomic file replacement during lock breaks
- Feature 3: Logging of race events for debugging

## Installation

### Requirements

- Windows with NTFS
- Admin privileges for lock setup (escalatable)

### Install Commands

```bash
# Download from releases
# No install; run baitandswitch.exe directly
```

## Basic Usage

```bash
baitandswitch.exe -bait C:\temp\bait.ovpn -swap C:\temp\malicious.ovpn
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Verbose logging of lock events |
| -t, --timeout | Timeout for monitoring (seconds) |

## Examples

### Example 1: Basic Usage

```bash
baitandswitch.exe -bait bait.ovpn -swap evil.ovpn
```

### Example 2: Advanced Usage

```bash
baitandswitch.exe -bait C:\path\to\bait.ovpn -swap C:\path\to\malicious.ovpn -v -t 300
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Hijack Execution Flow]] Hijack Execution Flow

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual OpLock breaks in file system logs (ETW or ProcMon)
- Rapid file modifications in application config directories
- Presence of baitandswitch.exe in process lists

## Related Procedures


## Related Tools

- [[tools/Invoke-ExploitNordVPNConfigLPE]]

## References

- https://github.com/googleprojectzero/symboliclink-testing-tools
- Project Zero blog on TOCTOU exploits
