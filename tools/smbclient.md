---
id: tool-uuid-002
url: 'https://www.samba.org/samba/docs/current/man-html/smbclient.1.html'
tags:
  - access
  - smb
type: tool
verified: false
platforms:
  - Linux
  - SMB
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.636Z'
validated: true
submitted: true
---
# smbclient

**Status**: Unverified

## Overview

Smbclient is a command-line tool for interacting with SMB/CIFS servers, allowing file access and enumeration.

## Description

Part of the Samba suite, it emulates a Windows client for connecting to shares, useful for testing access controls in offensive security.

## Features

- Feature 1: Anonymous share access
- Feature 2: File upload/download
- Feature 3: Interactive shell for navigation

## Installation

### Requirements

- Samba package

### Install Commands

```bash
# On Ubuntu/Debian
apt update && apt install smbclient

# On macOS with Homebrew
brew install samba
```

## Basic Usage

```bash
smbclient --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-L` | List shares |
| `-N` | No password |
| `-U` | Specify user |

## Examples

### Example 1: Basic Usage

```bash
smbclient -L //target-ip -N
```

### Example 2: Advanced Usage

```bash
smbclient //target-ip/share -N -c 'get file.txt'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[External Remote Services]] External Remote Services

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- SMB logs showing null session connections
- File access events without credentials

## Related Procedures

- [[procedures/Access-SMB-Shares-Without-Authentication]]

## Related Tools

- [[tools/nmap]]

## References

- Official documentation: https://www.samba.org/samba/docs/
