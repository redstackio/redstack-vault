---
id: tool-uuid-2
url: 'http://check-host.net/'
tags:
  - uptime
  - monitoring
  - http-check
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.110Z'
validated: true
submitted: true
---
# check-host.net

**Status**: Unverified

## Overview

check-host.net is an online monitoring tool for checking host availability via multiple protocols including HTTP, providing detailed response times and connectivity from worldwide locations, perfect for verifying DoS-induced downtime.

## Description

It supports checks for HTTP, ping, DNS, etc., with options for specific ports and intervals. In offensive security, it's used to confirm attack impact externally.

## Features

- Feature 1: Multi-protocol checks (HTTP, TCP, UDP)
- Feature 2: Global server locations for accurate pings
- Feature 3: Response time graphs and alerts

## Installation

### Requirements

- Web browser

### Install Commands

Web-based; no install.

## Basic Usage

Visit http://check-host.net/ and select check type.

### Common Options

| Option | Description |
|--------|-------------|
| Host | Target URL/IP |
| Protocol | HTTP/TCP/etc. |
| Port | Default 80/443 |

## Examples

### Example 1: Basic Usage

Check HTTP on https://staging.uzbey.com.

### Example 2: Advanced Usage

Specify multiple locations for comprehensive verification.

## Expected Output

Status reports like "Unreachable" with timings.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Traffic to check-host.net
- Query patterns for target hosts

## Related Procedures


## Related Tools

- [[tools/isup.me]]

## References

- Official site: http://check-host.net/
