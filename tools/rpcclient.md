---
id: c6f6d399-7ad1-44fb-bb64-5db4dac7198c
type: tool
verified: true
created_at: '2020-02-29T00:38:05.064399+00:00'
updated_at: '2023-05-30T19:51:14.399577+00:00'
platforms:
  - Linux
tags:
  - Enumeration
  - Network
commands:
  - '[[commands/rpcclient-authenticate-with-an-rpc-server]]'
url: 'https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html'
validated: true
---

# rpcclient

**Status**: ✓ Verified

## Overview

rpcclient is a command-line tool included in the Samba suite for interacting with Microsoft RPC (Remote Procedure Call) servers over SMB/CIFS. It provides an interactive shell for querying and enumerating Windows domain information, such as users, groups, domains, and security policies. Commonly used in penetration testing for Active Directory enumeration during reconnaissance and discovery phases.

## Description

rpcclient allows attackers or testers to connect to a target Windows system's RPC endpoints (e.g., SAMR, LSA) to perform operations like enumerating domain users and groups, querying user details, and looking up SIDs. It supports both anonymous (null) sessions for basic enumeration and authenticated sessions for deeper access. The tool is particularly useful against domain controllers or member servers exposing RPC services over port 445 (SMB).

## Features

- Interactive shell for RPC command execution
- Support for null authentication and credentialed logons
- Built-in commands for user/group enumeration (e.g., enumdomusers, queryuser)
- Domain lookup and SID resolution (e.g., lookupnames, samlookuprids)
- Policy and share querying (e.g., getdompwinfo, enumshares)

## Installation

### Requirements

- Samba suite (provides rpcclient)
- Network access to target SMB/RPC port (445/TCP)

### Install Commands

```bash
# On Debian/Ubuntu/Kali
sudo apt update
sudo apt install smbclient

# On CentOS/RHEL/Fedora
sudo yum install samba-client
# or
sudo dnf install samba-client

# Verify installation
rpcclient --help
```

## Basic Usage

```bash
rpcclient -U "username%password" <target_ip>
```

Once connected, enter the interactive shell and use commands like `enumdomusers` or `queryuser <rid>`.

### Common Options

| Option | Description |
|--------|-------------|
| `-U <user%pass>` | Specify username and password for authentication |
| `-I <ip>` | Target IP address |
| `-c <command>` | Execute a single RPC command non-interactively |
| `-N` | Use null (anonymous) authentication |

## Examples

### Example 1: Basic Usage (Null Session)

```bash
rpcclient -U "" 10.10.10.10
```

This attempts an anonymous connection to the target RPC server.

### Example 2: Advanced Usage (Authenticated Enumeration)

```bash
rpcclient -U "DOMAIN\\bob%secretpass" 10.10.10.10 -c "enumdomusers"
```

This runs a single command to enumerate domain users without entering the interactive shell.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery
- [[System Information Discovery]] System Information Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

- Monitor SMB traffic on port 445 for unusual RPC queries (e.g., enumdomusers patterns)
- Enable Windows Event Logging for RPC access (Event ID 5145 for share access, 4624 for logons)
- Use network IDS rules for rpcclient signatures or anomalous SMB sessions from external IPs
- Restrict RPC endpoints with firewalls and require authentication for SMB

## Related Procedures

- [[procedures/List-Domain-Users-and-Groups-with-MS-RPC-SMB-Service]]

## Related Tools

- [[tools/smbclient]]
- [[tools/Impacket]]

## References

- Official Samba Documentation: https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html
- MSRPC Enumeration Guide: https://pentestlab.blog/2017/04/25/msrpc-enumeration/
