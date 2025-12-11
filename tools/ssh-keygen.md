---
url: 'https://www.openssh.com/'
tags:
  - ssh
  - key-management
type: tool
platforms:
  - Linux
  - macOS
description: Utility for generating and managing SSH keys and certificates.
id: 46f4180a-8207-4890-9885-b025dc7a6c6f
created_at: '2025-12-11T03:47:39.312Z'
updated_at: '2025-12-11T03:47:39.312Z'
verified: false
validated: true
submitted: true
---
# ssh-keygen

**Status**: Unverified

## Overview

ssh-keygen is a standard OpenSSH tool for creating SSH key pairs and signing certificates, commonly used in security testing for authentication-related exploits.

## Description

It generates RSA, ECDSA, or Ed25519 keys and can sign certificates with custom extensions, enabling scenarios like authentication bypass via manipulated certificates.

## Features

- Key pair generation
- Certificate signing with extensions
- Key management and conversion

## Installation

### Requirements

- OpenSSH installed

### Install Commands

```bash
# Typically pre-installed on Unix-like systems; install via package manager if needed
sudo apt install openssh-client
```

## Basic Usage

```bash
ssh-keygen --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-t` | Key type |
| `-s` | Sign with CA key |
| `-O` | Specify certificate options |

## Examples

### Example 1: Basic Usage

```bash
ssh-keygen -t ed25519
```

### Example 2: Advanced Usage

```bash
ssh-keygen -s ca_key -O extension:custom=value user.pub
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Use Alternate Authentication Material]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unusual ssh-keygen executions in logs
- Detect creation of certificates with suspicious extensions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #git

## References

- Official OpenSSH documentation
