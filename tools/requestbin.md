---
id: tool-requestbin
url: 'https://requestbin.fullcontact.com'
tags:
  - ssrf
  - request-capture
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.375Z'
validated: true
submitted: true
---
# requestbin

**Status**: Unverified

## Overview

RequestBin is an online service for creating temporary endpoints (bins) to inspect and debug HTTP requests, useful for capturing SSRF payloads and analyzing server behavior.

## Description

Users create a bin to receive requests, viewing headers, body, and source IP. In security testing, it's used to confirm SSRF by seeing internal server requests hit the bin.

## Features

- Feature 1: Instant bin creation with unique URLs
- Feature 2: Real-time request inspection (headers, params, IP)
- Feature 3: Export and sharing of captured data

## Installation

### Requirements

- Web browser

### Install Commands

N/A - Web-based service.

## Basic Usage

Visit https://requestbin.fullcontact.com and create a bin.

### Common Options

N/A

## Examples

### Example 1: Basic Usage

Create bin at https://requestbin.fullcontact.com, get URL like /r/abc123, direct SSRF to it, and monitor incoming requests.

### Example 2: Advanced Usage

Use bin to capture multiple requests and filter by IP or headers.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Steal Application Access Token]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound traffic to requestbin domains
- Unusual request patterns from servers
- Log analysis for bin URLs in payloads

## Related Procedures


## Related Tools

- [[tools/ngrok]]
- [[tools/burp-suite]]

## References

- Official site: https://requestbin.fullcontact.com
