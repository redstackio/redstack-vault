---
url: 'https://fast.wistia.com/assets/external/E-v1.js'
tags:
  - video-embed
  - javascript
type: tool
platforms:
  - Web
description: >-
  Script for embedding Wistia videos, vulnerable to prototype pollution in this
  case.
id: f96526d2-83db-4caa-ac17-b87b6b93f8c4
created_at: '2025-12-13T23:56:20.385Z'
updated_at: '2025-12-13T23:56:20.385Z'
verified: false
validated: true
submitted: true
---
# Wistia Embed Script

**Status**: Unverified

## Overview

E-v1.js is used for video embedding but contains a vulnerability in URL parsing that allows prototype pollution.

## Description

The script parses URLs without validation, enabling exploitation via query parameters.

## Features

- Video embedding
- URL parsing

## Installation

### Requirements

- Web page

### Install Commands

<script async src="https://fast.wistia.com/assets/external/E-v1.js"></script>

## Basic Usage

Embed video code.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Script-based |

## Examples

### Example 1: Basic Usage

Load script on page.

### Example 2: Advanced Usage

Exploit with query params.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for polluted prototypes
- Script load anomalies

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Browser]]

## References

- Wistia documentation
