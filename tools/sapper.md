---
id: tool-005
url: 'https://www.npmjs.com/package/sapper'
tags:
  - framework
  - cli
type: tool
verified: false
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.471Z'
validated: true
submitted: true
---
---

# sapper

**Status**: Unverified

## Overview

Sapper is a framework CLI for building Svelte apps, vulnerable in version 0.27.10 to path traversal in static file serving.

## Description

Sapper's runtime handles /client/ requests without path validation, allowing encoded '../' traversal. Used in research to build and run vulnerable servers for exploitation.

## Features

- Feature 1: Dev and build modes
- Feature 2: Static asset serving
- Feature 3: Svelte integration

## Installation

### Requirements

- Node.js, NPM

### Install Commands

```bash
npm i sapper@0.27.10
```

## Basic Usage

```bash
npx sapper --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `dev` | Start dev server |
| `build` | Production build |

## Examples

### Example 1: Basic Usage

```bash
npx sapper dev
```

### Example 2: Advanced Usage

```bash
npx sapper build
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Sapper processes on port 3000
- Build artifacts in __sapper__build

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: svelte]]

## References

- Official documentation: https://sapper.svelte.dev/

---
