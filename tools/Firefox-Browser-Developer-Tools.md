---
id: tool-001-firefox-devtools
url: 'https://developer.mozilla.org/en-US/docs/Tools'
tags:
  - web-debugging
  - request-interception
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.261Z'
validated: true
submitted: true
---
# Firefox-Browser-Developer-Tools

**Status**: Unverified

## Overview

Firefox Developer Tools is a built-in suite in the Firefox browser for inspecting, debugging, and modifying web applications, commonly used in security testing for intercepting and tampering with HTTP requests during vulnerability exploitation like auth bypasses.

## Description

The tools include the Network panel for capturing requests, Inspector for DOM manipulation, and Console for scripting. In offensive security, it's used to proxy and edit form submissions, such as modifying parameters in POST requests to endpoints like api.data.gov's user creation API. No installation is needed beyond Firefox; it's ideal for quick, low-overhead testing without external proxies.

## Features

- Feature 1: Network monitoring and request pausing/editing for tampering
- Feature 2: Header and body inspection with real-time modification
- Feature 3: Integration with Firefox for seamless browser-based attacks

## Installation

### Requirements

- Firefox browser version 55.0 or later

### Install Commands

No additional installation; enable via Firefox menu: Tools > Web Developer > Toggle Tools.

## Basic Usage

```bash
# Launch Firefox and open dev tools with Ctrl+Shift+I (Linux/Windows) or Cmd+Opt+I (macOS)
firefox https://api.data.gov/signup/
```

### Common Options

| Option | Description |
|--------|-------------|
| Network Tab | Capture and edit HTTP requests |
| Persist Logs | Retain request history across page loads |

## Examples

### Example 1: Basic Usage

Open dev tools, navigate to Network tab, load signup page, submit form, and pause on POST to edit.

### Example 2: Advanced Usage

```bash
# In console, inject script to auto-modify requests (for automation)
document.addEventListener('submit', function(e) { /* modify form data */ });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript (for console scripting)

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual browser user-agent strings in logs
- Frequent request pauses or edits in proxy traces
- Console errors from dev tools on production sites

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/Chrome-Developer-Tools]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Tools
- Related resources: Mozilla Developer Network guides on Network panel
