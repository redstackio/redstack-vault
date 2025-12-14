---
url: 'https://www.npmjs.com/'
tags:
  - package-manager
  - installation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.553Z'
id: e13e5838-b029-4d9a-b237-f3070c79c031
validated: true
submitted: true
---
# npm

**Status**: Unverified

## Overview

npm (Node Package Manager) is the default package manager for Node.js, used to install, manage, and publish JavaScript packages, including vulnerable ones like Uppy Companion for SSRF exploitation in security testing.

## Description

npm handles dependency resolution, global/local installs, and script execution in Node.js environments. In offensive security, it's commonly used to deploy third-party modules with known vulnerabilities, such as the SSRF in @uppy/companion, allowing attackers to set up exploitable servers quickly.

## Features

- Feature 1: Global and local package installation with version pinning
- Feature 2: Dependency auditing and vulnerability scanning (npm audit)
- Feature 3: Script execution via package.json for automated setups

## Installation

### Requirements

- Node.js (includes npm by default)

### Install Commands

```bash
# npm comes with Node.js; update via
npm install -g npm@latest
```

## Basic Usage

```bash
npm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-g, --global` | Install packages globally |
| `-v, --version` | Show version |
| `--save` | Add to package.json dependencies |

## Examples

### Example 1: Basic Usage

```bash
npm install @uppy/companion
```

### Example 2: Advanced Usage

```bash
npm install -g @uppy/companion --audit
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to registry.npmjs.org
- Process monitoring for npm.exe or node processes installing packages
- Log analysis for global installs in system paths

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Node.js]]
- [[tools/Yarn]]

## References

- Official documentation: https://docs.npmjs.com/
- Related resources: Node.js security guides
