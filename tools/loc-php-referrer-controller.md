---
id: tool-loc-php
url: 'http://spqr.zz.mu/loc.php'
tags:
  - referrer-tool
  - php-redirect
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.695Z'
validated: true
submitted: true
---
# loc-php-referrer-controller

**Status**: Unverified

## Overview

Custom PHP script used to control HTTP referrer headers for testing web vulnerabilities like XSS by spoofing referrers during redirects.

## Description

This tool is a simple PHP redirector that sets a custom Referer header based on input parameters and forwards to a target URL. It's ideal for scenarios requiring precise control over browser navigation and headers in offensive security testing, such as exploiting referrer-based DOM XSS.

## Features

- Feature 1: Sets arbitrary Referer header via URL parameters.
- Feature 2: Performs HTTP redirect to specified target.
- Feature 3: Supports payload injection in referrer string.

## Installation

### Requirements

- PHP-enabled web server (e.g., Apache with mod_php).
- Basic file hosting capability.

### Install Commands

```bash
# Create loc.php file with content:
# <?php header('Referer: ' . $_GET[0]); header('Location: ' . $_GET[1]); ?>
# Upload to server
```

## Basic Usage

```bash
# Access via browser or curl with parameters
curl "http://yourserver/loc.php?malicious-referrer&target-url"
```

### Common Options

| Option | Description |
|--------|-------------|
| First param | Referrer string (e.g., '//search.informatica.com/payload') |
| Second param | Redirect URL (e.g., 'https://target.com?myk=xxx') |

## Examples

### Example 1: Basic Usage

```bash
# Spoof referrer and redirect
curl "http://spqr.zz.mu/loc.php?//search.informatica.com/onmouseover=alert(1)&https://kb.informatica.com/page?myk=xxx"
```

### Example 2: Advanced Usage

```bash
# In browser: http://spqr.zz.mu/loc.php?prefix/payload&full-target-url
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Referer headers in access logs containing JavaScript.
- High volume of redirects from external PHP endpoints.

## Related Procedures

- [[procedures/Craft-Malicious-Referrer-for-XSS-Injection]]

## Related Tools

- [[Burp Suite]]
- [[Custom Redirect Scripts]]

## References

- HackerOne Report #189834
