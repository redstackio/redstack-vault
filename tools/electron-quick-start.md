---
id: tool-002
url: 'https://github.com/electron/electron-quick-start'
tags:
  - sample-app
  - electron
  - testing
type: tool
verified: false
platforms:
  - Desktop
  - Windows
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:29.136Z'
validated: true
submitted: true
---
# electron-quick-start

**Status**: Unverified

## Overview

electron-quick-start is a GitHub repository providing a minimal template for Electron applications. It serves as a starting point for security researchers to test vulnerabilities in renderer processes, such as improper access to system APIs like Bluetooth.

## Description

The repo includes a basic main.js for the Electron main process, index.html for the renderer, and package.json for dependencies. When run with vulnerable Electron versions, it exposes the Web Bluetooth API without protections, ideal for reproducing access control issues.

## Features

- Feature 1: Simple renderer HTML/JS setup
- Feature 2: Basic main process for app lifecycle
- Feature 3: Easy customization for vulnerability testing

## Installation

### Requirements

- Git
- Node.js

### Install Commands

```bash
git clone https://github.com/electron/electron-quick-start
cd electron-quick-start
npm install
```

## Basic Usage

```bash
npm start
```

### Common Options

| Option | Description |
|--------|-------------|
| npm run build | Package the app

## Examples

### Example 1: Basic Usage

```bash
npm start
```

### Example 2: Advanced Usage

```bash
npm install electron@^16.0.5 --save-dev && npm start
```

> Pins a vulnerable version.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Git clone logs for the repository
- Running processes matching quick-start patterns
- File system artifacts in temp directories

## Related Procedures


## Related Tools

- [[tools/Electron]]

## References

- Official documentation: https://github.com/electron/electron-quick-start
