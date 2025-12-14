---
url: 'https://gchq.github.io/CyberChef/'
tags:
  - encoding
  - payload-generation
type: tool
platforms:
  - Web
  - Linux
  - Windows
  - macOS
description: 'The Cyber Swiss Army Knife for encoding, minifying, and generating payloads.'
id: cd2467f5-f985-4d26-87eb-8f382772993e
created_at: '2025-12-13T23:56:20.331Z'
updated_at: '2025-12-13T23:56:20.331Z'
verified: false
validated: true
submitted: true
---
# CyberChef

**Status**: Unverified

## Overview

CyberChef is a web app for data transformation, encoding, and analysis, commonly used for creating encoded payloads in security testing.

## Description

Supports operations like Base64, URL encoding, JS minification, and regex replacements for crafting exploit links.

## Features

- Data encoding/decoding
- JavaScript minification
- Recipe-based transformations

## Installation

### Requirements

- Web browser

### Install Commands

```bash
# Web-based, no install needed
```

## Basic Usage

```bash
# Open in browser: https://gchq.github.io/CyberChef/
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Web interface |

## Examples

### Example 1: Basic Usage

Load recipe and input data.

### Example 2: Advanced Usage

Use for payload encoding.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Access to CyberChef domain
- Encoded payload patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp]]

## References

- https://gchq.github.io/CyberChef/
