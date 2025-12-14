---
url: 'https://www.apple.com/safari/'
tags:
  - browser
  - web
  - testing
type: tool
verified: false
platforms:
  - macOS
  - iOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.145Z'
id: 06522524-493c-4a40-84ad-c63c7bbf8789
validated: true
submitted: true
---
# Safari-Browser

**Status**: Unverified

## Overview

Safari is Apple's web browser for macOS and iOS, used here to demonstrate and reproduce the self-XSS vulnerability in Shopify's Timeline by rendering unsanitized javascript: URLs as clickable links.

## Description

Safari's handling of pasted content in web apps like Shopify allows javascript: protocols to execute without blocking, making it ideal for testing client-side vulnerabilities. It supports macOS and iOS environments, with specific reproduction on iOS 13.4.1. In offensive security, it's used for verifying browser-specific XSS behaviors.

## Features

- Feature 1: Native support for WebKit rendering engine, which processes URLs in posts
- Feature 2: Clipboard integration for easy pasting of malicious links
- Feature 3: JavaScript execution in page context without additional extensions

## Installation

### Requirements

- macOS or iOS device
- Apple ID for App Store access (pre-installed on Apple devices)

### Install Commands

Safari is pre-installed; update via System Preferences > Software Update on macOS or App Store on iOS.

```bash
# No installation command needed; use software update
softwareupdate --install --all
```

## Basic Usage

```bash
# Launch Safari (no CLI for basic use; GUI browser)
open -a Safari
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | GUI-based; use Developer Tools (Cmd+Option+I) for inspection |
| N/A | Enable Web Inspector for debugging JS execution |

## Examples

### Example 1: Basic Usage

Open Safari, navigate to Shopify, and paste javascript: URLs into Timeline.

### Example 2: Advanced Usage

Use Safari's Developer Tools to inspect rendered links and confirm JS execution context.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser user-agent strings identifying Safari in logs
- Anomalous JS alerts or executions in web app monitoring

## Related Procedures

- [[procedures/Trigger-Self-XSS-in-Shopify-Timeline]]

## Related Tools

- [[tools/Chrome-Browser]]
- [[tools/Firefox-Browser]]

## References

- Official documentation: https://developer.apple.com/safari/
- Related resources: WebKit security advisories
