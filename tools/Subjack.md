---
url: 'https://github.com/haccer/subjack'
tags:
  - subdomain-takeover
  - recon
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  A Golang tool for detecting potential subdomain takeovers by checking against
  common cloud providers.
id: 3bff0425-a6a1-4c68-85d3-3aeae97adb66
created_at: '2025-12-14T05:32:23.698Z'
updated_at: '2025-12-14T05:32:23.698Z'
verified: false
validated: true
submitted: true
---
# Subjack

**Status**: Unverified

## Overview

Subjack is an open-source tool designed for scanning subdomains to detect takeover vulnerabilities by fingerprinting responses from services like AWS S3, GCP, and Heroku. It is commonly used in offensive security for identifying dangling DNS records quickly.

## Description

Subjack works by sending requests to subdomains and matching responses against known 'takeover available' signatures (e.g., 'NoSuchBucket' for S3). In the mozgcp.net scenario, it would flag GCP-related dangling records. It supports concurrent scanning and SSL checks, making it efficient for large domain lists.

## Features

- Feature 1: Scans against 50+ cloud providers and services
- Feature 2: Configurable threads and timeouts for performance
- Feature 3: JSON/CSV output for integration with other tools

## Installation

### Requirements

- Go 1.13+ installed
- Git

### Install Commands

```bash
# Clone and build
go install github.com/haccer/subjack@latest
```

Or download pre-built binaries from releases.

## Basic Usage

```bash
subjack --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-w` | Input wordlist of subdomains |
| `-t` | Number of threads |
| `-timeout` | Request timeout in seconds |
| `-o` | Output file |
| `-ssl` | Enable SSL checks |

## Examples

### Example 1: Basic Usage

```bash
subjack -w subdomains.txt -t 50 -o results.txt
```

### Example 2: Advanced Usage

```bash
subjack -w subs.txt -t 100 -timeout 30 -o vulnerable.json -ssl -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing high-volume DNS/HTTP requests to cloud endpoints
- Process monitoring for 'subjack' binary execution

## Related Procedures

- [[procedures/Discover-Dangling-DNS-Records]]

## Related Tools

- [[Amass]]
- [[Sublist3r]]

## References

- Official GitHub: https://github.com/haccer/subjack
- Related resources: OWASP Subdomain Takeover Guide
