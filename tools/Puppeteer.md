---
id: tool-puppeteer
url: 'https://pptr.dev/'
tags:
  - automation
  - chrome-control
type: tool
verified: false
platforms:
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.922Z'
validated: true
submitted: true
---
# Puppeteer

**Status**: Unverified

## Overview

Puppeteer is a Node.js library for controlling headless Chrome or Chromium, providing a secure alternative to raw debugging ports by supporting named pipes for local transport.

## Description

Mentioned as a mitigation reference, Puppeteer allows automation of Chrome without exposing websockets, using --remote-debugging-pipe to avoid port scanning vulnerabilities. It's used in security testing for browser automation but highlights secure practices against the Burp exploit.

## Features

- Feature 1: Headless browser control via API
- Feature 2: Support for pipe transport in debugging
- Feature 3: Screenshot and PDF generation

## Installation

### Requirements

- Node.js 14+
- macOS with Chrome

### Install Commands

```bash
npm i puppeteer
```

## Basic Usage

```bash
node script.js
```
(Where script uses puppeteer.launch({pipe: true}))

### Common Options

| Option | Description |
|--------|-------------|
| `--pipe` | Use named pipe for debugging |
| `--executablePath` | Path to Chrome binary |

## Examples

### Example 1: Basic Usage

```javascript
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  // ...
})();
```

### Example 2: Advanced Usage

Secure pipe: puppeteer.launch({ args: ['--remote-debugging-pipe'] })

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process: node with puppeteer
- Files: node_modules/puppeteer

## Related Procedures

- [[procedures/Launch-Burp-Scan-to-Expose-Debugging]]

## Related Tools

- [[tools/Chrome-Browser]]

## References

- GitHub: https://github.com/puppeteer/puppeteer/blob/main/src/node/PipeTransport.ts
- Docs: https://pptr.dev/
