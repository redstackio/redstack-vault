---
url: 'https://www.npmjs.com/'
tags:
  - package-manager
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.008Z'
id: 6b23adde-d81f-483c-af4f-b4a0e0e11ca9
validated: true
submitted: true
---
# npm

**Status**: Unverified

## Overview

npm is the default package manager for Node.js, used to initialize projects and install dependencies like Express and vulnerable modules in security testing PoCs.

## Description

npm handles dependency resolution, installation, and project scripting, essential for reproducing Node.js vulnerabilities by pulling in specific package versions.

## Features

- Feature 1: Dependency installation and management
- Feature 2: package.json configuration
- Feature 3: Script execution

## Installation

### Requirements

- Node.js installed

### Install Commands

```bash
# npm comes with Node.js
node -v
npm -v
```

## Basic Usage

```bash
npm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --install | Install packages |
| -y | Auto-confirm init |
| -v | Version info |

## Examples

### Example 1: Basic Usage

```bash
npm init -y
```

### Example 2: Advanced Usage

```bash
npm i express@4.18.0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- package.json and node_modules presence
- npm install logs in CI/CD

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/node]]

## References

- Official documentation: https://docs.npmjs.com/
