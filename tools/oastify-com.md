---
id: tool-oastify
url: 'https://oastify.com'
tags:
  - oast
  - ssrf
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.620Z'
validated: true
submitted: true
---
# oastify-com

**Status**: Unverified

## Overview

OAST service for detecting out-of-band interactions from SSRF via DNS/HTTP callbacks.

## Description

oastify.com provides unique subdomains to monitor blind exploits like SSRF, logging requests and DNS queries from vulnerable backends.

## Features

- Feature 1: Real-time DNS and HTTP interaction logs
- Feature 2: Custom subdomain generation
- Feature 3: Header capture for fingerprinting

## Installation

### Requirements

- Web browser

### Install Commands

No installation; web-based.

## Basic Usage

Visit https://oastify.com, generate payload, monitor logs.

### Common Options

N/A

## Examples

### Example 1: Basic Usage

Generate sa66ovrblrbiviochnojtli2bthk5ft4.oastify.com and use in SSRF payload.

### Example 2: Advanced Usage

Monitor for User-Agent: python-requests/2.28.1.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound DNS to oastify.com subdomains
- HTTP requests to oastify from internal IPs

## Related Procedures

- [[procedures/Confirm-Blind-SSRF-with-External-Domain]]

## Related Tools

- [[tools/Burp-Collaborator]]

## References

- https://oastify.com
