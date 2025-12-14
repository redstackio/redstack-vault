---
id: tool-uuid-1
url: 'https://github.com/projectdiscovery/subfinder'
tags:
  - recon
  - subdomain-enum
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.217Z'
validated: true
submitted: true
---
# Subfinder

**Status**: Unverified

## Overview

Subfinder is a fast passive subdomain discovery tool that leverages multiple sources like APIs and search engines for comprehensive enumeration without direct DNS queries.

## Description

Ideal for offensive security, Subfinder collects subdomains from passive intelligence sources, aiding in identifying misconfigurations like dangling DNS records in cloud environments such as AWS.

## Features

- Feature 1: Passive enumeration from 30+ sources
- Feature 2: High-speed concurrent querying
- Feature 3: Output filtering and deduplication

## Installation

### Requirements

- Go 1.16+

### Install Commands

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

## Basic Usage

```bash
subfinder -d example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Domain to enumerate |
| `-o` | Output file |
| `-v` | Verbose mode |

## Examples

### Example 1: Basic Usage

```bash
subfinder -d 8x8.com -o subs.txt
```

### Example 2: Advanced Usage

```bash
subfinder -d 8x8.com -all -o subs.txt -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to passive sources like crt.sh
- DNS query spikes from enumeration

## Related Procedures

- [[procedures/Identify-Dangling-DNS-Records-for-Subdomain-Takeover]]

## Related Tools

- [[Amass]]
- [[Sublist3r]]

## References

- Official GitHub repository
