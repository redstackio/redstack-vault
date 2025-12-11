---
url: BApp Store (Burp Suite extension store)
tags:
  - burp-extension
  - request-modification
type: tool
platforms:
  - Web
description: 'Burp Suite extension for converting request content types, such as to JSON.'
id: 7fbd4ff7-db79-435b-be09-b7b5f6b83e91
created_at: '2025-12-11T03:48:06.087Z'
updated_at: '2025-12-11T03:48:06.087Z'
verified: false
validated: true
submitted: true
---
# Content-Type Converter

**Status**: Unverified

## Overview

Content-Type Converter is a Burp Suite extension that allows easy conversion of HTTP request content types, useful for modifying payloads in different formats during web exploitation.

## Description

This extension integrates into Burp Suite's HTTP Editor, enabling right-click conversion options like to JSON, which is critical for exploits involving payload manipulation in web forms.

## Features

- Feature 1: Convert request to JSON, XML, etc.
- Feature 2: Seamless integration with Burp Suite
- Feature 3: Simplifies payload editing for vulnerability exploitation

## Installation

### Requirements

- Burp Suite installed
- Access to BApp Store

### Install Commands

```bash
# Install via Burp Suite's BApp Store interface
```

## Basic Usage

Right-click in HTTP Editor and select Convert to JSON.

### Common Options

| Option | Description |
|--------|-------------|
| Convert to JSON | Changes content type to application/json |
| Convert to XML | Changes to application/xml |

## Examples

### Example 1: Basic Usage

Intercept request, right-click, select Convert to JSON.

### Example 2: Advanced Usage

Convert and then modify JSON payload for array injection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for requests with unexpected content-type changes
- Detection method 2: Anomalous traffic patterns in web logs

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

- Burp Suite BApp Store
