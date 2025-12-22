---
id: tool-uuid-002
url: null
tags:
  - debugging
  - execution
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.073Z'
validated: true
submitted: true
---
# Browser-Console

**Status**: Unverified

## Overview

Built-in browser developer tool for executing JS and inspecting page behavior, ideal for real-time timing logs in attacks.

## Description

Accessed via F12 or right-click inspect, allows running commands like performance queries to capture and log data during webpage loads.

## Features

- Feature 1: JS execution
- Feature 2: Log inspection
- Feature 3: Resource monitoring

## Installation

### Requirements

- Any modern browser

### Install Commands

N/A

## Basic Usage

```javascript
console.log('test');
```

### Common Options

| Option | Description |
|--------|-------------|
| console.log | Output to console |

## Examples

### Example 1: Basic Usage

Open console and run function.

### Example 2: Advanced Usage

performance.getEntriesByType('resource')

## MITRE ATT&CK Mapping

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

- CSP to restrict console access
- Monitor for dev tools usage

## Related Procedures


## Related Tools

- [[tools/Resource-Timing-API]]

## References

- Browser dev docs
