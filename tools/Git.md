---
url: 'https://git-scm.com/'
tags:
  - version-control
  - recon
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Version control system for tracking changes in source code.
id: 104c3999-1056-4ec6-8ad7-b26047741536
created_at: '2025-12-11T03:48:06.075Z'
updated_at: '2025-12-11T03:48:06.075Z'
verified: false
validated: true
submitted: true
---
# git

**Status**: Unverified

## Overview

Git is a distributed version control system used for software development, often employed in security testing to clone and inspect repositories for leaked information.

## Description

Git allows cloning, committing, and searching repositories. In offensive security, it's used to discover sensitive data in public repos.

## Features

- Clone repositories: Download remote repos
- Log searching: Inspect commit history
- Branch management: Handle multiple code versions

## Installation

### Requirements

- Compatible OS

### Install Commands

```bash
sudo apt install git  # Debian-based
```

## Basic Usage

```bash
git --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `clone` | Clone a repository |

## Examples

### Example 1: Basic Usage

```bash
git clone https://github.com/example-repo.git
```

### Example 2: Advanced Usage

```bash
git log -p | grep sensitive
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Network Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for git clone traffic to public repos
- Log unusual repository accesses

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #curl

## References

- https://git-scm.com/docs
