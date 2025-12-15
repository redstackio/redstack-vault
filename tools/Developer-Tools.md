---
id: tool-003
url: 'https://developer.chrome.com/docs/devtools/'
tags:
  - debugging
  - console
  - chromium
type: tool
verified: false
platforms:
  - Desktop
  - Browser
  - Electron
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:29.123Z'
validated: true
submitted: true
---
# Developer-Tools

**Status**: Unverified

## Overview

Developer Tools (DevTools) is the built-in debugging console in Chromium-based environments like Electron and Chrome. It allows inspection, JavaScript execution, and network monitoring, commonly used in security testing to inject code and exploit renderer vulnerabilities.

## Description

DevTools provides tabs for Console (JS execution), Elements (DOM inspection), and Sources (script debugging). In Electron, it's enabled by default in development mode, enabling attackers to run API calls like navigator.bluetooth.requestDevice directly in the renderer context.

## Features

- Feature 1: Console for live JavaScript evaluation
- Feature 2: Network tab for API request tracing
- Feature 3: Application tab for storage and permissions inspection

## Installation

### Requirements

- Chromium-based app (e.g., Electron, Chrome)

### Install Commands

No installation needed; built-in.

## Basic Usage

```javascript
// Open with Ctrl+Shift+I, then type in Console
console.log('Test');
```

### Common Options

| Option | Description |
|--------|-------------|
| Ctrl+Shift+I | Open DevTools
| F12 | Alternative open shortcut

## Examples

### Example 1: Basic Usage

Open Console and run: ```javascript
navigator.userAgent
```

### Example 2: Advanced Usage

Execute async API: ```javascript
await navigator.bluetooth.requestDevice({acceptAllDevices: true})
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- UI focus on DevTools window
- Console logs showing injected scripts
- Process memory spikes from debugging

## Related Procedures


## Related Tools

- [[tools/Chromium]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Related resources: Electron DevTools integration
