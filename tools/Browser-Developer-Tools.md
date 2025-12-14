---
id: tool-browser-dev-tools
url: >-
  https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools
tags:
  - browser
  - devtools
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.427Z'
validated: true
submitted: true
---
# Browser-Developer-Tools

**Status**: Unverified

## Overview

Browser Developer Tools are built-in features in modern web browsers (e.g., Chrome, Firefox) used for inspecting, debugging, and modifying web page elements, commonly in security testing to bypass client-side controls.

## Description

These tools allow real-time DOM manipulation, network inspection, and console execution, essential for web vulnerability exploitation like SSRF via HTML edits. In offensive security, they facilitate client-side bypasses without external software.

## Features

- Feature 1: DOM inspector for editing HTML attributes
- Feature 2: Network tab for monitoring requests
- Feature 3: Console for JavaScript execution

## Installation

### Requirements

- Modern web browser (Chrome 12+, Firefox 52+, etc.)

### Install Commands

No installation needed; enable via F12 key or menu.

## Basic Usage

Press F12 to open tools.

### Common Options

| Option | Description |
|--------|-------------|
| Elements Tab | Inspect and edit HTML/CSS |
| Console | Run JavaScript |
| Network | View requests |

## Examples

### Example 1: Basic Usage

Open DevTools and inspect an element.

### Example 2: Advanced Usage

Edit an input's type: In Elements, double-click type="file" and change to type="url".

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser extensions or user-agent anomalies
- Unusual DOM changes in client-side logs

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[Postman]]

## References

- Official documentation: MDN Web Docs
- Related resources: OWASP Testing Guide
