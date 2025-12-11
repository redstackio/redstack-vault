---
url: 'https://www.openssh.com/'
tags:
  - remote-access
  - ssh
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Secure Shell client for remote access
id: 15646535-3d14-4f8e-a45c-a31e5a840764
created_at: '2025-12-11T03:47:47.555Z'
updated_at: '2025-12-11T03:47:47.555Z'
verified: false
validated: true
submitted: true
---
# ssh

**Status**: Unverified

## Overview

ssh is a protocol and tool for secure remote login and command execution.

## Description

Used to gain remote access after key injection in exploits.

## Features

- Feature 1: Key-based auth
- Feature 2: Port forwarding

## Installation

### Requirements

- OpenSSH package

### Install Commands

```bash
sudo apt install openssh-client
```

## Basic Usage

```bash
ssh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i` | Identity file |
| `-p` | Port |

## Examples

### Example 1: Basic Usage

```bash
ssh user@host
```

### Example 2: Advanced Usage

```bash
ssh -i keyfile user@host
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[tools/ssh]]

### Tactics

- [[Lateral Movement]]

## Detection

Indicators and methods for detecting this tool's usage:

- SSH login logs
- Network traffic to port 22

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #scp
- #sftp

## References

- Official site: https://www.openssh.com/
