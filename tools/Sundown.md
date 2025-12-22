---
url: 'https://github.com/vmg/sundown'
tags:
  - markdown
  - deprecated
  - xss-vuln
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:31.076Z'
id: 0b9d6c6c-3272-44e4-9988-4aebd464a80e
validated: true
submitted: true
---
# Sundown

**Status**: Unverified

## Overview

Sundown is a deprecated Markdown processing library forked from Discount, used for fast and secure HTML rendering from Markdown, but requires proper configuration to prevent XSS.

## Description

In Gratipay, Sundown was wrapped by mikasa without the HTML_SAFELINK flag, permitting javascript: URIs in links and enabling Stored XSS. It claims security auditing but mandates flags like HTML_SAFELINK for safe link handling. Alternatives like Hoedown are recommended for ongoing use.

## Features

- Fast Markdown-to-HTML conversion
- Extension support (e.g., tables, footnotes)
- Security flags for output sanitization

## Installation

### Requirements

- C compiler
- Make

### Install Commands

```bash
git clone https://github.com/vmg/sundown.git
cd sundown
make
```

## Basic Usage

```c
#include <sundown.h>
// Initialize renderer with flags like HTML_SAFELINK
```

### Common Options

| Option | Description |
|--------|-------------|
| `HTML_SAFELINK` | Restrict link protocols to safe ones (http, https, etc.) |
| `HTML_ESCAPE` | Escape HTML entities |

## Examples

### Basic Usage

Compile and run a sample to process Markdown file to HTML.

### Advanced Usage

```c
sd_renderer *renderer = sdhtml_renderer_new(0, 0);  // Flags=0 is unsafe
```

## Expected Output

Safe HTML if flags set; otherwise, potentially malicious links.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Code searches for sundown includes without safelinks
- Vulnerability scanners flagging deprecated Markdown libs
- Runtime analysis of rendered output

## Related Procedures


## Related Tools

- [[tools/mikasa]]
- [[tools/Hoedown]]

## References

- https://github.com/vmg/sundown
- Security advisories on Markdown XSS
