---
url: null
tags:
  - remote
  - debugging
type: tool
platforms:
  - Web
description: Tool for remote debugging in embedded contexts.
id: d475f578-3793-492d-9e77-327dbf7d4190
created_at: '2025-12-14T00:11:25.269Z'
updated_at: '2025-12-14T00:11:25.269Z'
verified: false
validated: true
submitted: true
---
# Remote Chrome Console

**Status**: Unverified

## Overview

Used for remotely debugging and executing code in iframes or embeds like codepen.io in Steam chat.

## Description

Inject scripts to enable remote console access for testing window properties and postMessage.

## Features

- Remote JS execution
- Context inspection

## Installation

### Requirements

- Chrome

### Install Commands

Built-in with DevTools.

## Basic Usage

Inject script for remote access.

### Common Options

| Option | Description |
|--------|-------------|
| Console | Remote exec |

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

- Unusual iframe activity

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

- Chrome debugging docs
