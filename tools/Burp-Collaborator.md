---
url: null
tags:
  - oob
  - logging
type: tool
platforms:
  - Web
description: Out-of-band interaction logger for Burp Suite
id: fc7fbafb-78eb-4544-bea6-c638b82f8d34
created_at: '2025-12-13T09:01:26.100Z'
updated_at: '2025-12-13T09:01:26.101Z'
verified: false
validated: true
submitted: true
---
# Burp Collaborator

**Status**: Unverified

## Overview

Burp Collaborator is a server that logs out-of-band interactions like DNS lookups and HTTP requests, used in exploits involving redirects or exfiltration.

## Description

It generates unique URLs for redirects, polling every second to capture leaked data such as session tokens from victim requests.

## Features

- DNS and HTTP logging
- Polling for real-time detection
- Integration with Burp Suite

## Installation

### Requirements

- Burp Suite Professional

### Install Commands

```bash
# Integrated in Burp Suite
```

## Basic Usage

Generate URL in Burp and poll.

### Common Options

| Option | Description |
|--------|-------------|
| Poll interval | Set to 1 second |

## Examples

### Example 1: Basic Usage

Use generated URL in payload.

### Example 2: Advanced Usage

Monitor for token leaks.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unexpected DNS queries to collaborator domains
- Anomalous HTTP redirects

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]

## References

- PortSwigger resources
