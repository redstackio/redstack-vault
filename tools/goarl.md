---
id: tool-uuid-001
url: 'https://github.com/cybercdh/goarl'
tags:
  - akamai
  - arl
  - recon
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.945Z'
validated: true
submitted: true
---
# goarl

**Status**: Unverified

## Overview

goarl is a Go-based tool for interacting with Akamai's Absolute Request Log (ARL), useful for generating logs, simulating requests, or exploiting misconfigurations in Akamai CDN setups during security testing and vulnerability discovery.

## Description

This tool allows users to craft and send requests that would be logged in Akamai ARL, helping in PoC development for issues like open ARL reflections leading to XSS. It's particularly relevant for testing DoD or enterprise sites using Akamai without proper sanitization, as in the reported vulnerability.

## Features

- Feature 1: Generate custom ARL entries for Akamai CDN
- Feature 2: Simulate request logging to identify reflection points
- Feature 3: Support for payload injection in log parameters for exploit testing

## Installation

### Requirements

- Go 1.16 or higher
- Git

### Install Commands

```bash
# Clone and build
go install github.com/cybercdh/goarl@latest
```

## Basic Usage

```bash
goarl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output for debugging |

## Examples

### Example 1: Basic Usage

```bash
goarl -url "https://target.com/search" -param "where=payload"
```

### Example 2: Advanced Usage

```bash
goarl -url "https://█████████/7/0/33/1d/" -param "search=www.citysearch.com/search?where=Binit%22%3E%3Cscript%3Ealert(1)%3C/script%3E" -method GET
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing unusual Go-based requests to Akamai endpoints
- GitHub traffic or binary downloads of goarl in security tools inventory

## Related Procedures

- [[procedures/Inject-XSS-Payload-via-Akamai-ARL-Search]]

## Related Tools

- [[Burp Suite]]
- [[Akamai CLI]]

## References

- Official GitHub: https://github.com/cybercdh/goarl
- Akamai ARL Documentation
