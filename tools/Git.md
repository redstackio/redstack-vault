---
url: 'https://git-scm.com/'
tags:
  - version-control
  - cloning
type: tool
platforms:
  - macOS
  - Linux
  - Windows
description: Version control system
id: e4fbe8b0-03c9-4e63-8e49-e6b70e12d722
created_at: '2025-12-11T06:10:40.452Z'
updated_at: '2025-12-11T06:10:40.452Z'
verified: false
validated: true
submitted: true
---
# git

**Status**: Unverified

## Overview

git is a distributed version control system used in security contexts to clone repositories and verify access permissions with leaked credentials.

## Description

In attack chains, git clones repos to prove read access, computing hashes for proof without full disclosure, as in GitHub token exploitation.

## Features

- Repository cloning
- Commit management
- Branching and merging

## Installation

### Requirements

- Standard on many systems

### Install Commands

```bash
apt install git
```

## Basic Usage

```bash
git --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `clone` | Clone repository |
| `log` | Show commit logs |

## Examples

### Example 1: Basic Usage

```bash
git clone https://github.com/user/repo
```

### Example 2: Advanced Usage

```bash
git clone https://token@github.com/org/repo
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor git clone activities
- Detect unauthorized repo accesses

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[github-cli]]

## References

- https://git-scm.com/docs
