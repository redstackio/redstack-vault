---
id: 79e76105-ae56-4233-83bc-27a3782fba54
name: Browser Console
type: tool
verified: false
created_at: '2025-12-11T06:10:40.631Z'
updated_at: '2025-12-11T06:10:40.631Z'
platforms:
  - Web
tags:
  - javascript
  - debugging
url: ''
description: Built-in browser tool for executing JavaScript and modifying page data
validated: true
submitted: true
---

# Browser Console

**Status**: Unverified

## Overview

Browser Console is a developer tool in web browsers for running JavaScript code, inspecting elements, and modifying client-side data.

## Description

Used in security testing to alter form data, execute scripts, and bypass client-side restrictions, such as modifying read-only fields in web forms.

## Features

- Feature 1: JavaScript execution
- Feature 2: DOM manipulation
- Feature 3: Console logging

## Installation

### Requirements

- Modern web browser (Chrome, Firefox, etc.)

### Install Commands

```bash
# Built-in, no installation needed
```

## Basic Usage

```bash
# Open via F12 or Ctrl+Shift+J
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | N/A |

## Examples

### Example 1: Basic Usage

```javascript
console.log('test');
```

### Example 2: Advanced Usage

```javascript
window.RailsData.user.email = 'test';
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Client-side script anomalies
- Detection method 2: Unexpected DOM changes

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
- [[tools/Browser-Dev-Tools]]

## References

- Official documentation
- Related resources
