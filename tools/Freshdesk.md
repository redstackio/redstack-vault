---
id: tool-freshdesk
url: 'https://freshdesk.com'
tags:
  - helpdesk
  - takeover
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.881Z'
validated: true
submitted: true
---
# Freshdesk

**Status**: Unverified

## Overview

Freshdesk is a customer support platform that allows custom domain mapping, exploitable in subdomain takeovers via dangling DNS records.

## Description

Attackers claim inactive subdomains like fddkim.freshdesk.com to hijack traffic. Free tier enables quick registration without cost.

## Features

- Feature 1: Custom domain support for branding
- Feature 2: HTML/JS customization for portals
- Feature 3: Easy signup and propagation

## Installation

### Requirements

- Web browser
- Email for account

### Install Commands

N/A (web-based)

## Basic Usage

```bash
# No CLI; access via browser
# Visit freshdesk.com, sign up, claim domain
```

### Common Options

| Option | Description |
|--------|-------------|
| Admin Panel | Domain settings |
| Portal Customization | Upload content |

## Examples

### Example 1: Basic Usage

Sign up at freshdesk.com and add custom domain fddkim.freshdesk.com.

### Example 2: Advanced Usage

Configure portal with phishing form under claimed domain.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1583.001]] Acquire Infrastructure: Domains

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unexpected Freshdesk resolutions for subdomains
- API logs of new domain claims

## Related Procedures

- [[procedures/Claim-Subdomain-on-Freshdesk]]

## Related Tools

- [[Zendesk]]
- [[Intercom]]

## References

- Freshdesk documentation
- HackerOne reports on takeovers
