---
url: 'https://github.com/hoedown/hoedown'
tags:
  - markdown
  - xss-prevention
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:31.071Z'
id: ba675bd3-05a8-495e-8e55-3ee6f43fdd54
validated: true
submitted: true
---
# Hoedown

**Status**: Unverified

## Overview

Hoedown is a fork of the Sundown Markdown library, providing similar fast processing with warnings about the need for post-processing to prevent XSS in rendered output.

## Description

As an alternative to Sundown, Hoedown emphasizes security by documenting the requirement for additional sanitization after rendering, such as stripping unsafe attributes. In the Gratipay context, it could mitigate the XSS if used with proper post-processing, unlike the misconfigured Sundown.

## Features

- Compatible with Sundown API
- Buffer management for efficient parsing
- Extension handling

## Installation

### Requirements

- C compiler

### Install Commands

```bash
git clone https://github.com/hoedown/hoedown.git
cd hoedown
make
make install
```

## Basic Usage

```c
#include <hoedown.h>
// Render with post-processing for safety
```

### Common Options

| Option | Description |
|--------|-------------|
| `extensions` | Enable Markdown features |
| `renderer_flags` | Set output restrictions |

## Examples

### Basic Usage

Process a Markdown string to HTML with safety checks.

### Advanced Usage

Integrate with HTML sanitizers post-render.

## Expected Output

HTML requiring manual XSS checks; safer with add-ons.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Dependency scans for hoedown in codebases
- Review for post-processing implementations

## Related Procedures


## Related Tools

- [[tools/Sundown]]

## References

- https://github.com/hoedown/hoedown
- XSS prevention guides for Markdown
