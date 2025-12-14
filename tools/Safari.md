---
id: uuid-7
url: 'https://www.apple.com/safari/'
tags:
  - browser
  - safari
type: tool
verified: false
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.324Z'
validated: true
submitted: true
---
# Safari

**Status**: Unverified

## Overview

Safari is Apple's web browser for macOS and iOS, used here to trigger browser-specific vulnerabilities like the Nextcloud user_oidc XSS due to user agent detection and meta refresh handling.

## Description

In security testing, Safari is essential for reproducing browser-conditional exploits. Its unique user agent string causes Nextcloud to apply a vulnerable workaround, injecting unencoded payloads into HTML.

## Features

- Feature 1: Strict adherence to web standards
- Feature 2: Built-in developer tools for inspection
- Feature 3: User agent that triggers app-specific logic

## Installation

### Requirements

- macOS device

### Install Commands

Pre-installed on macOS; update via App Store.

## Basic Usage

```bash
open -a Safari http://localhost:8081/login
```

### Common Options

N/A (GUI browser)

## Examples

### Example 1: Basic Usage

Open Safari and navigate to http://localhost:8081/login to trigger the flow.

### Example 2: Advanced Usage

Use Web Inspector (Cmd+Opt+I) to inspect the meta refresh response and confirm payload injection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- User agent strings in server logs identifying Safari
- Traffic from macOS IPs

## Related Procedures

- [[procedures/Trigger-XSS-via-Safari-Login]]

## Related Tools

- [[Chrome]]

## References

- Official documentation: https://developer.apple.com/safari/
- Related resources: WebKit security advisories
