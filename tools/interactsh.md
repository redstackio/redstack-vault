---
id: 070cb11a-44d8-4680-9c23-12ee245ebcc7
name: interactsh
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.095Z'
platforms:
  - Linux
  - Windows
tags:
  - oob
  - rce
url: null
validated: true
submitted: true
---

# interactsh

**Status**: Unverified

## Overview

Interactsh is an out-of-band interaction tool for capturing DNS, HTTP, and other requests during security testing, particularly for blind RCE or exfiltration verification.

## Description

It provides unique domains for payloads, logging interactions from targets. Essential for confirming exploits like deserialization RCE where direct output isn't visible.

## Features

- Feature 1: DNS/HTTP/SMTP interaction polling
- Feature 2: Unique subdomain generation
- Feature 3: Real-time logging and correlation

## Installation

### Requirements

- Go 1.16+
- Network access for polling

### Install Commands

```bash
# Install with Go
go install github.com/projectdiscovery/interactsh-client@latest
go install github.com/projectdiscovery/interactsh-server@latest
```

## Basic Usage

```bash
interactsh-client -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `--domain` | Custom domain base |
| `-v` | Verbose mode |

## Examples

### Example 1: Basic Usage

```bash
interactsh-client
```

### Example 2: Advanced Usage

```bash
interactsh-client -v --json-output interactions.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Alternative Protocol]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- DNS queries to interactsh.com subdomains
- Client polling traffic to interact.sh
- Log entries for OOB interactions

## Related Procedures

- [[procedures/Observe-RCE-Confirmation-via-Interactsh]]

## Related Tools

- [[tools/ysoserial.net]]

## References

- Project Discovery: https://github.com/projectdiscovery/interactsh
