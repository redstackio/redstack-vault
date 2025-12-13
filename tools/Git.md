---
url: ''
tags:
  - version-control
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Version control system for cloning repositories.
id: 69f31dc9-ecda-4722-bb92-8b23a86a58a9
created_at: '2025-12-13T09:01:22.321Z'
updated_at: '2025-12-13T09:01:22.321Z'
verified: false
validated: true
submitted: true
---
# Git

**Status**: Unverified

## Overview

Git is a distributed version control system used to clone and manage code repositories, essential for setting up exploit environments.

## Description

In offensive security, Git is commonly used to obtain proof-of-concept code or setups from GitHub for vulnerability reproduction.

## Features

- Clone repositories
- Manage branches
- Track changes

## Installation

### Requirements

- Internet access

### Install Commands

```bash
sudo apt install git  # On Debian-based systems
```

## Basic Usage

```bash
git --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

```bash
git clone https://github.com/example/repo.git
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor command-line executions for git clone
- Check network traffic to GitHub

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/docker-compose]]

## References

- https://git-scm.com/
