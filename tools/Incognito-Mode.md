---
url: null
tags:
  - web
  - privacy
type: tool
platforms:
  - Web
description: Browser mode for unauthenticated access without session cookies
id: de4bea96-60b9-4156-a255-67cf87f5a137
created_at: '2025-12-13T09:00:34.380Z'
updated_at: '2025-12-13T09:00:34.380Z'
verified: false
validated: true
submitted: true
---
# Incognito Mode

**Status**: Unverified

## Overview

Incognito or private browsing mode used to access URLs without existing session cookies, simulating an unauthenticated user in security tests.

## Description

This feature allows testing of cached content accessibility without logged-in sessions, crucial for verifying disclosures in cache poisoning attacks.

## Features

- No cookie persistence
- Isolated browsing session

## Installation

### Requirements

- Web browser supporting incognito

### Install Commands

Built-in feature.

## Basic Usage

Open a new incognito window and navigate to URL.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | N/A |

## Examples

### Example 1: Basic Usage

Open incognito and visit https://www.lyst.com/LAVFKS53DG.css

### Example 2: Advanced Usage

Combine with source view.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Difficult to detect as it's client-side

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Web-Browser]]

## References

- Browser privacy mode guides
