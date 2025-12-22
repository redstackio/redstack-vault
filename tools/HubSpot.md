---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
url: 'https://www.hubspot.com/'
tags:
  - hosting
  - cms
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:39:01.980Z'
validated: true
submitted: true
---
# HubSpot

**Status**: Unverified

## Overview

HubSpot is a marketing and CRM platform providing content management and hosting services. In security contexts, it's exploited for subdomain takeovers when DNS points to expired instances, allowing attackers to claim and host malicious content.

## Description

HubSpot's CMS allows easy deployment of HTML, PHP, and JS on custom domains via CNAME records. In the Roblox attack, an expired HubSpot site enabled takeover of devrel.roblox.com for phishing and script hosting. Features include drag-and-drop editing, analytics, and integrations, but misconfigurations lead to takeover risks.

## Features

- Feature 1: Custom domain hosting via CNAME for subdomains
- Feature 2: Support for dynamic content (PHP, JS) in marketing hubs
- Feature 3: Free tier for claiming unowned instances

## Installation

### Requirements

- Web browser and email for account signup
- No local install; SaaS platform

### Install Commands

N/A (web-based signup)

## Basic Usage

```bash
# No CLI; access via browser: https://app.hubspot.com
```

### Common Options

| Option | Description |
|--------|-------------|
| Signup | Create free account to claim instances |
| CMS Editor | Upload HTML/PHP files to pages |

## Examples

### Example 1: Basic Usage

Sign up at hubspot.com, claim dangling instance, map to subdomain, upload index.html.

### Example 2: Advanced Usage

In CMS, create page with PHP: Edit > Code > Paste script > Publish to subdomain.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- DNS queries showing CNAME to hs-sites.com on unused subdomains
- Anomalous content on marketing pages (e.g., scripts stealing data)
- HubSpot login alerts for claimed accounts

## Related Procedures


## Related Tools

- [[AWS S3]] (similar takeover vector)
- [[GitHub Pages]]

## References

- Official documentation: https://knowledge.hubspot.com
- Related resources: HackerOne reports on subdomain takeovers
