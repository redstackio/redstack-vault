---
type: tool
verified: true
platforms:
  - Linux
  - Windows
tags:
  - network
  - service-attacks
url: 'https://linux.die.net/man/8/showmount'
validated: true
---

# showmount

**Status**: ✓ Verified

## Overview

showmount is a command-line utility used to query the mount daemon on a remote host for information about the state of the NFS (Network File System) server on that machine. With no options, it lists the set of clients who are mounting from that host. It is commonly used in security testing for discovering NFS shares and potential misconfigurations that could allow unauthorized access to file systems.

## Description

showmount interacts with the NFS server's portmapper (rpcbind) to retrieve details about exported file systems, including which directories are shared and their access permissions. This tool is particularly useful during reconnaissance phases to identify open NFS services and enumerate shares without needing to mount them. It supports options for listing exports, mounted directories, and filtering by host. On Windows, it can be used via Cygwin or WSL, though native support is limited.

## Features

- Feature 1: List NFS exports on a remote server with access controls
- Feature 2: Display clients currently mounting shares from the server
- Feature 3: Filter output by specific hosts or directories for targeted enumeration

## Installation

### Requirements

- NFS client utilities (nfs-common on Linux)
- Network access to the target's RPC port (typically 111/udp and 2049/tcp)

### Install Commands

```bash
# On Debian/Ubuntu
sudo apt update && sudo apt install nfs-common

# On Kali Linux (pre-installed)
# No action needed

# On Windows (via WSL or Cygwin)
# Install Ubuntu WSL and run the above, or use Cygwin setup for nfs-utils
```

## Basic Usage

```bash
showmount --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -e, --exports | List NFS exports on the specified host |
| -a, --all | List all clients mounting from the host |
| -d, --directories | List directories that are mounted by clients |
| -h, --host HOST | Specify the remote host to query |
| -v, --verbose | Provide verbose output |

## Examples

### Example 1: Basic Usage

List NFS exports on a target host:

```bash
showmount -e 10.10.10.10
```

### Example 2: Advanced Usage

List all mounted directories:

```bash
showmount -d 10.10.10.10
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor RPC traffic to port 111/udp from internal hosts
- Detection method 2: Log queries to NFS services (rpc.mountd) and alert on unauthorized enumeration attempts
- Detection method 3: Network IDS rules for showmount RPC calls (program 100005)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/rpcinfo]]

## References

- Official man page: https://linux.die.net/man/8/showmount
- NFS documentation: https://www.ietf.org/rfc/rfc1094.txt
