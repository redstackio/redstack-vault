---
url: 'https://github.com/OWASP/Amass'
tags:
  - recon
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.178Z'
id: 678a2acb-be2c-4b1f-bb0c-f7c99d8640b7
validated: true
submitted: true
---
# Amass

**Status**: Unverified

## Overview

Amass is a tool for network mapping, external asset discovery, and reconnaissance using open-source intelligence.

## Description

It performs subdomain enumeration, DNS resolution, and more, ideal for initial attack surface discovery in web pentests.

## Features

- Feature 1: Passive and active enumeration modes
- Feature 2: Integration with multiple data sources
- Feature 3: Output in various formats

## Installation

### Requirements

- Go 1.16+

### Install Commands

```bash
go install -v github.com/owasp-amass/amass/v4/...@master
```

## Basic Usage

```bash
amass enum -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| --passive | Passive mode |

## Examples

### Example 1: Basic Usage

```bash
amass enum --passive -d example.com
```

### Example 2: Advanced Usage

```bash
amass enum --passive -d example.com -o output.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

- Monitor DNS query patterns
- Log tool signatures in network traffic

## Related Procedures

- [[procedures/Reconnaissance-and-Exposed-Git-Discovery]]

## Related Tools

- [[tools/Subfinder]]

## References

- Official GitHub repo
