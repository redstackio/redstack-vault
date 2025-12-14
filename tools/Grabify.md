---
id: tool-grabify-001
url: 'https://grabify.link/'
tags:
  - tracking
  - reconnaissance
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.043Z'
validated: true
submitted: true
---
# Grabify

**Status**: Unverified

## Overview

Grabify is a free online URL shortening and tracking service used in security testing to monitor HTTP requests, capture IP addresses, and log headers without requiring server setup. It is commonly employed in SSRF verification to detect server-initiated fetches.

## Description

Grabify creates disposable shortened links that redirect to a user-specified URL while logging details of visitors, including IP, user-agent, timestamp, and referrer. In offensive security, it helps confirm vulnerabilities like SSRF by observing if a target server requests the link. Features include bot filtering (which can be disabled), geolocation, and exportable logs. It is web-based, requiring no installation, and suitable for quick reconnaissance in web application testing.

## Features

- Feature 1: IP logging and geolocation for request source identification
- Feature 2: Custom redirect URLs to mask tracking (e.g., to YouTube)
- Feature 3: Real-time dashboard with hit details and export options

## Installation

### Requirements

- Web browser
- Internet connection

### Install Commands

No installation needed; access via browser.

```bash
# No command required
```

## Basic Usage

```bash
# Visit https://grabify.link/ in browser
```

### Common Options

| Option | Description |
|--------|-------------|
| Bot Toggle | Filter out bot traffic (disable for SSRF to catch server requests) |
| Redirect URL | Target page after logging (e.g., http://youtube.com) |

## Examples

### Example 1: Basic Usage

1. Go to https://grabify.link/
2. Enter http://example.com as redirect
3. Create URL: https://grabify.link/ABC123
4. Use ABC123 to access logs

### Example 2: Advanced Usage

For SSRF: Disable bot toggle, create link, input into PoC, then check logs for server IP.

```bash
# No CLI; browser-based
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound requests to grabify.link domains from servers
- Unusual short-link resolutions in proxy logs
- Correlate with XML-RPC activity

## Related Procedures


## Related Tools

- [[Related Tool 1|tools/IPLogger]]
- [[Related Tool 2|tools/Canarytokens]]

## References

- Official site: https://grabify.link/
- Usage in SSRF: HackerOne reports on WordPress vulnerabilities
