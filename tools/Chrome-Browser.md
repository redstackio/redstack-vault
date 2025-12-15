---
id: tool-chrome-browser
url: 'https://www.google.com/chrome/'
tags:
  - browser
  - javascript
type: tool
verified: false
platforms:
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.928Z'
validated: true
submitted: true
---
# Chrome-Browser

**Status**: Unverified

## Overview

Google Chrome is a web browser that supports JavaScript execution and remote debugging protocols, used here for navigating to the exploit and interacting with clickjacking payloads.

## Description

In the attack, a standard Chrome instance loads the exploit page, enabling JS to scan ports and exploit the debugging websocket. Known XSS vulnerabilities in the debugging protocol (since 2016) are leveraged when remote debugging is enabled. Chrome's headless mode is used by Burp, but full browser simulates user interaction.

## Features

- Feature 1: JavaScript engine (V8) for client-side execution
- Feature 2: DevTools protocol for remote debugging via websocket
- Feature 3: Support for clickjacking via iframes

## Installation

### Requirements

- macOS 10.13+

### Install Commands

```bash
# Download from official site
open /Applications/Google\ Chrome.app
```

## Basic Usage

```bash
# Launch Chrome
open -a "Google Chrome" http://127.0.0.1:8000/burp.html
```

### Common Options

| Option | Description |
|--------|-------------|
| `--headless` | Run without UI (used by Burp) |
| `--remote-debugging-port=9222` | Enable websocket debugging |

## Examples

### Example 1: Basic Usage

Navigate to a URL manually or via command line.

### Example 2: Advanced Usage

```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript
- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process: Google Chrome with --remote-debugging-port flag
- Network: Local ws:// connections
- Logs: Chrome debug protocol traffic

## Related Procedures

- [[procedures/Navigate-to-Exploit-in-Browser]]
- [[procedures/Scan-for-Debugging-Port-and-Clickjack]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Chromium bugs: Search for remote debugging XSS
