---
id: 123e4567-e89b-12d3-a456-426614174005
name: undici
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.219Z'
platforms:
  - Node.js
tags:
  - http-client
  - ssrf
url: 'https://github.com/nodejs/undici'
validated: true
submitted: true
---

# undici

**Status**: Unverified

## Overview

Undici is an HTTP/1.1 client library for Node.js, designed for making efficient HTTP requests. It is commonly used in server-side applications but is vulnerable to SSRF in versions <= 5.8.1 when handling user-controlled pathname inputs.

## Description

Undici provides a fast, standards-compliant HTTP client with features like connection pooling and pipelining. In offensive security, it can be exploited via SSRF if pathname accepts absolute or protocol-relative URLs, allowing attackers to force requests to internal resources. Patched in version 5.8.2 by adding validation.

## Features

- Feature 1: Efficient HTTP/1.1 implementation with multiplexing
- Feature 2: Promise-based API for async requests
- Feature 3: Support for custom origins and pathnames in request options

## Installation

### Requirements

- Node.js >= 12
- npm or yarn

### Install Commands

```bash
npm install undici@5.8.1
```

## Basic Usage

```javascript
const undici = require("undici");
undici.request("http://example.com");
```

### Common Options

| Option | Description |
|--------|-------------|
| origin | Base URL for the request |
| pathname | Path component; vulnerable if user-controlled |
| method | HTTP method (default: GET) |

## Examples

### Example 1: Basic Usage

```javascript
undici.request({ origin: "http://example.com", pathname: "/api" });
```

### Example 2: Advanced Usage (Vulnerable Demo)

```javascript
undici.request({ origin: "http://example.com", pathname: "//127.0.0.1" });
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for undici imports in code
- Detect requests to internal IPs from app servers
- Version checks for <= 5.8.1

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://github.com/nodejs/undici
- CVE-2022-35949: https://hackerone.com/reports/1663788
