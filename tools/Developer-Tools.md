---
url: null
tags:
  - debugging
  - testing
type: tool
platforms:
  - Desktop
  - Electron
description: Browser developer tools for testing payloads
id: 678e32cd-600b-4c08-957c-538b0e2009eb
created_at: '2025-12-11T06:10:22.466Z'
updated_at: '2025-12-11T06:10:22.466Z'
verified: false
validated: true
submitted: true
---
# Developer Tools

**Status**: Unverified

## Overview

Built-in developer tools in browsers or Electron apps for testing RCE payloads in console.

## Description

Allows executing and debugging JavaScript in the context of the Slack app to verify overwrites and leaks.

## Features

- Console execution: Run JS snippets.
- Debugging: Inspect objects.
- Network monitoring: View requests.

## Installation

### Requirements

- Slack desktop app or browser.

### Install Commands

```bash
# Built-in, no install needed
```

## Basic Usage

```bash
# Open via Ctrl+Shift+I
```

### Common Options

N/A

## Examples

### Example 1: Basic Usage

```javascript
console.log('test')
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Console access logs if monitored.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/HTTPS-Enabled-Server]]

## References

- Chrome DevTools docs
