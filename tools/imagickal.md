---
id: tool-uuid-3
url: 'https://www.npmjs.com/package/imagickal'
tags:
  - vulnerable
  - imagemagick-wrapper
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.099Z'
configuration: Version 4.2.0
validated: true
submitted: true
---
# imagickal

**Status**: Unverified

## Overview

imagickal is a Node.js module wrapping ImageMagick commands for image processing, vulnerable to command injection in version 4.2.0 due to unsanitized inputs.

## Description

This tool allows Node.js applications to execute ImageMagick binaries like 'identify' for metadata extraction. The vulnerability enables RCE by injecting shell commands into filenames, useful in demonstrating supply chain attacks via npm packages.

## Features

- Feature 1: Wrapper for ImageMagick CLI tools (identify, convert)
- Feature 2: Asynchronous command execution
- Feature 3: Input parameter passing to binaries

## Installation

### Requirements

- Node.js and npm
- ImageMagick installed on host

### Install Commands

```bash
npm i imagickal@4.2.0
```

## Basic Usage

```bash
node -e "require('imagickal').identify('image.jpg')"
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Direct function calls like im.identify(filename) |

## Examples

### Example 1: Basic Usage

```javascript
const im = require('imagickal'); im.identify('image.jpg');
```

### Example 2: Advanced Usage (Vulnerable)

```javascript
im.identify('image.jpg; touch HACKED;');
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Audit npm dependencies for imagickal@4.2.0
- Monitor ImageMagick invocations from Node.js with injected commands

## Related Procedures

- [[procedures/Install-Vulnerable-imagickal-Module]]

## Related Tools

- [[tools/ImageMagick]]

## References

- npm page: https://www.npmjs.com/package/imagickal
- HackerOne report: https://hackerone.com/reports/973245
