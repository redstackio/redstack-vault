---
id: tool-firefox-devtools-001
url: 'https://developer.mozilla.org/en-US/docs/Tools'
tags:
  - browser
  - network
  - debug
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.686Z'
validated: true
submitted: true
---
# Firefox-Developer-Tools

**Status**: Unverified

## Overview

Firefox Developer Tools provide built-in debugging capabilities for web applications, including network monitoring and request editing, useful for API testing and vulnerability exploitation like unauthenticated state changes.

## Description

Integrated into Firefox, these tools allow inspection of HTTP requests via the Network panel, enabling right-click editing and resending for testing endpoints without external proxies. Commonly used in scenarios requiring quick verification of API responses, such as confirming DoS impacts post-payload injection.

## Features

- Feature 1: Network panel for capturing and filtering requests
- Feature 2: Edit and Resend for modifying methods, headers, and bodies
- Feature 3: Console for JavaScript execution and error logging

## Installation

### Requirements

- Firefox browser version 50+

### Install Commands

```bash
# Pre-installed in Firefox; access via F12 or CTRL+SHIFT+I
```

## Basic Usage

```bash
# Open tools
firefox --devtools
```

### Common Options

| Option | Description |
|--------|-------------|
| `CTRL+SHIFT+E` | Open Network tool |
| `F12` | Toggle Developer Tools |

## Examples

### Example 1: Basic Usage

Open Network tab (CTRL+SHIFT+E), reload page to capture requests, right-click a request > Edit and Resend.

### Example 2: Advanced Usage

Modify a captured GET to PUT, add JSON body, and resend to test API.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser logs showing devtools activation
- Modified requests from browser IPs
- Console errors during testing

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor
- Related resources: MDN Web Docs
