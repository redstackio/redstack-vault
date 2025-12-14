---
id: tool-uuid-1
url: 'https://www.google.com'
tags:
  - recon
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.790Z'
validated: true
submitted: true
---
# Google-Search

**Status**: Unverified

## Overview

Google Search is a web search engine used for reconnaissance to discover public URLs and endpoints on target domains during security assessments.

## Description

In offensive security, it's employed to scrape site-specific pages via dorks, identifying forms and parameters vulnerable to injection without direct scanning tools.

## Features

- Feature 1: Advanced query operators like 'site:' and 'inurl:'
- Feature 2: Large index of public web content
- Feature 3: Free and accessible via browser or CLI tools like googler

## Installation

### Requirements

- Internet connection

### Install Commands

```bash
# For CLI: pip install googler
```

## Basic Usage

```bash
googler 'site:data.gov'
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | Number of results |
| `--json` | Output in JSON |

## Examples

### Example 1: Basic Usage

```bash
googler 'site:data.gov' -n 100
```

### Example 2: Advanced Usage

```bash
googler 'site:data.gov inurl:issue' --json > results.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual volume of search queries from IP.
- Log patterns matching dork strings.

## Related Procedures

- [[procedures/Gather-and-Explore-URLs-from-Google-Search]]

## Related Tools

- [[Shodan]]

## References

- Official documentation: https://www.google.com/search/howsearchworks/
