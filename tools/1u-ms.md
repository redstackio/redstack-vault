---
url: 'http://1u.ms/'
tags:
  - dns-rebinding
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.891Z'
id: 2e8eb9cb-28d4-4e36-9901-399aaa8f82f5
validated: true
submitted: true
---
# 1u.ms

**Status**: Unverified

## Overview

1u.ms is a free online DNS rebinding service used in security testing to create domains that resolve to different IPs over time, commonly for bypassing SSRF protections.

## Description

The tool allows quick setup of rebinding attacks by configuring TTL and IP sequences via a web interface. It's particularly useful for cloud environments like AWS where IP whitelisting is common. No local installation needed; operates entirely online.

## Features

- Feature 1: Custom TTL for rebinding timing (e.g., 1 second)
- Feature 2: Multiple IP resolution sequences
- Feature 3: Simple web-based configuration without coding

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

No installation required; access via browser.

## Basic Usage

Visit http://1u.ms/ and enter configuration details.

### Common Options

| Option | Description |
|--------|-------------|
| TTL | Time to live for each resolution (seconds) |
| IPs | Sequence of IPs to resolve to |

## Examples

### Example 1: Basic Rebinding

Configure: IP1: 8.8.8.8 (TTL 1s), IP2: 169.254.169.254.

### Example 2: Advanced Usage

Set multiple rebinds for repeated tests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Queries to known rebinding domains (e.g., *.1u.ms)
- Anomalous DNS TTL in logs
- Rapid IP changes for same domain

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official site: http://1u.ms/
- DNS Rebinding documentation
