---
url: 'https://www.npmjs.com/package/webpack-bundle-analyzer'
tags:
  - visualizer
  - xss-vulnerable
type: tool
verified: false
platforms:
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:36.900Z'
configuration: Version 3.0.3 (vulnerable); fixed in 3.3.2
id: 2d9018ed-d6d6-45de-8518-03446e867a66
validated: true
submitted: true
---
# webpack-bundle-analyzer

**Status**: Unverified

## Overview

Webpack Bundle Analyzer visualizes bundle sizes via an interactive treemap in a local web interface, vulnerable to XSS in version 3.0.3 due to unsanitized EJS rendering.

## Description

The tool parses webpack stats JSON and serves a viewer at localhost:8888 using EJS templates. Malicious names inject script tags, executing JS on load. Used in security testing to demonstrate client-side execution risks.

## Features

- Feature 1: Treemap visualization of modules
- Feature 2: Local HTTP server for interface
- Feature 3: Stats JSON parsing

## Installation

### Requirements

- Node.js

### Install Commands

```bash
npm i webpack-bundle-analyzer
```

## Basic Usage

```bash
npx webpack-bundle-analyzer stats.json
```

### Common Options

| Option | Description |
|--------|-------------|
| `--port` | Server port (default 8888) |
| `--open` | Auto-open browser |

## Examples

### Example 1: Basic Usage

```bash
npx webpack-bundle-analyzer poc.json
```

### Example 2: Advanced Usage

```bash
npx webpack-bundle-analyzer --port 8889 stats.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process listening on port 8888
- viewer.ejs files in node_modules

## Related Procedures

- [[procedures/Run-Analyzer-on-Malicious-JSON]]
- [[procedures/Access-Web-Interface-to-Trigger-XSS]]

## Related Tools

- [[tools/webpack]]

## References

- Official documentation: https://www.npmjs.com/package/webpack-bundle-analyzer
- Vulnerability report: https://hackerone.com/reports/463380
