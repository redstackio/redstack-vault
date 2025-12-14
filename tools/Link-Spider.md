---
url: ''
tags:
  - web
  - crawling
  - recon
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  A generic web link spidering tool for crawling sites to trigger caching or
  enumerate links, often implemented via wget or custom scripts.
id: 40152c4e-7865-43ef-a5c9-3600c0d0b88a
created_at: '2025-12-14T03:15:26.517Z'
updated_at: '2025-12-14T03:15:26.517Z'
verified: false
validated: true
submitted: true
---
# Link-Spider

**Status**: Unverified

## Overview

Link Spider is a tool or technique for recursively following and requesting web links to map site structure or trigger server behaviors like caching, commonly used in web vulnerability exploitation such as cache poisoning.

## Description

It simulates user navigation by fetching pages and links without full downloads, ideal for poisoning caches in CMS like Concrete by embedding manipulated hostnames. Features include user-agent spoofing, recursion limits, and robots.txt ignoring for comprehensive coverage in offensive ops.

## Features

- Feature 1: Recursive link following to cover site depth
- Feature 2: Head-only requests to avoid bandwidth waste
- Feature 3: Customizable user agents to evade detection

## Installation

### Requirements

- wget or similar HTTP client installed

### Install Commands

```bash
# wget is usually pre-installed; otherwise:
sudo apt update && sudo apt install wget
```

## Basic Usage

```bash
wget --spider https://example.com/
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| --recursive, -r | Turn on recursive retrieving |
| --spider | Spider mode - only fetch URLs |

## Examples

### Example 1: Basic Usage

```bash
wget --spider --recursive https://fake-site.com/
```

### Example 2: Advanced Usage

```bash
wget --spider -r -l 2 -U "Mozilla/5.0" https://site.com/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual spike in rapid GET requests from single IP
- Detection method 2: Log patterns matching wget user agents or recursive patterns

## Related Procedures

- [[procedures/Spider-Site-to-Generate-Poisoned-Cache-Files]]

## Related Tools

- [[Burp Suite]]
- [[ZAP]]

## References

- wget man page
- Web crawling techniques in offensive security
