---
id: tool-rvm
url: 'https://rvm.io'
tags:
  - ruby
  - manager
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.114Z'
validated: true
submitted: true
---
# rvm

**Status**: Unverified

## Overview

RVM (Ruby Version Manager) is a command-line tool for installing, managing, and switching multiple Ruby versions, essential for building environment-specific gems like rubyluabridge in security testing of Ruby-based apps.

## Description

RVM allows isolated Ruby environments, preventing conflicts in development or exploitation setups. In offensive security, it's used to match target Ruby versions (e.g., GitLab's 2.7.4) for compiling extensions that enable vulnerabilities.

## Features

- Feature 1: Installs Ruby from source with custom flags
- Feature 2: Manages gemsets for project isolation
- Feature 3: Shell integration for seamless switching

## Installation

### Requirements

- Bash shell
- curl or wget
- Build essentials (gcc, make)

### Install Commands

```bash
curl -sSL https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm  # For user install
```

## Basic Usage

```bash
rvm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `-v, --version` | Display version |

## Examples

### Example 1: Basic Usage

```bash
rvm install 2.7.4
rvm use 2.7.4
```

### Example 2: Advanced Usage

```bash
rvm install 2.7.4 --binary
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] Lua (via Ruby env setup)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of ~/.rvm directory
- rvm in process lists or shell history
- Multiple Ruby installs via `which -a ruby`

## Related Procedures

- [[procedures/Install-rubyluabridge-for-Lua-Extension]]

## Related Tools

- [[tools/apt]]

## References

- Official documentation: https://rvm.io/rvm/install
- Related resources: RubyGems.org
