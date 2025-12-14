---
id: tool-uuid-001
url: 'https://github.com/0x3c3e/recloud'
name: recloud
tags:
  - aws
  - subdomain-takeover
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.909Z'
validated: true
submitted: true
---
# recloud

**Status**: Unverified

## Overview

recloud is a proof-of-concept tool for demonstrating IP reuse and subdomain takeover in AWS Elastic IP scenarios, simulating dangling IP attacks.

## Description

Designed for security researchers, recloud helps verify and exploit reusable cloud IPs by checking availability and simulating takeovers. It's useful in red teaming for cloud misconfiguration testing, particularly AWS environments.

## Features

- Feature 1: IP availability checking in AWS pools
- Feature 2: Subdomain resolution simulation
- Feature 3: PoC for Elastic IP reuse attacks

## Installation

### Requirements

- Go 1.16+
- Git

### Install Commands

```bash
go install github.com/0x3c3e/recloud@latest
```

## Basic Usage

```bash
recloud --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
recloud --ip 52.XX.XX.XX --subdomain mta1a1.spmail.uber.com
```

### Example 2: Advanced Usage

```bash
recloud --ip 52.XX.XX.XX --subdomain mta1a1.spmail.uber.com --simulate
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- API calls to AWS EC2 AllocateAddress
- Anomalous Go binary network traffic
- GitHub repo access logs

## Related Procedures


## Related Tools

- [[AWS CLI]]

## References

- Official GitHub: https://github.com/0x3c3e/recloud
