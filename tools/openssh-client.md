---
url: 'https://www.openssh.com/'
tags:
  - ssh
  - remote-access
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.634Z'
id: 70fd2d92-9d72-4560-b828-aa6c33350088
validated: true
submitted: true
---
# openssh-client

**Status**: Unverified

## Overview

OpenSSH Client is a standard tool for secure remote login and command execution over SSH, commonly used in security testing for authenticated access to network devices like the Ubiquiti EdgeSwitch.

## Description

OpenSSH provides encrypted connections for authentication and remote command execution, essential for exploiting SSH-based vulnerabilities such as arbitrary command injection. In offensive operations, it's used to connect to targets, run shell commands, and facilitate privilege escalation without needing proprietary tools.

## Features

- Feature 1: Secure authentication via passwords or keys
- Feature 2: Remote command execution without interactive shell
- Feature 3: Port forwarding and tunneling for advanced access

## Installation

### Requirements

- Linux, Windows (via WSL or native), or macOS
- Network connectivity

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install openssh-client

# On macOS (Homebrew)
brew install openssh
```

## Basic Usage

```bash
ssh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p | Specify port (default 22) |
| -o | Set SSH options (e.g., StrictHostKeyChecking=no) |

## Examples

### Example 1: Basic Usage

```bash
ssh user@target_ip
```

### Example 2: Advanced Usage

```bash
ssh user@target_ip 'command'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]

### Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing SSH connections from external IPs
- Process monitoring for ssh/sshd executions
- Anomalous command patterns in SSH logs

## Related Procedures

- [[procedures/Authenticate-as-Privilege-0-User-on-Ubiquiti-EdgeSwitch]]
- [[procedures/Execute-Arbitrary-Shell-Commands-via-SSH-for-Root-Escalation]]

## Related Tools

- [[tools/putty]]

## References

- Official documentation: https://www.openssh.com/manual.html
- Related resources: SSH man pages
