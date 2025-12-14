---
id: t-smokescreen
url: 'https://github.com/stripe/smokescreen'
tags:
  - proxy
  - ssrf-prevention
type: tool
verified: false
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.909Z'
validated: true
submitted: true
---
# Smokescreen

**Status**: Unverified

## Overview

Smokescreen is an open-source proxy tool developed by Stripe to restrict outbound HTTP/HTTPS requests from internal services, primarily to mitigate SSRF attacks by enforcing allow/deny lists on URLs.

## Description

Built in Go, Smokescreen acts as a reverse proxy that validates and rewrites outbound requests based on configurable rules, including an optional deny_list for additional external URL restrictions. It's commonly used in microservices architectures to prevent internal services from accessing unauthorized domains, though vulnerabilities like incomplete domain matching can lead to bypasses. In offensive security, it's analyzed for weaknesses in proxy logic.

## Features

- Feature 1: URL validation against allow/deny lists to block SSRF
- Feature 2: Request rewriting and logging for compliance
- Feature 3: Support for internal service integration via HTTP proxying

## Installation

### Requirements

- Go 1.16 or higher
- Git for cloning the repository

### Install Commands

```bash
# Clone the repository
git clone https://github.com/stripe/smokescreen.git

# Build the binary
cd smokescreen
make build
```

## Basic Usage

```bash
./smokescreen --config config.yaml
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--config` | Path to configuration file |
| `--deny-list` | Enable deny_list rules |

## Examples

### Example 1: Basic Usage

```bash
./smokescreen --config smokescreen.yaml --listen :8080
```

### Example 2: Advanced Usage

```bash
./smokescreen --config smokescreen.yaml --deny-list-domains "example.com" --verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to proxy port (default 8080)
- Logs showing URL validation denials

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/HAProxy]]
- [[tools/Nginx]]

## References

- Official documentation: https://github.com/stripe/smokescreen
- Related resources: Stripe engineering blog on SSRF prevention
