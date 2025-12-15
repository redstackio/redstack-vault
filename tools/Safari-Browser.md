---
id: tool-safari-browser
url: 'https://www.apple.com/safari/'
tags:
  - browser
  - trigger
  - user-agent
type: tool
verified: false
platforms:
  - macOS
  - iOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.854Z'
validated: true
submitted: true
---
# Safari-Browser

**Status**: Unverified

## Overview

Safari is Apple's web browser, used here to trigger browser-specific vulnerabilities like the Nextcloud user_oidc XSS due to its unique user agent string that matches the flawed Safari detection logic.

## Description

Safari's user agent (containing /Safari/ but not /Chrome/) activates a workaround in Nextcloud's LoginController.php, leading to unescaped HTML insertion. In security testing, it's essential for reproducing client-side flaws, inspecting payloads via developer tools, and observing CSP interactions. No special config needed beyond default settings.

## Features

- Feature 1: Built-in Web Inspector for debugging JS and HTML
- Feature 2: Strict adherence to web standards, exposing UA-specific bugs
- Feature 3: Integration with macOS for seamless local testing

## Installation

### Requirements

- macOS or iOS device

### Install Commands

```bash
# Pre-installed on macOS; update via Software Update
softwareupdate --install --all
```

## Basic Usage

```bash
# Launch from terminal
/Applications/Safari.app/Contents/MacOS/Safari
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | GUI-based; use Cmd+Option+I for inspector |

## Examples

### Example 1: Basic Usage

Navigate to http://localhost:8081/login in Safari to trigger the flow.

### Example 2: Advanced Usage

Use Web Inspector: Right-click > Inspect Element to view injected HTML.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Server logs showing Safari UA strings (/Safari/)
- Detection method 2: Browser fingerprinting via JavaScript to identify Safari

## Related Procedures

- [[procedures/Trigger-Stored-XSS-via-Safari-Login]]

## Related Tools

- [[Related Tool 1|Chrome]]
- [[Related Tool 2|Firefox]]

## References

- Official documentation: https://developer.apple.com/safari/
- Related resources: User agent strings reference
