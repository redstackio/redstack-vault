---
id: tool-browser-devtools-001
name: Browser-DevTools
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.267Z'
platforms:
  - Web
tags:
  - debugging
  - testing
url: >-
  https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools
validated: true
submitted: true
---

# Browser-DevTools

**Status**: Unverified

## Overview

Browser Developer Tools (DevTools) are built-in features in modern browsers like Chrome, Firefox, and Edge, used for debugging, inspecting, and manipulating web applications during security testing, such as simulating network responses for XSS validation.

## Description

DevTools provide tabs for Elements (DOM inspection), Console (JS execution), Network (request monitoring), and more. In offensive security, they're essential for overriding responses, injecting payloads, and verifying exploits like DOM-based XSS without full infrastructure changes.

## Features

- Feature 1: Network tab for intercepting and overriding HTTP responses
- Feature 2: Console for running JS commands like fetch uploads
- Feature 3: Elements tab for live DOM editing and script injection testing

## Installation

### Requirements

- Modern web browser (Chrome, Firefox, Edge)

### Install Commands

No installation needed; access via F12 or right-click > Inspect.

## Basic Usage

```bash
# N/A - Browser UI
```

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open DevTools |
| Ctrl+Shift+I | Toggle inspector |
| Network > Disable cache | Prevent caching during tests |

## Examples

### Example 1: Basic Usage

Open DevTools (F12), go to Network tab, check 'Disable cache', reload page to fetch fresh assets.

### Example 2: Advanced Usage

In Sources tab, enable 'Override content', map URL to local malicious file, then load page to simulate injection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser extensions or user-agent anomalies (rare, as it's native)
- Console logs from debugging sessions
- Network traces showing overridden responses

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[Postman]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Related resources: MDN Web Docs
