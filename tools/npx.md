---
id: tool-003
url: 'https://www.npmjs.com/package/npx'
tags:
  - executor
type: tool
verified: false
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.490Z'
validated: true
submitted: true
---
---

# npx

**Status**: Unverified

## Overview

NPX executes Node.js packages without global installation, used here to run Sapper CLI and degit for setting up the vulnerable environment.

## Description

In security testing, NPX allows on-the-fly execution of tools like Sapper dev/build or degit clones, avoiding permanent installs while preparing exploits.

## Features

- Feature 1: Temporary package execution
- Feature 2: Automatic download if missing
- Feature 3: Integration with NPM ecosystem

## Installation

### Requirements

- Node.js and NPM

### Install Commands

```bash
# Bundled with NPM 5.2+
npm -v  # Check
```

## Basic Usage

```bash
npx --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Help |
| `--yes` | Skip prompts |

## Examples

### Example 1: Basic Usage

```bash
npx sapper dev
```

### Example 2: Advanced Usage

```bash
npx degit repo target
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- NPX processes
- Temporary cache in ~/.npm/_npx

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: npm]]

## References

- Official documentation: https://www.npmjs.com/package/npx

---
