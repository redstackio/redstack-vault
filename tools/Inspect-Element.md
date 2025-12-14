---
url: 'https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector'
tags:
  - devtools
  - web-testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.321Z'
id: 3faf38dc-1ecc-4b18-a996-52a64893ef05
validated: true
submitted: true
---
# Inspect-Element

**Status**: Unverified

## Overview

Inspect Element is a built-in developer tool in browsers like Firefox, used to examine and modify the DOM, CSS, and JavaScript of web pages in real-time, ideal for testing form manipulations in vulnerability assessments.

## Description

This tool allows security testers to dynamically alter HTML elements, such as form inputs, to inject payloads like empty arrays for triggering server-side errors. In the context of PHP path disclosure, it's used to append '[]' to input values without altering the source code, enabling quick exploitation of input validation flaws.

## Features

- Feature 1: Real-time DOM editing and inspection
- Feature 2: Console for JavaScript execution
- Feature 3: Elements panel for attribute/value changes

## Installation

### Requirements

- Modern web browser (e.g., Firefox)
- No separate installation; enabled via keyboard shortcut

### Install Commands

```bash
# No installation needed; access via F12 in Firefox
firefox --devtools
```

## Basic Usage

```bash
# Launch browser and press F12
firefox https://target.com
# Then F12 to open devtools
```

### Common Options

| Option | Description |
|--------|-------------|
| Elements Tab | Inspect and edit HTML |
| Console Tab | Run JS commands |
| Network Tab | Monitor requests |

## Examples

### Example 1: Basic Usage

Right-click on a form input and select 'Inspect Element' to open the panel.

### Example 2: Advanced Usage

In the Elements tab, locate <input value="test">, edit to <input value="test[]">, then submit the form to trigger error. Use Console to log: console.log(document.querySelector('input').value);

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Server-side logs showing tampered form data (e.g., unexpected [] in inputs)
- Client-side anomalies like modified DOM not matching expected source
- WAF rules flagging unusual parameter appendages

## Related Procedures


## Related Tools

- [[tools/Firefox]]
- [[tools/Chrome-DevTools]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector
- Related resources: OWASP Testing Guide on Client-Side Manipulation
