---
url: null
tags:
  - web-testing
type: tool
platforms:
  - Web
description: Web browser for accessing and testing HTTP endpoints
id: e4c94b02-4925-4647-8972-ae6d40a6ffc7
created_at: '2025-12-11T06:10:15.990Z'
updated_at: '2025-12-11T06:10:15.990Z'
verified: false
validated: true
submitted: true
---
# Browser

**Status**: Unverified

## Overview

A standard web browser like Chrome or Firefox used for manually accessing URLs, inspecting responses, and testing web vulnerabilities such as CRLF injection.

## Description

Browsers enable direct interaction with web applications, including developer tools for viewing headers, cookies, and network traffic. Commonly used in offensive security for PoC demonstration.

## Features

- Network inspection: View HTTP requests and responses
- Cookie management: Observe set cookies
- URL manipulation: Test encoded parameters

## Installation

### Requirements

- Any OS
- Internet access

### Install Commands

Pre-installed on most systems; download from official sites if needed.

## Basic Usage

```bash
# Not applicable; use GUI to navigate to URL
```

### Common Options

| Option | Description |
|--------|-------------|
| Dev Tools | Inspect elements and network |
| Incognito | Test without existing cookies |

## Examples

### Example 1: Basic Usage

Navigate to the URL and open dev tools to inspect headers.

### Example 2: Advanced Usage

Use network tab to capture response from injected URL.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual access patterns in web logs
- Encoded CRLF in request parameters

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Bandicam]]

## References

- Browser documentation (e.g., Chrome DevTools)
