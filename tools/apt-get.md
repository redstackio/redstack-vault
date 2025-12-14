---
id: tool-001
url: 'https://manpages.debian.org/buster/apt/apt-get.8.en.html'
tags:
  - package-manager
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.951Z'
validated: true
submitted: true
---
# apt-get

**Status**: Unverified

## Overview

apt-get is a command-line tool for handling packages on Debian-based Linux distributions, used here for installing build dependencies.

## Description

It fetches, installs, and manages software packages from repositories, essential for setting up development environments like cURL builds.

## Features

- Feature 1: Package installation and updates
- Feature 2: Dependency resolution
- Feature 3: System-wide management

## Installation

### Requirements

- Debian/Ubuntu base system

### Install Commands

```bash
# Pre-installed on most distros
```

## Basic Usage

```bash
apt-get --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-y` | Auto-yes |
| `update` | Refresh lists |

## Examples

### Example 1: Basic Usage

```bash
sudo apt-get update
```

### Example 2: Advanced Usage

```bash
sudo apt-get install -y clang valgrind
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Time Discovery]] System Services

### Tactics

- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Sudo logs for apt-get executions
- Package manager audit trails

## Related Procedures

- [[procedures/Building-cURL-with-Security-Debugging-Flags]]

## Related Tools

- [[tools/yum]]
- [[tools/dnf]]

## References

- Official man page
