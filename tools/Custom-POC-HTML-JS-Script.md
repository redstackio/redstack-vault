---
url: null
tags:
  - poc
  - javascript
  - automation
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.485Z'
id: 854e1fb5-7e13-4c0c-a358-ccbf6f1d1bbb
validated: true
submitted: true
---
# Custom-POC-HTML-JS-Script

**Status**: Unverified

## Overview

A browser-based HTML/JavaScript proof-of-concept for automating web cache poisoning by generating random .css URLs, opening them in popups to trigger caching while authenticated, and logging URLs for later retrieval.

## Description

This custom tool targets vulnerabilities like the Lyst.com cache poisoning issue. It runs entirely client-side in a browser, using JavaScript to create random endpoints and simulate requests via popups. Ideal for offensive security testing of cache keying flaws, enabling scalable poisoning without external dependencies.

## Features

- Feature 1: Random 10-character ID generation from alphanumeric charset 'QWERTZUIOPASDFGHJUKLYXCVBNM1234567890'
- Feature 2: Dynamic URL construction (e.g., `https://www.lyst.com/[random].css`)
- Feature 3: Popup-based request triggering with auto-closure after 3 seconds and 200ms status checks

## Installation

### Requirements

- Modern web browser (e.g., Chrome, Firefox)
- Authenticated session to target site

### Install Commands

No installation required; save as .html file and open in browser.

```html
<!DOCTYPE html>
<html>
<body>
<script>
// PoC code here
</script>
</body>
</html>
```

## Basic Usage

Open the HTML file in a browser while logged into the target site. Execute the script to generate and poison a URL.

### Common Options

| Option | Description |
|--------|-------------|
| Charset | Customizable alphanumeric string for ID generation |
| Interval | 200ms for popup status checks |
| Timeout | 3000ms delay before closing popup |

## Examples

### Example 1: Basic Usage

Load HTML and run: Generates ID, opens `https://www.lyst.com/[ID].css` in popup, caches, closes, alerts URL.

### Example 2: Advanced Usage

Modify charset or timeouts in script for different targets; loop for multiple poisonings.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for rapid popup openings to random .css endpoints from authenticated sessions
- Detection method 2: Log client-side JS executions generating unusual URLs

## Related Procedures


## Related Tools


## References

- HackerOne Report #631589
