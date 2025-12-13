---
url: 'https://www.google.com'
tags:
  - reconnaissance
  - google-dorking
type: tool
platforms:
  - Web
description: Web search engine used for reconnaissance and discovering indexed information.
id: ca83dbf9-9f38-47bd-bed0-2e53624dedac
created_at: '2025-12-13T09:01:26.419Z'
updated_at: '2025-12-13T09:01:26.419Z'
verified: false
validated: true
submitted: true
---
# Google Search

**Status**: Unverified

## Overview

Google Search is a powerful web search engine that can be used in security testing for reconnaissance, particularly through dork queries to find exposed information on target domains.

## Description

This tool allows querying indexed web pages, which can reveal sensitive data if sites lack proper crawling restrictions. It's commonly used in offensive security for gathering victim information from open sources.

## Features

- Site-specific searches
- Advanced operators like 'site:', 'inurl:'
- Result filtering controls

## Installation

### Requirements

- Web browser or curl

### Install Commands

No installation needed; access via web.

## Basic Usage

```bash
curl "https://www.google.com/search?q=site:example.com"
```

### Common Options

| Option | Description |
|--------|-------------|
| `q` | Query string |
| `filter=0` | Disable filtering |

## Examples

### Example 1: Basic Usage

```bash
curl "https://www.google.com/search?q=site:example.com"
```

### Example 2: Advanced Usage

```bash
curl "https://www.google.com/search?q=site:example.com&filter=0"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Open Websites-Domains]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitoring outbound traffic to google.com with suspicious queries
- Web server logs showing crawler activity

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Google-Chrome]]
- [[tools/Google-Toolbar]]

## References

- https://www.google.com
