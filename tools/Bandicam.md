---
url: null
tags:
  - screen-recording
type: tool
platforms:
  - Windows
description: Screen recording software for demonstrating vulnerabilities
id: 14479ce7-b3e7-425a-ab23-cc542c912c8c
created_at: '2025-12-11T06:10:15.986Z'
updated_at: '2025-12-11T06:10:15.986Z'
verified: false
validated: true
submitted: true
---
# Bandicam

**Status**: Unverified

## Overview

Bandicam is a screen recording tool used to capture video demonstrations of vulnerabilities, such as CRLF injection PoCs, for reporting purposes.

## Description

It allows high-quality recording of screen activity, useful in security testing to provide visual evidence of exploits without sharing sensitive data.

## Features

- Screen capture: Record specific areas
- Video export: Save in various formats
- Overlay: Add annotations

## Installation

### Requirements

- Windows OS
- Sufficient storage

### Install Commands

```bash
# Download from official website and install
```

## Basic Usage

```bash
# Launch Bandicam and start recording
```

### Common Options

| Option | Description |
|--------|-------------|
| Record button | Start/stop recording |
| Settings | Configure quality |

## Examples

### Example 1: Basic Usage

Record browser accessing vulnerable URL.

### Example 2: Advanced Usage

Record with annotations highlighting injected headers.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- None directly; supportive tool

### Tactics

- None directly

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of recording software in environment
- Video files in reports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Browser]]

## References

- Bandicam official site
