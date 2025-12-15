---
id: tool-uuid-1
url: >-
  https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools
tags:
  - debugging
  - manipulation
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.234Z'
validated: true
submitted: true
---
# Browser-Developer-Tools

**Status**: Unverified

## Overview

Browser Developer Tools are built-in features in modern web browsers (Chrome, Firefox, Edge) used for inspecting, debugging, and manipulating web pages, commonly in security testing to bypass client-side controls like disabled forms.

## Description

These tools provide consoles for JavaScript execution, network inspection for request interception, and element editing for DOM manipulation. In offensive security, they enable quick tests for client-side vulnerabilities, such as enabling hidden or disabled UI elements, without external software. Key use cases: Form bypasses, cookie extraction, and JavaScript injection.

## Features

- Feature 1: Elements panel for HTML/CSS editing (e.g., remove 'disabled' attributes)
- Feature 2: Network tab for capturing HTTP requests/cookies
- Feature 3: Console for running JavaScript to automate changes

## Installation

### Requirements

- Modern web browser (Chrome 50+, Firefox 50+, etc.)

### Install Commands

No installation needed; access via F12 or right-click > Inspect.

## Basic Usage

```bash
# No CLI; browser-based
# Open: Press F12 or Ctrl+Shift+I
```

### Common Options

| Option | Description |
|--------|-------------|
| Elements Tab | Edit DOM in real-time |
| Network Tab | Intercept and replay requests |
| Console | Execute JS commands |

## Examples

### Example 1: Basic Usage

Open dev tools (F12), go to Elements, find <input disabled>, right-click > Edit as HTML, remove 'disabled'.

### Example 2: Advanced Usage

In Console: document.querySelector('#loginButton').removeAttribute('disabled');

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for rapid DOM changes via client-side logging
- Detect unusual JS execution patterns in web logs
- Use CSP to restrict dev tools access (limited effectiveness)

## Related Procedures

- [[procedures/Bypass-milConnect-Login-Form-Restrictions]]
- [[procedures/Intercept-myPay-Session-Cookies]]

## Related Tools

- [[Burp Suite]]
- [[Postman]]

## References

- Official documentation: MDN Web Docs
- Related resources: OWASP Testing Guide
