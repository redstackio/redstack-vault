---
id: 3e1ba3ce-f705-4d10-870c-0f04e81fe07f
name: publicwww.com
type: tool
verified: false
created_at: '2025-12-11T06:10:15.338Z'
updated_at: '2025-12-11T06:10:15.338Z'
platforms:
  - Web
tags:
  - recon
  - web
url: >-
  https://publicwww.com/websites/%22If%20you're%20reading%20this,%20you%20should%20visit%20automattic.com%22/
description: Website search engine for finding vulnerable sites.
validated: true
submitted: true
---

# publicwww.com

**Status**: Unverified

## Overview

PublicWWW is a search engine for websites' source code, used in reconnaissance to find potential vulnerable WordPress.com sites by querying specific strings.

## Description

It indexes web page source code, allowing searches for patterns like specific comments or scripts to identify targets running particular software or configurations.

## Features

- Feature 1: Source code searching
- Feature 2: Query-based site discovery
- Feature 3: Export results

## Installation

### Requirements

- Web browser

### Install Commands

No installation; web-based service.

## Basic Usage

Navigate to the URL and enter a query.

### Common Options

| Option | Description |
|--------|-------------|
| `query` | Search string |

## Examples

### Example 1: Basic Usage

Query: "If you're reading this, you should visit automattic.com"

### Example 2: Advanced Usage

Use filters for domain-specific searches.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor access to publicwww.com
- Detection method 2: Log reconnaissance queries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Browser-JavaScript-Console]]

## References

- Official PublicWWW website
