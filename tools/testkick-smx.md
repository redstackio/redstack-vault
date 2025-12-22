---
url: null
tags:
  - plugin
  - csgo
  - xss
type: tool
platforms:
  - Windows
  - 'CS:GO'
description: Custom SourceMod plugin for testing kick payloads
id: 58a28fbe-62bd-4f4b-8dfe-3bc0688924da
created_at: '2025-12-14T00:11:25.193Z'
updated_at: '2025-12-14T00:11:25.193Z'
verified: false
validated: true
submitted: true
---
# Testkick Smx

**Status**: Unverified

## Overview

SourceMod plugin to test unlimited kick messages with XSS payloads in CS:GO.

## Description

Registers sm_testkick command and loops KickClient for payload delivery.

## Features

- Unlimited message size
- Custom kick testing

## Installation

### Requirements

- SourceMod

### Install Commands

```bash
# Place in addons/sourcemod/plugins
```

## Basic Usage

```bash
sm_testkick payload
```

### Common Options

| Option | Description |
|--------|-------------|
| `payload` | Kick message |

## Examples

### Example 1: Basic Usage

```bash
sm_testkick <a onmouseover=...>
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Plugin load events

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sourcemod]]

## References

- Custom plugin code
