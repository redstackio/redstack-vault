---
url: 'https://wiki.debian.org/apt'
tags:
  - package-manager
type: tool
verified: false
platforms:
  - Linux
  - Debian
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.870Z'
id: d2664e1a-4998-4071-a2ce-3706ea0fbd29
validated: true
submitted: true
---
# apt

**Status**: Unverified

## Overview

Debian/Ubuntu package manager for installing software, used in containers to acquire tools like Scapy for exploits.

## Description

apt handles dependency resolution and installation from repositories. In attacks, it's used to install runtime dependencies in non-immutable containers.

## Features

- Feature 1: Update package lists (apt update)
- Feature 2: Install packages (apt install)
- Feature 3: Auto-resolve dependencies

## Installation

### Requirements

- Debian-based OS

### Install Commands

```bash
# Already available on Ubuntu
apt update
```

## Basic Usage

```bash
apt --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -y | Yes to prompts |
| update | Refresh repos |
| install | Install package |

## Examples

### Example 1: Basic Usage

```bash
apt update
apt install vim
```

### Example 2: Advanced Usage

```bash
apt install -y python3-pip curl wget
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Audio Capture]] (Tool acquisition via packages)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- apt logs in /var/log/apt
- Unexpected package installs in container

## Related Procedures

- [[procedures/Install-Dependencies-and-Generate-SSH-Key]]

## Related Tools

- [[tools/yum]]

## References

- Official documentation: https://manpages.debian.org/buster/apt/apt.8.en.html
