---
id: tool-001
url: 'https://www.google.com'
tags:
  - reconnaissance
  - osint
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.961Z'
validated: true
submitted: true
---
# Google-Dorking

**Status**: Unverified

## Overview

Google Dorking is a technique using advanced Google search operators to uncover sensitive information or hidden endpoints on websites, commonly used in reconnaissance for security assessments.

## Description

This method exploits Google's indexing to find exposed files, directories, or vulnerable parameters without direct interaction with the target. In offensive ops, it's ideal for discovering PHP endpoints or login pages on subdomains. Features include site:, inurl:, filetype: operators for precise queries.

## Features

- Feature 1: Site-specific searches to limit to subdomains
- Feature 2: Filetype filtering for code exposure (e.g., .php)
- Feature 3: Parameter discovery via inurl: for injection points

## Installation

### Requirements

- Web browser
- No installation needed

### Install Commands

N/A

## Basic Usage

```bash
# In browser search bar
site:target.gov filetype:php
```

### Common Options

| Option | Description |
|--------|-------------|
| `site:` | Restrict to domain |
| `inurl:` | Search in URL |
| `filetype:` | Limit file types |

## Examples

### Example 1: Basic Usage

Search: site:subdomain.gov inurl:.php

### Example 2: Advanced Usage

Search: site:subdomain.gov inurl:search.php "error"

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Search Engines

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual search volume from IPs querying domain
- No direct detection; focus on exposed assets

## Related Procedures

- [[procedures/Google-Dorking-for-Vulnerable-PHP-Endpoints]]

## Related Tools

- [[Shodan]]
- [[Censys]]

## References

- Google Advanced Search documentation
- OSINT Framework resources
