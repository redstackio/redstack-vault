---
id: tool-vercel-dashboard
url: 'https://vercel.com'
tags:
  - cloud
  - hosting
  - domain-management
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.297Z'
validated: true
submitted: true
---
# Vercel-Dashboard

**Status**: Unverified

## Overview

The Vercel Dashboard is a web-based interface for managing deployments, domains, and projects on the Vercel platform, commonly used in security testing for subdomain takeover reconnaissance and claiming attempts.

## Description

Vercel provides serverless hosting and edge functions, with the dashboard allowing users to link custom domains via CNAME records. In offensive security, it's leveraged to detect and exploit dangling subdomains where DNS points to Vercel without ownership, enabling potential hijacks for malicious content deployment.

## Features

- Feature 1: Domain management for adding and verifying custom subdomains
- Feature 2: Project deployment oversight to check for unlinked CNAMEs
- Feature 3: Authorization and verification flows to prevent unauthorized claims

## Installation

### Requirements

- Web browser (Chrome, Firefox recommended)
- Internet access

### Install Commands

No installation required; access via browser.

## Basic Usage

Visit https://vercel.com/login to authenticate, then navigate to projects/settings/domains.

### Common Options

| Option | Description |
|--------|-------------|
| Domains Tab | Manage and add subdomains |
| Settings | Configure project-specific domains |

## Examples

### Example 1: Basic Usage

Log in and go to https://vercel.com/[username]/project/settings/domains to list domains.

### Example 2: Advanced Usage

Search for a subdomain like 'proxies.example.com' to check availability and attempt addition.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Vulnerability Scanning]] Vulnerability Scanning

### Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual login attempts to Vercel from security testing IPs
- API calls to domain endpoints without corresponding deployments
- Audit log entries for failed domain additions

## Related Procedures


## Related Tools

- [[tools/DNS-Tools]] (for initial CNAME discovery)
- [[tools/Burp-Suite]] (for intercepting dashboard requests)

## References

- Official documentation: https://vercel.com/docs
- Related resources: HackerOne reports on subdomain takeovers
