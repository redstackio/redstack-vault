---
id: tool-sshd
url: 'https://www.openssh.com/'
tags:
  - ssh
  - service
  - demo
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.794Z'
validated: true
submitted: true
---
# sshd

**Status**: Unverified

## Overview

sshd is the OpenSSH daemon, a secure shell server for remote login and command execution. In security testing, it's used to demonstrate service detection via SSRF by running in debug mode on internal ports, logging connection attempts and exposing version information in responses.

## Description

OpenSSH's sshd provides encrypted network connectivity and is commonly deployed on Linux servers. For SSRF demos like phpBB exploitation, configure it on a non-standard port (e.g., 2222) in debug mode to capture and log incoming connections from the vulnerable application, revealing the attacker's probe without full authentication.

## Features

- Feature 1: Secure remote access via SSH protocol
- Feature 2: Debug mode for verbose logging of connection attempts
- Feature 3: Version banner exposure on connection for enumeration

## Installation

### Requirements

- Linux OS (e.g., Ubuntu)
- OpenSSH server package

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install openssh-server
```

## Basic Usage

```bash
sudo systemctl start ssh
sshd -d  # Debug mode on default port 22
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Debug mode, single instance with verbose output |
| `-p <port>` | Specify listening port (e.g., -p 2222) |
| `-f <config>` | Use custom config file |

## Examples

### Example 1: Basic Usage

```bash
sudo sshd -p 2222 -d
```

Runs sshd in debug mode on port 2222, logging connections.

### Example 2: Advanced Usage

```bash
sudo sshd -p 2222 -d -e /var/log/sshd.log
```

Debug mode with error output to log file for persistent monitoring.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (as target for enumeration)

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing connections to non-standard ports like 2222
- Debug logs in /var/log/auth.log with failed auth attempts from internal IPs
- Process monitoring for sshd -d instances

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://www.openssh.com/manual.html
- Related resources: OpenSSH GitHub
