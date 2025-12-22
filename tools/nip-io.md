---
id: tool-nip-io
url: 'https://nip.io'
tags:
  - dns-rebinding
  - ssrf
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.618Z'
validated: true
submitted: true
---
# nip-io

**Status**: Unverified

## Overview

DNS service for wildcard resolution, enabling rebinding attacks to bypass IP restrictions in SSRF.

## Description

nip.io resolves subdomains like 10.0.0.1.nip.io to 10.0.0.1, allowing attackers to target internal IPs via external domains.

## Features

- Feature 1: Arbitrary IP resolution via subdomains
- Feature 2: Supports IPv4/IPv6
- Feature 3: No registration needed

## Installation

### Requirements

- None

### Install Commands

Web-based.

## Basic Usage

Use in URL: http://10.0.0.1.nip.io

### Common Options

N/A

## Examples

### Example 1: Basic Usage

http://127.0.0.1.nip.io for localhost rebinding.

### Example 2: Advanced Usage

https://10.x.x.x.nip.io for HTTPS internal.

## MITRE ATT&CK Mapping

### Techniques

- [[Vulnerability Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

- DNS queries to nip.io with internal IPs

## Related Procedures

- [[procedures/Enumerate-Internal-IPs-with-DNS-Rebinding]]

## Related Tools

- [[tools/localtest-me]]

## References

- https://nip.io
