---
id: tool-pipedream
url: 'https://pipedream.net'
tags:
  - request-bin
  - exfil
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.098Z'
validated: true
submitted: true
---
# Pipedream.net

**Status**: Unverified

## Overview

Pipedream.net is a request bin service for capturing and logging HTTP requests, used to verify outbound connections from RCE payloads in compromised environments like Elastic Cloud.

## Description

It creates temporary endpoints to inspect headers, body, and params from curl or other requests, helping confirm network access post-RCE without complex setup.

## Features

- Feature 1: Instant request bin creation.
- Feature 2: Real-time logging and inspection.
- Feature 3: Supports HTTPS with query params.

## Installation

### Requirements

- Web browser.

### Install Commands

N/A (web-based).

## Basic Usage

Visit https://pipedream.net and create a bin.

### Common Options

| Option | Description |
|--------|-------------|
| Bin URL | Unique endpoint like https://enu8lspgwcj2k.x.pipedream.net |

## Examples

### Example 1: Basic Usage

Create bin at https://enu8lspgwcj2k.x.pipedream.net; send curl -k to it.

### Example 2: Advanced Usage

Monitor multiple requests with timestamps.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Tactics

- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound HTTPS to pipedream.net domains.
- Unusual query params in requests.

## Related Procedures

- [[procedures/Host-Malicious-HTML-Payload-for-Chromium-RCE]]

## Related Tools

- [[tools/Requestbin.com]]

## References

- https://pipedream.net/docs/
