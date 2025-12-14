---
id: tool-uuidgen-001
url: 'https://man7.org/linux/man-pages/man1/uuidgen.1.html'
tags:
  - cache-bypass
  - random
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.909Z'
validated: true
submitted: true
---
# uuidgen

**Status**: Unverified

## Overview

uuidgen generates universally unique identifiers, used to append random query strings to URLs, disabling CDN caching and bypassing throttling in DoS attacks.

## Description

In post-fix testing, $(uuidgen) ensures each request is unique, forcing fresh proxy fetches to slow2.php without cache hits.

## Features

- Feature 1: Generates RFC 4122 UUIDs
- Feature 2: Random or time-based variants
- Feature 3: Shell integration for commands

## Installation

### Requirements

- util-linux package

### Install Commands

```bash
apt install util-linux
```

## Basic Usage

```bash
uuidgen --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r` | Random UUID |
| `-t` | Time-based |

## Examples

### Example 1: Basic Usage

```bash
uuidgen
```

### Example 2: Advanced Usage

```bash
curl https://example.com?$(uuidgen)
```

## MITRE ATT&CK Mapping

### Techniques

- [[Network Denial of Service]] (for evasion)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

- Unusual query parameters in requests

## Related Procedures

- [[procedures/Post-Fix-DoS-Testing]]

## Related Tools

- [[tools/curl]]

## References

- man uuidgen
