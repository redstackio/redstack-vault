---
url: 'https://requestbin.com'
tags:
  - request-capture
  - web-testing
type: tool
platforms:
  - Web
description: Online service for capturing and inspecting HTTP requests.
id: 4f499f4e-5cb6-412c-87b3-a443f0b99007
created_at: '2025-12-13T09:01:21.860Z'
updated_at: '2025-12-13T09:01:21.860Z'
verified: false
validated: true
submitted: true
---
# RequestBin

**Status**: Unverified

## Overview

RequestBin is a web-based tool for creating temporary endpoints to capture and inspect incoming HTTP requests, commonly used in security testing to validate exploits like redirects or smuggling.

## Description

It provides real-time request logging, useful for debugging and verifying the impact of web vulnerabilities in offensive scenarios.

## Features

- Feature 1: Temporary request bins
- Feature 2: Real-time inspection
- Feature 3: Header and body logging

## Installation

### Requirements

- Web browser

### Install Commands

```bash
# No installation needed, access via web
```

## Basic Usage

```bash
# Visit https://requestbin.com and create a bin
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Web-based interface |

## Examples

### Example 1: Basic Usage

Create a bin and send a test request.

### Example 2: Advanced Usage

Use with specific bin URL like https://requestbin.com/r/enjv2g5042bg for exploit validation.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Traffic to requestbin.com domains
- Detection method 2: Anomalous redirect patterns

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

- Official site: https://requestbin.com
