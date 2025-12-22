---
url: 'https://man.openbsd.org/ssh-keygen'
tags:
  - ssh
  - keygen
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.864Z'
id: 528a2416-166a-4f9b-b755-14606174444d
validated: true
submitted: true
---
# ssh-keygen

**Status**: Unverified

## Overview

Utility to generate, manage, and convert SSH keys for authentication, used to create keys for injection in privilege escalation attacks.

## Description

Part of OpenSSH, ssh-keygen supports various algorithms like ed25519 and RSA. In security ops, it's used to generate backdoor keys for persistent access.

## Features

- Feature 1: Key pair generation
- Feature 2: Passphrase protection
- Feature 3: Key conversion and fingerprinting

## Installation

### Requirements

- OpenSSH package

### Install Commands

```bash
# On Ubuntu
apt install openssh-client
```

## Basic Usage

```bash
ssh-keygen --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t | Type (ed25519, rsa) |
| -f | File name |
| -N | Passphrase |

## Examples

### Example 1: Basic Usage

```bash
ssh-keygen -t rsa
```

### Example 2: Advanced Usage

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ''
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Device Authentication]] Network Credential Access

### Tactics

- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- New keys in ~/.ssh
- ssh-keygen processes

## Related Procedures

- [[procedures/Install-Dependencies-and-Generate-SSH-Key]]

## Related Tools

- [[tools/openssh-client]]

## References

- Man page: https://man.openbsd.org/ssh-keygen
