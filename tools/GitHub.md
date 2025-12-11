---
url: 'https://github.com'
tags:
  - recon
  - web
type: tool
platforms:
  - Web
description: >-
  Platform for hosting and searching public code repositories, often used for
  discovering leaked credentials.
id: ad95ecd1-1f03-4b17-95bf-5bc965c2435d
created_at: '2025-12-11T06:10:28.739Z'
updated_at: '2025-12-11T06:10:28.739Z'
verified: false
validated: true
submitted: true
---
# GitHub

**Status**: Unverified

## Overview

GitHub is a web-based platform for version control and collaboration, commonly used in offensive security for searching public repositories to find leaked sensitive information like API keys.

## Description

It allows users to search and access public codebases, which can reveal hard-coded credentials if not properly secured. In security testing, it's used for reconnaissance to identify potential entry points.

## Features

- Public repository search
- Code browsing and downloading
- Integration with other tools for automated scanning

## Installation

### Requirements

- Web browser
- Optional: GitHub account for advanced features

### Install Commands

No installation needed; access via web.

## Basic Usage

Navigate to https://github.com and use the search bar.

### Common Options

| Option | Description |
|--------|-------------|
| Search filters | Language, stars, etc. |

## Examples

### Example 1: Basic Usage

Search for "Starbucks JumpCloud".

### Example 2: Advanced Usage

Use advanced search for specific file types.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor outbound traffic to github.com
- Use secret scanning alerts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[TruffleHog]]

## References

- https://docs.github.com/en/search-github
