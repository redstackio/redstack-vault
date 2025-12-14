---
url: 'https://is.gd/'
tags:
  - url-shortener
  - payload
type: tool
platforms:
  - Web
description: >-
  URL shortening service used to create compact links for injecting external
  scripts in payloads with length restrictions.
id: 946edcc1-6b10-49b1-9580-4b6a81797992
created_at: '2025-12-13T23:56:20.171Z'
updated_at: '2025-12-13T23:56:20.171Z'
verified: false
validated: true
submitted: true
---
# is.gd URL Shortener

**Status**: Unverified

## Overview

is.gd is a free URL shortening service that creates short links from long URLs, useful in security testing for fitting payloads into restricted fields like UUIDs.

## Description

The tool allows quick shortening of URLs without registration, making it ideal for embedding external resources in exploits like XSS where length is limited.

## Features

- Feature 1: Instant URL shortening
- Feature 2: Custom short links
- Feature 3: Stats tracking

## Installation

### Requirements

- Web browser or API access

### Install Commands

No installation needed; use via website or API.

## Basic Usage

```bash
curl -i 'https://is.gd/create.php?format=simple&url=http://example.com'
```

### Common Options

| Option | Description |
|--------|-------------|
| `format=simple` | Return only the short URL |
| `url=` | The long URL to shorten |

## Examples

### Example 1: Basic Usage

```bash
curl -i 'https://is.gd/create.php?format=simple&url=http://malicious-js.com/script.js'
```

### Example 2: Advanced Usage

Use in scripts to automate shortening.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for requests to is.gd domain
- Check for shortened URLs in user inputs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[bit.ly]]
- [[tinyurl]]

## References

- https://is.gd/
- API documentation
