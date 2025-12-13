---
url: >-
  https://support.cloudflare.com/hc/en-us/articles/200172516-Which-file-extensions-does-Cloudflare-cache-for-static-content-
tags:
  - caching
  - proxy
type: tool
platforms:
  - Web
description: >-
  Proxy and caching service that caches static content based on file extensions,
  exploited for Web Cache Deception.
id: 96a988a2-cda3-4b31-8fe7-fcad64e8d0a6
created_at: '2025-12-13T09:00:34.434Z'
updated_at: '2025-12-13T09:00:34.434Z'
verified: false
validated: true
submitted: true
---
# CloudFlare

**Status**: Unverified

## Overview

CloudFlare is a web proxy and caching service that optimizes content delivery by caching static files based on extensions like .css, which can be exploited in Web Cache Deception attacks to cache dynamic content.

## Description

In this context, CloudFlare's default caching behavior for certain file extensions allows attackers to force caching of sensitive data from Discourse instances, leading to data leakage.

## Features

- Caches static content by extension
- Global CDN for performance
- Security features like DDoS protection

## Installation

### Requirements

- Domain registration
- CloudFlare account

### Install Commands

No installation needed; configure via CloudFlare dashboard.

## Basic Usage

```bash
# No CLI; managed via web interface
```

### Common Options

| Option | Description |
|--------|-------------|
| Caching Level | Standard, Aggressive |
| File Extensions | .css, .js, etc. |

## Examples

### Example 1: Basic Usage

Configure domain to proxy through CloudFlare.

### Example 2: Advanced Usage

Set custom cache rules for extensions.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor CF-Cache-Status headers
- Log requests with cacheable extensions to dynamic routes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools



## References

- Official documentation
