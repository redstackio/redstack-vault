---
url: >-
  https://portswigger.net/daily-swig/path-confusion-web-cache-deception-threatens-user-information-online
tags:
  - web
  - deception
type: tool
platforms:
  - Web
description: Technique to exploit caching mechanisms for information disclosure
id: 71a0a977-3603-490b-8673-bd6f5cdd6925
created_at: '2025-12-13T09:00:34.572Z'
updated_at: '2025-12-13T09:00:34.572Z'
verified: false
validated: true
submitted: true
---
# Web Cache Deception Concept

**Status**: Unverified

## Overview

Web Cache Deception is a technique that exploits web caching mechanisms to store and retrieve sensitive user data by deceiving the cache into treating dynamic content as static.

## Description

This concept involves path confusion attacks where appending static extensions to dynamic URLs tricks caches into storing private information, useful in offensive security for token theft and more.

## Features

- Exploits caching misconfigurations
- Enables information disclosure
- Applicable to web applications with CDNs or proxies

## Installation

### Requirements

- Web browser or HTTP client
- Knowledge of target caching behavior

### Install Commands

```bash
# No installation required, conceptual technique
```

## Basic Usage

```bash
curl "https://target.com/dynamic.css"
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Conceptual - use HTTP tools |

## Examples

### Example 1: Basic Usage

```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css"
```

### Example 2: Advanced Usage

```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css" -H "User-Agent: custom"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Steal Web Session Cookie]]

### Tactics

- [[Initial Access]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for URLs with mismatched extensions
- Check cache logs for sensitive data storage

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp-Suite]]
- [[curl]]

## References

- https://portswigger.net/daily-swig/path-confusion-web-cache-deception-threatens-user-information-online
