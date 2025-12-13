---
url: null
tags:
  - package-manager
type: tool
platforms:
  - Linux
description: Package manager for Node.js to install dependencies.
id: 1400f611-77ec-4a10-b1ff-c4a8a2bdf563
created_at: '2025-12-13T09:01:22.055Z'
updated_at: '2025-12-13T09:01:22.056Z'
verified: false
validated: true
submitted: true
---
# npm

**Status**: Unverified

## Overview

npm is the default package manager for Node.js, used to install and manage packages like Express.

## Description

Facilitates dependency installation for Node.js projects.

## Features

- Install packages
- Manage versions
- Scripts execution

## Installation

### Requirements

- Node.js

### Install Commands

```bash
# Comes with Node.js
```

## Basic Usage

```bash
npm install package
```

### Common Options

| Option | Description |
|--------|-------------|
| `install` | Install package |

## Examples

### Example 1: Basic Usage

```bash
npm install express
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques



### Tactics



## Detection

Indicators and methods for detecting this tool's usage:

- Monitor npm install commands

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Node-js]]

## References

- npm documentation
