---
id: 1e2cda9c-4925-4f81-ad1c-5cf9dc4016ad
name: Browser Dev Tools
type: tool
verified: false
created_at: '2025-12-11T06:10:40.627Z'
updated_at: '2025-12-11T06:10:40.627Z'
platforms:
  - Web
tags:
  - debugging
  - inspection
url: ''
description: Browser developer tools for inspecting and debugging web applications
validated: true
submitted: true
---

# Browser Dev Tools

**Status**: Unverified

## Overview

Browser Dev Tools provide capabilities for inspecting network requests, copying CURL commands, and debugging web apps.

## Description

Essential for security researchers to capture and modify requests, such as updating staff information in web interfaces without verification.

## Features

- Feature 1: Network inspection
- Feature 2: CURL request copying
- Feature 3: Element debugging

## Installation

### Requirements

- Modern web browser

### Install Commands

```bash
# Built-in
```

## Basic Usage

```bash
# Open with F12
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | N/A |

## Examples

### Example 1: Basic Usage

Inspect network tab.

### Example 2: Advanced Usage

Copy as CURL from request.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Anomalous request patterns
- Detection method 2: Client-side modifications

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
- [[tools/Browser-Console]]

## References

- Official documentation
- Related resources
