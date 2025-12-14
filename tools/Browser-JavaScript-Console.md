---
url: ''
tags:
  - web-testing
  - javascript
type: tool
platforms:
  - Web
description: >-
  Built-in browser developer tool for executing JavaScript to test web
  vulnerabilities like CORS and cache poisoning.
id: 0ce46934-b747-4c26-a353-0700a24ed8a2
created_at: '2025-12-14T17:32:48.569Z'
updated_at: '2025-12-14T17:32:48.569Z'
verified: false
validated: true
submitted: true
---
# Browser-JavaScript-Console

**Status**: Unverified

## Overview

The Browser JavaScript Console is a developer tool in modern browsers (Chrome, Firefox, etc.) for running ad-hoc JavaScript code, inspecting network requests, and debugging web applications. In security testing, it's used to simulate cross-origin requests and observe behaviors like CORS enforcement or cache responses.

## Description

Accessed via F12 or right-click > Inspect > Console tab, it allows direct execution of Fetch API calls or other JS to interact with remote endpoints. Essential for client-side vulnerability testing without external tools, particularly for CORS misconfigurations and cache poisoning in APIs like WP-JSON.

## Features

- Feature 1: Real-time code execution and error logging
- Feature 2: Network tab integration for header inspection (e.g., ACAO, X-Cache)
- Feature 3: Cross-origin request simulation with automatic Origin headers

## Installation

### Requirements

- Modern web browser (Chrome 50+, Firefox 50+, etc.)

### Install Commands

No installation needed; built-in.

## Basic Usage

```javascript
// Open console and run
console.log('Test');
```

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open DevTools |
| Ctrl+Shift+J (Chrome) | Direct console access |
| Network tab | Inspect requests/responses |

## Examples

### Example 1: Basic Usage

```javascript
fetch('https://example.com/api').then(r => r.text()).then(t => console.log(t));
```

### Example 2: Advanced Usage

```javascript
fetch('https://target.com/wp-json/', {headers: {'Origin': 'https://attacker.com'}}).then(r => console.log(r.headers));
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual cross-origin requests from browser sessions
- Console logs in error reports

## Related Procedures

- [[procedures/Poison-WP-JSON-Cache-with-Arbitrary-Origin]]

## Related Tools

- [[tools/Fetch-API]]

## References

- MDN Web Docs: Console API
