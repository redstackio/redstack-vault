---
url: 'https://developer.mozilla.org/en-US/docs/Tools'
tags:
  - devtools
  - dom-inspection
  - web
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:23.432Z'
id: 8822cd06-10b5-40d7-b6a0-35d7c3f764df
validated: true
submitted: true
---
# Mozilla-Firefox-Developer-Tools

**Status**: Unverified

## Overview

Mozilla Firefox Developer Tools (Inspect Element) is a built-in suite for debugging, inspecting, and modifying web page elements, commonly used in security testing to demonstrate client-side vulnerabilities like DOM manipulation for open redirects.

## Description

The tools include the Inspector for viewing and editing HTML/CSS, Console for JavaScript execution, and Network panel for traffic analysis. In offensive operations, attackers use it to tamper with form attributes on sites like Coinbase sign-in pages to alter redirects, enabling phishing without server interaction.

## Features

- Feature 1: Real-time DOM editing and attribute modification
- Feature 2: Element selection and highlighting on the page
- Feature 3: Persistence of changes within the browser session

## Installation

### Requirements

- Mozilla Firefox browser installed

### Install Commands

```bash
# No separate installation; access via F12 or right-click > Inspect Element
firefox --devtools
```

## Basic Usage

Press F12 or right-click and select "Inspect Element".

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open Developer Tools |
| Ctrl+Shift+I | Toggle Inspector |
| Ctrl+Shift+C | Inspect Element tool |

## Examples

### Example 1: Basic Usage

Right-click on a page element and select "Inspect Element" to open the panel and view DOM.

### Example 2: Advanced Usage

Select an element, edit its 'action' attribute in the inspector, and observe the page update.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Client-side script monitoring for dev tools activation
- CSP violations or anomalous DOM changes
- Browser forensics showing inspector usage in session history

## Related Procedures


## Related Tools

- [[tools/Chrome-DevTools]]
- [[tools/Safari-Web-Inspector]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector
- Related resources: Firefox Developer Edition notes
