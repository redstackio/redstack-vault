---
url: 'https://www.cloudflare.com'
tags:
  - proxy
  - cdn
  - caching
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.417Z'
id: 22f45994-e0bb-4cdb-849d-fcbfdc71c427
validated: true
submitted: true
---
# CloudFlare Proxy

**Status**: Unverified

## Overview

CloudFlare acts as a proxy/CDN that caches static files like .css, enabling Web Cache Deception by storing dynamic user content from Discourse regionally for attacker retrieval.

## Description

Default CloudFlare settings cache based on extensions (e.g., .css as static), ignoring dynamic nature. This leads to regional shared caches (13 PoPs) that can be tainted via victim browsers and read server-side.

## Features

- Feature 1: Regional caching for performance
- Feature 2: MIME-type based rules (static for .css)
- Feature 3: CF-Cache-Status headers for verification

## Installation

### Requirements

- Domain DNS pointed to CloudFlare

### Install Commands

N/A (service signup)

## Basic Usage

Proxy enabled via dashboard; no CLI.

### Common Options

| Option | Description |
|--------|-------------|
| Cache Rules | Bypass for dynamic paths |
| Purge Cache | Clear tainted entries |

## Examples

### Example 1: Basic Usage

Enable proxy on DNS record.

### Example 2: Advanced Usage

Set page rule: *discourse.org/u/* Cache Level: Bypass

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Impair Defenses]]

### Tactics

- [[Defense Evasion]]

## Detection

Indicators and methods for detecting this tool's usage:

- CF-Cache-Status: HIT on user routes
- Regional traffic spikes to .css
- Cache analytics in dashboard

## Related Procedures

- [[procedures/Trigger-CloudFlare-Caching-of-Dynamic-Content-via-CSS-Extension]]

## Related Tools

- [[tools/PHP-for-Server-Side-Extraction]]

## References

- Official documentation: https://developers.cloudflare.com/cache
