---
id: tool-uuid-1
url: 'https://publicwww.com'
tags:
  - recon
  - search
type: tool
verified: false
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.874Z'
validated: true
submitted: true
---
# publicwww-com

**Status**: Unverified

## Overview

publicwww.com is a search engine for scanning billions of web pages to find sites containing specific code snippets, strings, or patterns, useful for identifying vulnerable websites using features like Jetpack Likes in WordPress.

## Description

The tool allows querying for JavaScript code, HTML elements, or text to estimate the attack surface, such as searching for 'jetpack likes' to find over 100k potentially vulnerable domains. It's web-based, no installation needed, and supports regex for precise searches in offensive security reconnaissance.

## Features

- Feature 1: Code snippet search across public websites
- Feature 2: Regex support for advanced pattern matching
- Feature 3: Result counts and sample URLs for validation

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

No installation; access via https://publicwww.com

## Basic Usage

```bash
# No CLI; use web interface
```

### Common Options

| Option | Description |
|--------|-------------|
| Search Query | Enter string like "showOtherGravatars" |
| Regex Mode | Enable for pattern searches |

## Examples

### Example 1: Basic Usage

Search for "jetpack likes" to find sites using the feature.

### Example 2: Advanced Usage

Query `/showOtherGravatars.*avatar_URL/` to match vulnerable code patterns.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to publicwww.com from recon IPs
- Queries in logs matching vulnerability patterns

## Related Procedures


## Related Tools

- [[Shodan]]
- [[Censys]]

## References

- Official site: https://publicwww.com
- Usage guide: Tool's help section
