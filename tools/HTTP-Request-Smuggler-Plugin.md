---
url: null
tags:
  - smuggling
  - burp-plugin
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Assists in detecting and exploiting HTTP Request Smuggling vulnerabilities by
  crafting desynchronized requests.
id: 1160b0e9-c97a-49e6-87d6-5bb948f624bb
created_at: '2025-12-13T09:01:17.606Z'
updated_at: '2025-12-13T09:01:17.606Z'
verified: false
validated: true
submitted: true
---
# HTTP Request Smuggler Plugin

**Status**: Unverified

## Overview

This Burp Suite plugin helps in identifying and exploiting HTTP Request Smuggling vulnerabilities through automated scanning and request crafting.

## Description

It integrates with Burp Suite to scan for CL.TE, TE.CL, and other smuggling variants, generating POCs for exploitation.

## Features

- Feature 1: Automated smuggling detection
- Feature 2: POC request generation
- Feature 3: Integration with Burp tools

## Installation

### Requirements

- Burp Suite

### Install Commands

```bash
# Install via Burp's BApp Store
```

## Basic Usage

```bash
# Use within Burp Suite interface
```

### Common Options

| Option | Description |
|--------|-------------|
| `Scan` | Initiate scan |

## Examples

### Example 1: Basic Usage

Scan target in Burp.

### Example 2: Advanced Usage

Generate POC for specific variant.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Plugin-specific requests
- Detection method 2: Burp extension logs

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

- Burp Extender documentation
