---
id: 027ca479-5f3c-4c11-b8d4-e904e08d9750
type: tool
verified: true
created_at: '2020-06-25T00:11:34.131643+00:00'
updated_at: '2023-05-30T20:00:28.175277+00:00'
platforms:
  - Linux
tags:
  - network
  - smb
url: 'https://www.samba.org/samba/docs/current/man-html/net.8.html'
commands:
  - '[[commands/net-sync-local-time-with-remote-server]]'
validated: true
---

# net-samba-linux

**Status**: ✓ Verified

## Overview

Net is a command-line tool from the Samba suite on Linux systems that emulates the functionality of the Windows `net` utility. It is commonly used in security testing for interacting with Windows domains and SMB shares, including tasks like time synchronization, user/group management, share enumeration, and Kerberos authentication operations.

## Description

The `net` tool provides a Unix/Linux equivalent for Windows network administration commands, enabling red teamers and penetration testers to perform domain joins, time syncs, and user manipulations in Active Directory environments without needing Windows tools. It supports RPC and SMB protocols, making it essential for post-exploitation in hybrid networks.

## Features

- Feature 1: Time synchronization with remote servers for Kerberos compatibility
- Feature 2: User and group management (add/remove/query) via RPC
- Feature 3: Share enumeration and access control list (ACL) manipulation
- Feature 4: Kerberos ticket handling and domain authentication

## Installation

### Requirements

- Samba libraries and common binaries
- Network access to target domain/SMB servers

### Install Commands

```bash
# On Debian/Ubuntu
sudo apt update
sudo apt install samba-common-bin

# On CentOS/RHEL
sudo yum install samba-client

# Verify installation
net --help
```

## Basic Usage

```bash
net help
```

### Common Options

| Option | Description |
|--------|-------------|
| -U username[%password] | Specify user credentials for authentication |
| -k | Use Kerberos authentication |
| -S server | Target a specific server |
| -I ip | Specify interface IP |

## Examples

### Example 1: Basic Usage

```bash
net time -S dc01.example.com
```

### Example 2: Advanced Usage

```bash
net user /add testuser -U admin%password -S dc01.example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for SMB/RPC traffic from Linux hosts to domain controllers
- Detection method 2: Log analysis for `net` command executions in process monitoring (e.g., auditd on Linux)
- Detection method 3: Unusual time sync requests or user creation events in Windows event logs

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
- [[tools/rpcclient]]

## References

- Official documentation: https://www.samba.org/samba/docs/current/man-html/net.8.html
- Samba project: https://www.samba.org/
