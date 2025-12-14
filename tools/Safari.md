---
url: 'https://www.apple.com/safari/'
tags:
  - browser
  - testing
type: tool
verified: false
platforms:
  - macOS
  - iOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.205Z'
id: 6cc32e25-2155-494e-abeb-eb719de109db
validated: true
submitted: true
---
# Safari

**Status**: Unverified

## Overview

Safari is Apple's default web browser, used here for testing and reproducing web vulnerabilities like reflected XSS by loading malicious URLs.

## Description

Safari supports modern web standards including JavaScript execution, making it suitable for verifying XSS payloads in a real browser environment. In offensive security, it's used to simulate victim interactions on macOS or iOS devices.

## Features

- Feature 1: Built-in developer tools for inspecting HTML and console output.
- Feature 2: Intelligent Tracking Prevention to simulate privacy-focused browsing.
- Feature 3: Seamless integration with macOS for quick URL testing.

## Installation

### Requirements

- macOS or iOS device.

### Install Commands

Pre-installed on Apple devices; update via App Store.

## Basic Usage

```bash
# No CLI; launch via GUI and enter URL in address bar
```

### Common Options

| Option | Description |
|--------|-------------|
| Cmd+Option+I | Open Developer Tools |
| Cmd+R | Reload page |

## Examples

### Example 1: Basic Usage

Launch Safari and navigate to a URL to test XSS.

### Example 2: Advanced Usage

Use Developer Tools: Cmd+Option+I, then reload to observe payload execution.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser user-agent strings in logs identifying Safari.
- No specific detection as it's a standard browser.

## Related Procedures


## Related Tools

- [[tools/Chrome]]
- [[tools/Firefox]]

## References

- Official documentation: https://developer.apple.com/safari/
