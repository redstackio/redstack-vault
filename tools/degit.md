---
id: tool-004
url: 'https://www.npmjs.com/package/degit'
tags:
  - shallow-clone
type: tool
verified: false
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.475Z'
validated: true
submitted: true
---
---

# degit

**Status**: Unverified

## Overview

Degit performs shallow Git clones of repositories or branches, used to obtain specific Sapper template examples without full history.

## Description

For offensive security, Degit enables quick setup of vulnerable project variants, like the Webpack branch, to test path traversal in isolated environments.

## Features

- Feature 1: Shallow, fast cloning
- Feature 2: Branch/tag targeting
- Feature 3: Force overwrite options

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm install -g degit
```

## Basic Usage

```bash
degit --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Help |
| `--force` | Overwrite existing |

## Examples

### Example 1: Basic Usage

```bash
degit repo target
```

### Example 2: Advanced Usage

```bash
degit "repo#branch" dir --force
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Degit process logs
- Shallow repo artifacts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: git]]

## References

- Official documentation: https://github.com/richtr/degit

---
