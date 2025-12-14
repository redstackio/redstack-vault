---
id: tool-libcurl
url: 'https://curl.se/libcurl/'
tags:
  - library
  - http
  - url-parsing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.037Z'
validated: true
submitted: true
---
# libcurl

**Status**: Unverified

## Overview

libcurl is a client-side URL transfer library for C/C++ applications; affected versions omit IPv6 zone IDs during parsing, leading to SSRF and bypass in URL-fetching apps.

## Description

Provides APIs like CURLU for URL manipulation (curl_url_set/get for CURLUPART_HOST/ZONEID). Alternatives include Rust URL parser, Go net/url, Python urllib/urllib3, which preserve zones. Used in web apps for HTTP requests.

## Features

- Feature 1: Multi-protocol support including HTTP over IPv6
- Feature 2: URL parsing and component extraction
- Feature 3: Easy integration in C applications

## Installation

### Requirements

- Development headers

### Install Commands

```bash
# On Ubuntu
apt install libcurl4-openssl-dev
```

## Basic Usage

```bash
# In C code
#include <curl/curl.h>
CURLU *url = curl_url();
curl_url_set(url, CURLUPART_URL, "http://[fe80::1%eth0]/", 0);
```

### Common Options

| Option | Description |
|--------|-------------|
| `CURLUPART_HOST` | Hostname part |
| `CURLUPART_ZONEID` | Zone ID part |

## Examples

### Example 1: Basic Usage

```c
curl_url_get(url, CURLUPART_HOST, &host, 0);
```

### Example 2: Advanced Usage

```bash
# Compile with -lcurl
gcc test.c -o test -lcurl
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Cloud Instance Metadata API]] Unsecured Web Services

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Static analysis for libcurl linking in binaries
- Runtime monitoring for CURLU API calls

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/curl]]
- [[tools/trurl]]

## References

- Official documentation: https://curl.se/libcurl/c/
- HackerOne: https://hackerone.com/reports/2814750
