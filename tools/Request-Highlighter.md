---
url: 'https://portswigger.net/bappstore/11729a617d8d4d3b87c82e34b71885c3'
tags:
  - burp-extension
  - traffic-analysis
type: tool
platforms:
  - Windows
  - Linux
  - macOS
description: Burp extension for highlighting requests.
id: 7a2e8f45-0724-47fe-8866-0870a6c2b128
created_at: '2025-12-11T03:47:56.442Z'
updated_at: '2025-12-11T03:47:56.442Z'
verified: false
validated: true
submitted: true
---
# Request Highlighter

**Status**: Unverified

## Overview

Request Highlighter is a Burp Suite extension that colors requests based on criteria like User-Agent headers, used to distinguish traffic from different PlayStation Now components.

## Description

It enhances traffic analysis by visually separating requests, such as those with 'gkApollo' or 'Electron' headers.

## Features

- Feature 1: Custom highlighting rules
- Feature 2: Based on headers, methods, etc.
- Feature 3: Integration with Burp Proxy

## Installation

### Requirements

- Burp Suite

### Install Commands

```bash
# Install via BApp Store
```

## Basic Usage

Configure rules in Burp Extensions tab.

### Common Options

| Option | Description |
|--------|-------------|
| `Highlight based on` | Specify criteria |

## Examples

### Example 1: Basic Usage

Highlight 'gkApollo' User-Agent.

### Example 2: Advanced Usage

Multiple rules for different components.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Burp extension logs
- Detection method 2: Traffic pattern changes

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

- https://portswigger.net/bappstore
