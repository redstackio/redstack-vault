---
url: 'https://blackfan.ru/bugbounty/webcachedeception.php'
tags:
  - cache-poisoning
  - xss
type: tool
platforms:
  - Web
description: >-
  PHP script for automating web cache poisoning attacks by sending crafted
  requests to inject payloads.
id: 39e722b4-9f77-4b7b-b9a3-934953466d9e
created_at: '2025-12-13T09:00:34.539Z'
updated_at: '2025-12-13T09:00:34.539Z'
verified: false
validated: true
submitted: true
---
# webcachedeception.php

**Status**: Unverified

## Overview

A PHP script designed to automate web cache poisoning by crafting HTTP requests with specific headers to inject XSS payloads into caches, commonly used in bug bounty hunting for vulnerabilities like those in Discourse.

## Description

The tool sends requests to poison caches with user-provided payloads, targeting mechanisms like those in CloudFront, and specifies cache duration. It's useful for demonstrating stored XSS via cache deception.

## Features

- Feature 1: Automates header manipulation for cache poisoning
- Feature 2: Supports custom payloads and durations
- Feature 3: Generates poisoned URLs for verification

## Installation

### Requirements

- Web server with PHP
- Network access

### Install Commands

```bash
# Download or access directly via URL
```

## Basic Usage

```bash
https://blackfan.ru/bugbounty/webcachedeception.php --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `url` | Target URL |
| `payload` | Injection payload |
| `cache` | Poison duration |

## Examples

### Example 1: Basic Usage

```bash
https://blackfan.ru/bugbounty/webcachedeception.php?url=https://target.com/?param&payload=<script>alert(1)</script>&cache=60
```

### Example 2: Advanced Usage

```bash
https://blackfan.ru/bugbounty/webcachedeception.php?url=https://meta.discourse.org/?cacheattack&payload=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E&cache=60
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual X-Forwarded-Host headers
- Detection method 2: Log cache poisoning attempts via anomalous parameters

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

- Official documentation
- Related resources
