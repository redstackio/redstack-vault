---
url: ''
tags:
  - debugging
  - web
type: tool
platforms:
  - Web
description: Tool for remotely debugging and executing code in embedded browser contexts.
id: 88f6d3cb-3238-4f60-bffb-46ec66585e64
created_at: '2025-12-11T06:10:17.236Z'
updated_at: '2025-12-11T06:10:17.236Z'
verified: false
validated: true
submitted: true
---
# Remote Chrome Console

**Status**: Unverified

## Overview

Remote Chrome Console allows debugging iframes and embedded contexts like OEMBED in Steam.

## Description

Used to inject and execute JS in restricted environments.

## Features

- Remote script execution
- Console access

## Installation

### Requirements

- Chrome with remote debugging enabled

### Install Commands

```bash
# Enable via flags
```

## Basic Usage

```bash
# Inject script to enable
```

### Common Options

| Option | Description |
|--------|-------------|
| --remote-debugging-port | Port |

## Examples

### Example 1: Basic Usage

Execute Object.keys(window) remotely.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Remote debugging port activity

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Chrome-DevTools]]

## References

- Chrome remote debugging docs
