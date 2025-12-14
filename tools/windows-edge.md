---
url: 'https://www.npmjs.com/package/windows-edge'
tags:
  - vulnerable-module
  - rce
type: tool
platforms:
  - Windows
description: >-
  Node.js module for launching Microsoft Edge tabs on Windows, vulnerable to
  RCE.
id: e853e2c2-634b-42fd-bfdd-c482e59825d3
created_at: '2025-12-14T17:23:20.007Z'
updated_at: '2025-12-14T17:23:20.007Z'
verified: false
validated: true
submitted: true
---
# windows-edge

**Status**: Unverified

## Overview

A Node.js module designed to open Microsoft Edge tabs, but version 1.0.1 contains a command injection vulnerability exploitable via URI parameter.

## Description

The module formats URI input directly into shell commands without sanitization, allowing RCE on Windows hosts during security assessments.

## Features

- Feature 1: Launch Edge with specified URI
- Feature 2: Callback for process handling
- Feature 3: Windows-specific integration

## Installation

### Requirements

- Node.js on Windows

### Install Commands

```bash
npm i windows-edge@1.0.1
```

## Basic Usage

```bash
# In JS: require('windows-edge').edge({uri: 'url'}, callback);
```

### Common Options

| Option | Description |
|--------|-------------|
| `uri` | URL to open (vulnerable to injection) |

## Examples

### Example 1: Basic Usage

```javascript
const edge = require('windows-edge');
edge({uri:'https://example.com'}, (err, ps)=>{});
```

### Example 2: Advanced Usage (Exploitation)

```javascript
edge({uri:'https://github.com/; touch HACKED; #'}, (err, ps)=>{});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of node_modules/windows-edge
- Shell executions from edge.exe

## Related Procedures


## Related Tools

- [[tools/Node.js]]

## References

- HackerOne Report: https://hackerone.com/reports/878420
