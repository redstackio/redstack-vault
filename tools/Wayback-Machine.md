---
url: 'https://web.archive.org/'
tags:
  - archiving
  - proof
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:26.739Z'
id: e81c1f56-0b7f-4131-9a27-96e9fc448304
validated: true
submitted: true
---
# Wayback-Machine

**Status**: Unverified

## Overview

The Wayback Machine is the Internet Archive's service for capturing and accessing historical web snapshots.

## Description

It allows users to archive live pages for preservation, useful in security for proof of exploits like subdomain takeovers.

## Features

- Feature 1: On-demand snapshot requests
- Feature 2: Historical browsing
- Feature 3: API for automation

## Installation

### Requirements

- Browser

### Install Commands

No installation.

## Basic Usage

```bash
# Web-based
```

### Common Options

| Option | Description |
|--------|-------------|
| Save Page | URL input |

## Examples

### Example 1: Basic Usage

Enter http://svcardproxydevus.starbucks.com/ to archive.

### Example 2: Advanced Usage

Use API: curl "https://archive.org/save" -d url=example.com

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Archive via Utility]]

### Tactics

- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Requests to archive.org
- Snapshot alerts via monitoring

## Related Procedures

- [[procedures/Archive-Takeover-Proof-with-Wayback-Machine]]

## Related Tools


## References

- Site: https://web.archive.org/
