---
url: 'https://www.openssh.com/'
tags:
  - remote-access
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Secure Shell client for remote access
id: 4b16ca77-d503-4a89-a5c7-3f8e64810f59
created_at: '2025-12-11T06:10:29.113Z'
updated_at: '2025-12-11T06:10:29.113Z'
verified: false
validated: true
submitted: true
---
# ssh

**Status**: Unverified

## Overview

ssh is used for secure remote login, here to gain RCE after key injection.

## Description

Enables encrypted remote shell access using key-based authentication.

## Features

- Feature 1: Key authentication
- Feature 2: Port forwarding
- Feature 3: Secure file transfer

## Installation

### Requirements

- OpenSSH package

### Install Commands

```bash
apt install openssh-client
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

- [[Remote Services]]

### Tactics

- [[Lateral Movement]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: SSH login logs
- Detection method 2: Anomalous connections

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[scp]]
- [[rsync]]

## References

- Official documentation: https://www.openssh.com/manual.html
