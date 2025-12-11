---
id: bb395ba5-31a9-4a87-bd07-22f0caa85216
name: npm
type: tool
verified: false
created_at: '2025-12-11T03:48:06.046Z'
updated_at: '2025-12-11T03:48:06.046Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - package-management
  - node-js
url: 'https://www.npmjs.com/'
description: Node Package Manager for managing JavaScript packages
validated: true
submitted: true
---

# npm

**Status**: Unverified

## Overview

npm is the default package manager for Node.js, used to install, manage, and publish JavaScript packages. In security testing, it's often used for exploiting dependency-related vulnerabilities like confusion attacks.

## Description

npm allows developers to share and reuse code via packages. It connects to a public registry but can be configured for private use. In offensive security, it's leveraged for supply chain attacks by registering malicious packages.

## Features

- Package installation and dependency management
- Publishing to public or private registries
- Version control and scripting support

## Installation

### Requirements

- Node.js installed

### Install Commands

```bash
# npm is bundled with Node.js
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
| `-v, --version` | Show version |

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
- [[Compromise Software Supply Chain]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unexpected npm installations from public sources
- Audit package.json for suspicious dependencies

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #yarn
- #pnpm

## References

- https://docs.npmjs.com/
- Node.js documentation
