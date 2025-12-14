---
url: 'https://developer.mozilla.org/en-US/docs/Web/API/Console'
tags:
  - browser
  - devtools
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:25.793Z'
id: a354adc2-9dfe-4045-a969-ce7b0552983b
validated: true
submitted: true
---
# Web-Inspector

**Status**: Unverified

## Overview

Web Inspector (browser developer tools) enables interactive JavaScript execution and inspection of web applications, ideal for testing Meteor.js methods in Rocket.Chat.

## Description

Built into browsers like Chrome (DevTools) and Firefox (Inspector), it provides a console for running code, network monitoring, and DOM inspection. In offensive security, it's used for client-side exploit testing, such as injecting into Meteor calls without external tools.

## Features

- Feature 1: Console for JS execution and error logging.
- Feature 2: Network tab to monitor requests/responses.
- Feature 3: Sources tab for debugging scripts.

## Installation

### Requirements

- Modern web browser (Chrome, Firefox, Safari, Edge).

### Install Commands

No installation; built-in. Access via F12 or right-click > Inspect.

## Basic Usage

```javascript
// In console
console.log('Test');
```

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open inspector |
| Ctrl+Shift+I | Toggle dev tools |

## Examples

### Example 1: Basic Usage

Open console and run `Meteor.call('method', 'arg');`.

### Example 2: Advanced Usage

Monitor network: Load page, filter by XHR to see Meteor requests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser user-agent anomalies.
- Console API calls in logs.

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[Postman]]

## References

- MDN Web Docs: Console API
