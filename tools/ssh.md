---
id: tool-ssh
url: 'https://www.openssh.com/'
tags:
  - remote-access
  - tunnel
  - protocol
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.341Z'
validated: true
submitted: true
---
---
# SSH

**Status**: Unverified

## Overview

SSH (Secure Shell) is a protocol and tool for secure remote login and command execution, widely used for tunneling and port forwarding in security assessments.

## Description

In this context, SSH creates reverse tunnels to expose internal services like Docker Registries from sandboxed environments to external attackers, bypassing network restrictions.

## Features

- Feature 1: Encrypted connections
- Feature 2: Port forwarding (local/remote)
- Feature 3: Key-based and password authentication

## Installation

### Requirements

- OpenSSH package

### Install Commands

```bash
# On Linux
apt install openssh-client openssh-server
```

## Basic Usage

```bash
ssh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-R` | Remote port forward |
| `-f` | Background |
| `-N` | No exec |

## Examples

### Example 1: Basic Usage

```bash
ssh user@host
```

### Example 2: Advanced Usage

```bash
ssh -R 5555:localhost:5000 user@host -f -N
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Protocol Tunneling]] Protocol Tunneling
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- SSH logs showing forwards from internal IPs
- Network flows to external SSH servers
- Auth failures or unusual sessions

## Related Procedures


## Related Tools

- [[tools/netcat]]

## References

- Official documentation: https://www.openssh.com/manual.html
- Related resources: RFC 4251

---
