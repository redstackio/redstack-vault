---
url: 'https://github.com/lc/gau'
tags:
  - reconnaissance
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.406Z'
id: 479d075d-813b-4806-adf9-fa8ff616656b
validated: true
submitted: true
---
# gau

**Status**: Unverified

## Overview

Gau (Get All URLs) is a command-line tool for retrieving URLs from public sources like the Wayback Machine, AlienVault OTX, and Common Crawl, primarily used in offensive security for passive reconnaissance to discover historical endpoints and potential exposures.

## Description

Gau excels at gathering archived web content without direct interaction with the target, making it ideal for identifying leaked secrets in old URLs. In this case, it was used to find an exposed WakaTime API key in a historical endpoint.

## Features

- Feature 1: Fetches URLs from multiple passive sources (Wayback, AlienVault, etc.)
- Feature 2: Filters by domain or subsdomain
- Feature 3: High-speed parallel processing for large domains

## Installation

### Requirements

- Go 1.13+ installed

### Install Commands

```bash
go install github.com/lc/gau/v2/cmd/gau@latest
```

## Basic Usage

```bash
gau --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |
| `-s` | Only subdomains |

## Examples

### Example 1: Basic Usage

```bash
gau wakatime.com
```

Retrieves all URLs for the domain.

### Example 2: Advanced Usage

```bash
gau -s wakatime.com | grep api
```

Fetches subdomain URLs and filters for API-related ones.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Engines]] Search Open Websites/Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to archive APIs (archive.org, otx.alienvault.com)
- Command-line process named 'gau' in reconnaissance phases

## Related Procedures

- [[procedures/Discover-Exposed-URLs-with-Gau]]

## Related Tools

- [[waybackurls]]
- [[hakrawler]]

## References

- Official documentation: https://github.com/lc/gau
- Related resources: OWASP Testing Guide on Reconnaissance
