---
id: tool-web-inspector-001
name: Browser-Web-Inspector
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.238Z'
platforms:
  - Web
tags:
  - developer-tools
  - inspection
  - javascript
url: >-
  https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools
validated: true
submitted: true
---

# Browser-Web-Inspector

**Status**: Unverified

## Overview

Browser Web Inspector (also known as Developer Tools) is a built-in suite in modern web browsers for inspecting, debugging, and manipulating web pages. In security testing, it's used for discovering vulnerabilities like CSS injection by executing JavaScript in the console and inspecting network traffic.

## Description

Available in browsers like Chrome (DevTools), Firefox (Inspector), and Safari (Web Inspector), this tool provides tabs for Elements (DOM inspection), Console (JS execution), Network (API monitoring), and more. For offensive security, it's essential for client-side exploitation, such as crafting Meteor.call payloads in Rocket.Chat to inject CSS. No installation required; it's native to the browser.

## Features

- Feature 1: Console for real-time JavaScript execution and error logging
- Feature 2: Network tab to capture and analyze HTTP/WebSocket requests
- Feature 3: Elements tab for DOM manipulation and style inspection

## Installation

### Requirements

- Modern web browser (Chrome 12+, Firefox 52+, Safari 6+)
- No additional software needed

### Install Commands

```bash
# No installation; access via F12 or right-click > Inspect
```

## Basic Usage

```bash
# Open in Chrome: Press F12 or Ctrl+Shift+I
```

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open Developer Tools |
| Ctrl+Shift+C | Inspect element under cursor |
| Console tab | Execute JS commands |

## Examples

### Example 1: Basic Usage

Open inspector and type in console:

```javascript
console.log('Test');
```

### Example 2: Advanced Usage

Monitor network for Rocket.Chat API:

Switch to Network tab, filter 'WS' for WebSocket, and inspect 'rid' in payloads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript
- [[Account Discovery]] Account Discovery

### Tactics

- [[Discovery]] Discovery
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Browser process anomalies (e.g., devtools.exe in task manager)
- Client-side logs showing console executions if instrumented
- Network behavior indicating manual inspection (e.g., prolonged sessions)

## Related Procedures

- [[procedures/Exploit-CSS-Injection-in-Rocket-Chat-Avatars]]
- [[procedures/Identify-Rocket-Chat-Room-ID]]

## Related Tools

- [[Burp Suite]]
- [[Postman]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Related resources: MDN Web Docs on DevTools
