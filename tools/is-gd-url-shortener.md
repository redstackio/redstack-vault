---
id: tool-isgd
url: 'https://is.gd/'
tags:
  - url-shortener
  - payload-delivery
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.389Z'
validated: true
submitted: true
---
# is.gd URL Shortener

**Status**: Unverified

## Overview

is.gd is a free URL shortening service used in security testing to compress long external links, such as JavaScript payloads, to fit within character limits of input fields like UUIDs.

## Description

In offensive security, is.gd helps deliver external resources (e.g., malicious JS files hosted on S3) without exceeding restrictions. Append parameters like ?11 for unique URLs. No API key needed for basic use; supports up to 30-character shorts.

## Features

- Feature 1: Instant shortening without registration
- Feature 2: Custom aliases for tracking
- Feature 3: Stats on click-throughs for payload verification

## Installation

### Requirements

- Web browser or curl for access

### Install Commands

No installation; access via web.

```bash
# No install needed
```

## Basic Usage

Visit https://is.gd/ and paste URL to shorten.

### Common Options

| Option | Description |
|--------|-------------|
| Custom alias | Specify short code |
| ?11 param | Generate unique short

## Examples

### Example 1: Basic Usage

Shorten https://s3.amazonaws.com/cachemoney/upservexss.js to //is.gd/z0i2sU.

```bash
curl -X POST https://is.gd/create.php -d "longurl=https://example.com/js/payload.js" -c cookies.txt
```

### Example 2: Advanced Usage

Use with custom code:

```bash
curl -X POST https://is.gd/create.php -d "shorturl=mypayload&longurl=https://example.com/js/payload.js"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor outbound requests to is.gd
- Block shortener domains in CSP
- Log unusual external script loads

## Related Procedures


## Related Tools

- [[bit.ly]]
- [[tinyurl]]

## References

- Official site: https://is.gd/
- API docs: https://isgd.dev/api
