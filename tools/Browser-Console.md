---
url: ''
tags:
  - debugging
  - xss
type: tool
platforms:
  - Web
description: Built-in developer tool for executing JavaScript and inspecting web pages.
id: b047e900-3bac-49f2-9024-8595ec9d170d
created_at: '2025-12-13T23:56:20.408Z'
updated_at: '2025-12-13T23:56:20.408Z'
verified: false
validated: true
submitted: true
---
# Browser Console

**Status**: Unverified

## Overview

The browser console is a developer tool integrated into web browsers for running JavaScript, inspecting DOM, and testing exploits like XSS.

## Description

It allows direct manipulation of page content, execution of scripts, and verification of vulnerabilities in real-time on live sites.

## Features

- JavaScript execution
- DOM inspection
- Network monitoring

## Installation

### Requirements

- Modern web browser (Chrome, Firefox, etc.)

### Install Commands

No installation needed; access via F12 or right-click > Inspect.

## Basic Usage

```javascript
console.log('test');
```

### Common Options

| Option | Description |
|--------|-------------|
| `console.log` | Output messages |
| `document` | DOM manipulation |

## Examples

### Example 1: Basic Usage

```javascript
alert('test');
```

### Example 2: Advanced Usage

```javascript
document.write(document.body.innerHTML.replace(/\\\\//g,'/'));
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual console activity in logs
- Script executions on sensitive domains

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Internet-Explorer]]

## References

- Browser developer documentation
