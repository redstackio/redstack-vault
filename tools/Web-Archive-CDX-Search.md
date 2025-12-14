---
id: tool-cdx-search-2380084
url: 'https://web.archive.org/cdx/search/cdx'
tags:
  - osint
  - archive
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.072Z'
validated: true
submitted: true
---
# Web-Archive-CDX-Search

**Status**: Unverified

## Overview

The Web Archive CDX Search is an API endpoint from the Internet Archive's Wayback Machine used to query and retrieve indexed captures of web pages for a domain, aiding in OSINT for discovering historical exposures.

## Description

This tool provides programmatic access to the CDX server, allowing searches by URL patterns, timestamps, and output formats. It's essential for reconnaissance without needing the full Wayback interface, as seen in exposing Mozilla's API keys.

## Features

- Feature 1: Domain-specific URL capture listing
- Feature 2: Configurable output (text, JSON, CSV)
- Feature 3: Filtering by MIME type, status code, or keywords

## Installation

### Requirements

- Internet access
- HTTP client like curl

### Install Commands

```bash
# No installation needed; use via curl
```

## Basic Usage

```bash
curl "https://web.archive.org/cdx/search/cdx?url=example.com/*"
```

### Common Options

| Option | Description |
|--------|-------------|
| `url=domain/*` | Target domain pattern |
| `output=text` | Plain text output |
| `fl=original` | Select fields like original URL |

## Examples

### Example 1: Basic Usage

```bash
curl "https://web.archive.org/cdx/search/cdx?url=subscriptions.firefox.com/*&output=text&fl=original"
```

### Example 2: Advanced Usage

```bash
curl "https://web.archive.org/cdx/search/cdx?url=domain.com/*&from=20230101&to=20231231&output=json"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Open Websites-Domains]] Search Open Technical Databases or Platforms

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- API request logs to web.archive.org/cdx
- High volume of archive queries from a single IP

## Related Procedures

- [[procedures/Query-Internet-Archive-CDX-for-Domain]]

## Related Tools

- [[tools/beautifier-io]]

## References

- Official documentation: https://archive.org/help/wayback_api.php
