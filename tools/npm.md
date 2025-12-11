---
url: 'https://www.npmjs.com/'
tags:
  - npm
  - package-manager
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Node Package Manager for managing JavaScript packages
id: 8fbe060b-240e-4720-9ea3-69ea7b165bd5
created_at: '2025-12-11T06:10:40.139Z'
updated_at: '2025-12-11T06:10:40.139Z'
verified: false
validated: true
submitted: true
---
# npm

**Status**: Unverified

## Overview

npm is the default package manager for Node.js, used to install, publish, and manage dependencies in JavaScript projects.

## Description

It interacts with the NPM registry to fetch and publish packages, commonly used in development for dependency management but exploitable in supply chain attacks like dependency confusion.

## Features

- Package installation and publishing.
- Dependency resolution.
- Scripting and automation.

## Installation

### Requirements

- Node.js installed.

### Install Commands

```bash
# Typically installed with Node.js
node -v  # Verify installation
```

## Basic Usage

```bash
npm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--loglevel=verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
npm install express
```

### Example 2: Advanced Usage

```bash
npm publish --access public
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Supply Chain Compromise]]
- [[Command-Line Interface]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor registry accesses.
- Audit package installations.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Node.js]]

## References

- https://docs.npmjs.com/
