---
id: tool-google-dorks-001
url: 'https://www.google.com'
tags:
  - recon
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.493Z'
validated: true
submitted: true
---
# Google-Dorks

**Status**: Unverified

## Overview

Google Dorks use advanced search operators to discover hidden or sensitive web content, ideal for reconnaissance in pentesting.

## Description

Operators like site: and intitle: filter results to uncover admin pages or parameters on targets like MTN sites. No installation needed; browser-based for offensive ops.

## Features

- Feature 1: Domain-specific searching
- Feature 2: Title and URL filtering
- Feature 3: Exposure of indexed vulnerabilities

## Installation

### Requirements

- Web browser

### Install Commands

```bash
# No installation; use Google search
```

## Basic Usage

```bash
google dorks --help
```

### Common Options

| Option | Description |
|--------|-------------|
| site: | Limit to domain |
| intitle: | Search in title |

## Examples

### Example 1: Basic Usage

```bash
site:example.com intitle:"admin"
```

### Example 2: Advanced Usage

```bash
site:example.com inurl:"login" filetype:php
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual search volume from IPs
- Query logs showing dork patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/SQLMap]]

## References

- Google Advanced Search docs
