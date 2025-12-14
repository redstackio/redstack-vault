---
id: tool-wayback-machine
url: 'https://web.archive.org'
tags:
  - recon
  - archives
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.316Z'
validated: true
submitted: true
---
# Wayback-Machine

**Status**: Unverified

## Overview

The Wayback Machine is a digital archive of the World Wide Web maintained by the Internet Archive, allowing users to view historical versions of websites for research, reconnaissance, or data recovery in security contexts.

## Description

It crawls and stores snapshots of web pages over time, accessible via a simple URL interface. In offensive security, it's used to find exposed secrets in past versions of sites that may have been cleaned up on the live site, such as API keys in client-side code.

## Features

- Feature 1: Calendar-based snapshot navigation for specific URLs
- Feature 2: Full page rendering of historical content including JS and images
- Feature 3: Searchable archive with wildcard support for domains

## Installation

### Requirements

- Web browser (Chrome, Firefox, etc.)
- Internet connection

### Install Commands

No installation; access via https://web.archive.org.

## Basic Usage

```bash
# Browser: Visit https://web.archive.org/web/*/example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| web/*/* | Wildcard for all captures of a URL |
| Embed | Embed snapshots in other pages |

## Examples

### Example 1: Basic Usage

Navigate to https://web.archive.org/web/*/https://api.planet.com/ to view API endpoint history.

### Example 2: Advanced Usage

Use https://web.archive.org/web/20200101000000/https://api.planet.com/ for a specific timestamp.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Open Websites-Domains]] Search Open Websites and Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- No direct detection as it's passive web access; monitor for archive.org traffic in logs if relevant
- Unusual queries to historical endpoints may indicate reconnaissance

## Related Procedures

- [[procedures/Access-Wayback-Machine-Snapshots]]
- [[procedures/Extract-and-Validate-Exposed-API-Keys]]

## Related Tools

- [[Waybackpy]] (Python API wrapper)

## References

- Official site: https://archive.org/web/
- Removal policy: https://help.archive.org/help/how-to-request-a-website-be-removed-from-the-wayback-machine/
