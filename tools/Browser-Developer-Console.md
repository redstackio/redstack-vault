---
url: 'https://developer.mozilla.org/en-US/docs/Web/API/Console'
tags:
  - debugging
  - injection
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:17.936Z'
id: 0611d57b-3e0f-4c12-8b50-e9b74558e13a
validated: true
submitted: true
---
# Browser-Developer-Console

**Status**: Unverified

## Overview

The Browser Developer Console is a built-in debugging tool in modern web browsers (Chrome, Firefox, etc.) used for inspecting, debugging, and injecting JavaScript code during security testing, such as CSP bypass demonstrations.

## Description

This tool provides real-time interaction with the Document Object Model (DOM), allowing execution of JavaScript payloads to manipulate page elements, test policies like CSP, and simulate attacks like dynamic resource loading or redirects. It's essential for client-side web vulnerability assessment without external dependencies.

## Features

- Feature 1: JavaScript execution and error logging.
- Feature 2: DOM inspection and manipulation.
- Feature 3: Network request monitoring for policy violations.

## Installation

### Requirements

- Modern web browser (no installation needed; built-in).

### Install Commands

N/A; access via F12 or right-click > Inspect.

## Basic Usage

```javascript
console.log('Test');
```

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open devtools |
| Console tab | Switch to JS execution panel |

## Examples

### Example 1: Basic Usage

Execute simple log:
```javascript
console.log(document.cookie);
```

### Example 2: Advanced Usage

Inject payload for testing:
```javascript
document.createElement('img');
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Client-side logs of console API calls.
- Anomalous JS execution patterns in browser telemetry.

## Related Procedures

- [[procedures/Inject-Dynamic-Image-for-CSP-Bypass]]
- [[procedures/Exfiltrate-Session-via-Open-Redirect]]

## Related Tools

- [[Burp Suite]]
- [[Browser Extensions like Tampermonkey]]

## References

- MDN Web Docs: Console API
