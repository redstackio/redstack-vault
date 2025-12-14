---
url: null
tags:
  - saml
  - poc
type: tool
platforms:
  - Linux
  - macOS
description: Python script for crafting SAML bypass payloads by manipulating XML responses.
id: da64e5d7-ec9c-4333-b19f-624395097cde
created_at: '2025-12-14T17:31:19.318Z'
updated_at: '2025-12-14T17:31:19.318Z'
verified: false
validated: true
submitted: true
---
# samlbypasspoc.py

**Status**: Unverified

## Overview

A proof-of-concept Python script designed to exploit SAML validation flaws by prepending malicious Response elements to valid signed SAML XML, enabling authentication bypass in tools like Rocket.Chat.

## Description

The script decodes input, parses XML, injects a custom Response with forged assertions, re-encodes, and outputs. It's tailored for the Rocket.Chat vuln in saml_utils.js, where first Response is used unchecked.

## Features

- Feature 1: XML parsing and modification with ElementTree
- Feature 2: Customizable assertion forgery (NameID, Email, etc.)
- Feature 3: Base64 URL encoding/decoding

## Installation

### Requirements

- Python 3.6+
- No external libs (uses stdlib xml.etree)

### Install Commands

```bash
# Download script from source (e.g., HackerOne report attachments)
# Make executable
chmod +x samlbypasspoc.py
```

## Basic Usage

```bash
python3 samlbypasspoc.py <input>
```

### Common Options

| Option | Description |
|--------|-------------|
| Edit lines 25+ | Customize malicious Response attributes |

## Examples

### Example 1: Basic Usage

```bash
python3 samlbypasspoc.py PHNhbWw6UmVzcG9uc2U+...
```

### Example 2: Advanced Usage

Modify script for admin assertions, then run with piped input.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes with XML parsing on SAML endpoints
- Modified SAML XML in logs
- Script artifacts in temp files

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]

## References

- Source: https://hackerone.com/reports/812064
- Related resources: SAML XML security guides
