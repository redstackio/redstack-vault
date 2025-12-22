---
url: 'https://github.com/Crypt0s/FakeDns'
tags:
  - dns
  - fake-server
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.230Z'
id: a8184058-8c2e-4dc1-a6bf-661aee34f843
validated: true
submitted: true
---
# FakeDns

**Status**: Unverified

## Overview

FakeDns is a lightweight fake DNS server written in Go, used in security testing to simulate custom DNS responses for bypassing restrictions like SSRF IP checks.

## Description

It allows defining arbitrary records (A, CNAME, etc.) via command-line or config, responding to queries on port 53. In this attack, it maps public subdomains to external IPs and internal ones to 0.0.0.0 for localhost targeting.

## Features

- Feature 1: Supports A, AAAA, CNAME, MX, TXT records
- Feature 2: Wildcard domain support (e.g., *.local.yourdomain.com)
- Feature 3: Simple CLI for adding records dynamically

## Installation

### Requirements

- Go 1.16+ installed

### Install Commands

```bash
# Clone and build
go install github.com/Crypt0s/FakeDns@latest
```

## Basic Usage

```bash
fakedns
```
Add records before running, e.g., `A example.com 1.2.3.4`

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| -v | Verbose logging |

## Examples

### Example 1: Basic Usage

```bash
A www.example.com 203.0.113.1
fakedns
```
Query with dig to verify.

### Example 2: Advanced Usage

```bash
A *.internal.com 0.0.0.0
A public.com 198.51.100.1
fakedns -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Port 53 traffic from non-standard DNS processes
- Anomalous resolutions in logs
- Go binary named fakedns

## Related Procedures

- [[procedures/Setup-FakeDns-with-Malicious-Records]]

## Related Tools

- [[tools/Dnsmasq]]

## References

- Official GitHub repo
