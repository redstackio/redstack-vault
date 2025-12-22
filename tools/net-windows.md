---
type: tool
description: >-
  The net command is a built-in Windows utility for managing network resources,
  user accounts, shares, and policy settings.
url: >-
  https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net
tags:
  - network
  - configure
  - post-exploitation
platforms:
  - Windows
verified: true
validated: true
---

# net-windows

**Status**: Verified

## Overview

The net command is a versatile, built-in Windows command-line tool used for viewing and configuring network settings, managing user accounts, creating shares, and handling connections to remote resources. In security testing, it's commonly used for post-exploitation tasks like mounting remote SMB shares, enumerating users, or adding accounts for persistence.

## Description

Net provides subcommands like `net use` for mapping network drives, `net user` for account management, `net share` for file sharing, and `net accounts` for policy configuration. It operates locally or remotely with appropriate credentials, making it useful for lateral movement and privilege escalation in Windows environments. No external installation is required as it's native to all modern Windows versions.

## Features

- Network resource management: Connect/disconnect shares, map drives.
- User and group administration: Add, delete, or modify accounts.
- Share configuration: Create or delete network shares.
- Policy settings: View or set account lockout and password policies.

## Installation

### Requirements

- Windows OS (XP or later).
- Administrative privileges for most operations.

### Install Commands

Net is pre-installed on all Windows systems. No installation needed.

```command_prompt
# Verify availability
net /?
```

## Basic Usage

```command_prompt
net /help
```

### Common Options

| Option | Description |
|--------|-------------|
| `/help` or `/?` | Display help for the command. |
| `use` | Manage network connections. |
| `user` | Manage user accounts. |
| `share` | Manage shared resources. |

## Examples

### Example 1: Basic Usage

View current network connections:

```command_prompt
net use
```

### Example 2: Advanced Usage

Mount a remote share (see related command for details):

```command_prompt
net use Z: \\remote-server\share /user:domain\user password
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[SMB-Windows Admin Shares]] SMB/Windows Admin Shares
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Event logs: Monitor Security event ID 5145 for share access, 4624 for logons.
- Process monitoring: net.exe executions with suspicious arguments like remote IPs.
- Network traffic: SMB connections to unusual hosts.

## Related Procedures

- Procedures using net for share mounting or account creation.

## Related Tools

- [[smbclient-linux]]
- [[psexec-windows]]

## References

- Official Microsoft documentation: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1021/002/
