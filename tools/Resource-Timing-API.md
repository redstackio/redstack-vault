---
id: tool-uuid-001
url: 'https://developer.mozilla.org/en-US/docs/Web/API/Resource_Timing_API'
tags:
  - browser-api
  - performance
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.076Z'
validated: true
submitted: true
---
# Resource-Timing-API

**Status**: Unverified

## Overview

Browser API for measuring resource load performance, used in side-channel attacks to infer data from timing variations.

## Description

Part of Web Performance API, provides high-resolution timings for fetched resources like images or scripts, enabling precise measurement of server response times cross-origin.

## Features

- Feature 1: getEntriesByType('resource') for resource list
- Feature 2: responseEnd - responseStart for duration
- Feature 3: Supports modern browsers (Chrome 43+, Firefox 39+)

## Installation

### Requirements

- Modern browser

### Install Commands

No install; native JS API.

## Basic Usage

```javascript
performance.getEntriesByType('resource');
```

### Common Options

| Option | Description |
|--------|-------------|
| getEntriesByType | Filter by type |

## Examples

### Example 1: Basic Usage

```javascript
var res = performance.getEntriesByType('resource'); console.log(res[0].responseEnd - res[0].responseStart);
```

### Example 2: Advanced Usage

Loop over entries to average.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor JS execution in dev tools
- Block performance API in strict CSP

## Related Procedures


## Related Tools

- [[tools/Browser-Console]]

## References

- MDN Documentation
