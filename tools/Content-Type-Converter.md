---
url: BApp Store (Burp Suite extension)
tags:
  - burp-extension
  - content-conversion
type: tool
platforms:
  - Web
description: 'Burp Suite extension for converting request content types, such as to JSON.'
id: 74362976-d422-4e90-a956-ae588be41f52
created_at: '2025-12-11T06:10:31.037Z'
updated_at: '2025-12-11T06:10:31.037Z'
verified: false
validated: true
submitted: true
---
# Content-Type Converter

**Status**: Unverified

## Overview

Content-Type Converter is a Burp Suite extension that allows easy conversion of request content types, useful for exploits requiring specific formats like JSON.

## Description

Installed from the BApp Store, it integrates into Burp's HTTP Editor for right-click conversion options, enabling manipulations like array injections in payloads.

## Features

- Feature 1: Convert to JSON
- Feature 2: Other format conversions
- Feature 3: Seamless Burp integration

## Installation

### Requirements

- Burp Suite installed
- Access to BApp Store

### Install Commands

```bash
# Install from BApp Store within Burp Suite
```

## Basic Usage

```bash
# Right-click in HTTP Editor and select conversion
```

### Common Options

| Option | Description |
|--------|-------------|
| Convert to JSON | Changes content type to application/json |

## Examples

### Example 1: Basic Usage

```bash
# Select Extensions > Content-Type Converter > Convert to JSON
```

### Example 2: Advanced Usage

```bash
# Use in conjunction with request modification
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for converted request types
- Detection method 2: Extension usage logs in Burp

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

- BApp Store
