---
id: tool-libcurl-001
url: 'https://curl.se/libcurl/'
tags:
  - library
  - http
  - url-parse
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.513Z'
configuration: Version 7.68.0-1ubuntu2.24 on Ubuntu 20.04
validated: true
submitted: true
---
# libcurl

**Status**: Unverified

## Overview

libcurl is a client-side URL transfer library providing robust HTTP request capabilities; central to this vulnerability due to inconsistent IPv6 zone ID parsing.

## Description

Used in applications for URL validation and fetching, libcurl strips zone identifiers from IPv6 literals (e.g., [fe80::1%eth0] becomes [fe80::1]), enabling SSRF by default interface routing. Tested via custom C code; alternatives like Go net/url handle correctly.

## Features

- Feature 1: Multi-protocol support including HTTP/HTTPS.
- Feature 2: URL parsing via CURLU API.
- Feature 3: Interface binding for connections.

## Installation

### Requirements

- C compiler and development headers.

### Install Commands

```bash
# Ubuntu
apt install libcurl4-openssl-dev
```

## Basic Usage

```bash
# In C code
#include <curl/curl.h>
CURL *curl = curl_easy_init();
```

### Common Options

| Option | Description |
|--------|-------------|
| `CURLUPART_HOST` | Hostname parsing |
| `CURLOPT_URL` | Set URL for request |

## Examples

### Example 1: Basic Usage

```c
curl_easy_setopt(curl, CURLOPT_URL, "http://example.com");
curl_easy_perform(curl);
```

### Example 2: Advanced Usage

```c
// Parse IPv6 URL
CURLU *uh = curl_url();
curl_url_set(uh, CURLUPART_URL, "http://[fe80::1%eth0]/", 0);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Static analysis for libcurl-linked binaries.
- Runtime monitoring of parsing anomalies.

## Related Procedures


## Related Tools

- [[tools/curl]]
- [[tools/trurl]]

## References

- Official documentation: https://curl.se/libcurl/c/libcurl-tutorial.html
