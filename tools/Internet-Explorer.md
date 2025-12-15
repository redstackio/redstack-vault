---
id: tool-003
url: >-
  https://support.microsoft.com/en-us/windows/internet-explorer-11-has-retired-8a7f00ef-1630-40a4-a739-1e4ff6d9b4f7
tags:
  - browser
  - legacy
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.166Z'
validated: true
submitted: true
---
# Internet Explorer

**Status**: Unverified

## Overview

Internet Explorer (IE) is a legacy Microsoft browser used here as the vector for exploiting Kaspersky's Web protection add-on through malicious webpage loading.

## Description

IE's add-on architecture allows Kaspersky's script to run in the page context, vulnerable to JS prototype interception. Version 11 or earlier is targeted, with the add-on injecting protections that call unsafe methods like String.indexOf.

## Features

- Feature 1: Add-on support for AV integrations
- Feature 2: JavaScript execution in document context
- Feature 3: Certificate override for testing invalid HTTPS

## Installation

### Requirements

- Windows 7+ with IE11
- Kaspersky add-on installed

### Install Commands

IE is pre-installed; enable via Windows Features if disabled.

```cmd
# No install needed; launch via iexplore.exe
```

## Basic Usage

```cmd
iexplore.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| -private | Incognito mode |
| url | Direct navigation |

## Examples

### Example 1: Basic Usage

```cmd
iexplore.exe https://www.google.example.com:5000/disable_features2.html
```

Loads exploit page.

### Example 2: Advanced Usage

Override cert warning manually in browser.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Legacy IE processes (iexplore.exe) accessing suspicious URLs
- Add-on script injections logged
- Cert override events in browser history

## Related Procedures

- [[procedures/Load-Malicious-HTML-in-Internet-Explorer]]

## Related Tools

- [[tools/Python-3]]

## References

- Microsoft support: IE retirement notice
