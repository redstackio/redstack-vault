---
url: 'https://ngrok.com/'
tags:
  - tunneling
  - exposure
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Tunneling tool for exposing local servers to the internet.
id: 2a5e8759-a608-465c-a0bb-a5508dca5c79
created_at: '2025-12-11T03:48:06.023Z'
updated_at: '2025-12-11T03:48:06.023Z'
verified: false
validated: true
submitted: true
---
# ngrok

**Status**: Unverified

## Overview

Ngrok creates secure tunnels to local services, useful for testing exploits involving remote callbacks or fake servers.

## Description

Commonly used in red teaming to expose local ports publicly without firewall changes, as in fake API setups for vulnerabilities.

## Features

- Feature 1: HTTP/HTTPS tunneling
- Feature 2: Custom domains
- Feature 3: Request inspection

## Installation

### Requirements

- Account for advanced features

### Install Commands

```bash
snap install ngrok
```

## Basic Usage

```bash
ngrok --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `http` | Tunnel HTTP |
| `--region` | Server region |

## Examples

### Example 1: Basic Usage

```bash
ngrok http 5000
```

### Example 2: Advanced Usage

```bash
ngrok tcp 22
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to ngrok domains
- Process monitoring for ngrok binary

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #localtunnel

## References

- https://ngrok.com/docs
