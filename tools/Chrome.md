---
url: 'https://www.google.com/chrome/'
tags:
  - browser
type: tool
platforms:
  - Windows
  - macOS
  - Linux
description: Web browser for viewing and converting images.
id: 3ae8dc48-22e9-4f57-8289-ebf1da33dfcd
created_at: '2025-12-11T06:10:22.937Z'
updated_at: '2025-12-11T06:10:22.937Z'
verified: false
validated: true
submitted: true
---
# Chrome

**Status**: Unverified

## Overview

Google Chrome browser used to view black PNGs or convert to JPEG for extracting leaked data from screenshots.

## Description

Leverages browser capabilities to render and save images revealing metadata from SSRF attacks.

## Features

- Feature 1: Image rendering
- Feature 2: Developer tools
- Feature 3: File handling

## Installation

### Requirements

- Internet

### Install Commands

Download from website.

## Basic Usage

Open image in browser.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | N/A |

## Examples

### Example 1: Basic Usage

Drag PNG to Chrome tab.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Screen Capture]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser logs
- Network activity

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Firefox]]

## References

- https://www.google.com/chrome/
