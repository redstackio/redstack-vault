---
url: null
tags:
  - web
  - exploitation
type: tool
platforms:
  - Web
  - Linux
  - Windows
  - macOS
description: >-
  Standard browser for accessing, inspecting, and manipulating web URLs during
  testing.
id: 4f3bb4f6-4e74-479e-8cf3-fadd67920a03
created_at: '2025-12-14T17:33:24.363Z'
updated_at: '2025-12-14T17:33:24.363Z'
verified: false
validated: true
submitted: true
---
# Web Browser

**Status**: Unverified

## Overview

A web browser like Chrome or Firefox is essential for manual web exploitation, including URL manipulation, cookie inspection, and direct endpoint testing in security assessments.

## Description

Browsers enable loading URLs, editing parameters in the address bar, and observing responses. In attacks, they're used for token editing, redirect following, and verifying access without automated tools.

## Features

- Address bar for URL editing
- Developer tools for inspecting requests/responses
- Cookie and session management

## Installation

### Requirements

- Operating system with GUI

### Install Commands

```bash
# For Chrome on Ubuntu
sudo apt install google-chrome-stable
```

## Basic Usage

```
Open URL in address bar
```

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open DevTools |
| Ctrl+Shift+I | Inspect elements |

## Examples

### Example 1: Basic Usage

Load https://example.com

### Example 2: Advanced Usage

Edit token in address bar and reload

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- User-agent strings in logs
- Direct URL access patterns

## Related Procedures


## Related Tools

- [[tools/Google-Search]]

## References

- Browser documentation (e.g., Chrome DevTools)
