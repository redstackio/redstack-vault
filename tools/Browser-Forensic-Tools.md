---
id: tool-browser-forensics
url: 'https://www.nirsoft.net/utils/chrome_cache_view.html'
tags:
  - forensics
  - browser-analysis
  - credential-dump
type: tool
verified: false
platforms:
  - Windows
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.709Z'
validated: true
submitted: true
---
# Browser-Forensic-Tools

**Status**: Unverified

## Overview

Browser forensic tools are utilities designed to extract and analyze data from web browser storage, including cache, cookies, and history. They are commonly used in offensive security to recover sensitive information like cached API keys from compromised devices, particularly in scenarios involving information disclosure vulnerabilities.

## Description

These tools parse browser-specific data formats, such as Chrome's Cache SQLite database or Firefox's cache2 directory, to retrieve HTTP responses, form data, and stored credentials. In the context of client-side caching vulns, they enable attackers to dump plaintext sensitive data without needing live browser access. Features include filtering by URL, decoding compressed entries, and exporting to readable formats. Typically used post-compromise for data exfiltration in web app attacks.

## Features

- Feature 1: Cache entry parsing and decoding (e.g., WebP to plaintext)
- Feature 2: Search and filter for keywords like API keys
- Feature 3: Export to CSV/HTML for analysis

## Installation

### Requirements

- Administrative privileges on the target device
- .NET Framework (for Windows tools) or Python (for cross-platform)

### Install Commands

```bash
# For NirSoft ChromeCacheView (Windows portable, no install)
# Download from official site and run exe

# For cross-platform: pip install browser-cookie3 (for cookies, extend to cache)
```

## Basic Usage

```bash
ChromeCacheView.exe /shtml cache_report.html
```

### Common Options

| Option | Description |
|--------|-------------|
| /shtml | Export to HTML report |
| /stext | Export to text file |
| /filter | Filter by URL or content |

## Examples

### Example 1: Basic Usage

```bash
ChromeCacheView.exe
```

Opens GUI to browse and view cache entries.

### Example 2: Advanced Usage

```bash
ChromeCacheView.exe /shtml c:\output\cache.html /filter "kadira.io"
```

Exports filtered cache for specific domain to HTML.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials from Web Browsers]] Credentials from Web Browsers
- [[Credential Dumping]] OS Credential Dumping

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- File creation in temp directories (e.g., ChromeCacheView.exe)
- Anomalous access to browser data paths via process monitoring
- Network calls if tool uploads dumps

## Related Procedures


## Related Tools

- [[Autopsy]]
- [[Plaso]]

## References

- Official NirSoft documentation: https://www.nirsoft.net/utils/chrome_cache_view.html
- Browser forensics guides on SANS Institute
