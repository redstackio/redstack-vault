---
id: t-fastly-management-dashboard
url: 'https://manage.fastly.com/services/all'
tags:
  - cdn
  - domain-management
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.671Z'
validated: true
submitted: true
---
# Fastly-Management-Dashboard

**Status**: Unverified

## Overview

The Fastly Management Dashboard is a web-based interface for configuring and managing Fastly's edge cloud services, including domain provisioning and TLS setup, commonly used in security testing for domain takeover scenarios involving CDN subdomains.

## Description

This dashboard allows users to create services, add domains, configure hosts, and provision free TLS certificates. In offensive security, it's leveraged to claim unmonitored subdomains under freetls.fastly.net, enabling attacks like CSP bypass when such domains are whitelisted in applications. Features include VCL scripting for custom logic, real-time activation, and analytics. No installation required; access via browser after account creation.

## Features

- Feature 1: Service creation and management for CDN configurations
- Feature 2: Domain attachment with automatic TLS provisioning via free tier
- Feature 3: Host and backend setup for content control and routing

## Installation

### Requirements

- Web browser (Chrome, Firefox recommended)
- Fastly account (free signup)

### Install Commands

No installation needed; access via https://manage.fastly.com after login.

## Basic Usage

Log in and navigate to services for management.

### Common Options

| Option | Description |
|--------|-------------|
| Services Tab | View and create services |
| Domains Section | Add and configure domains |
| VCL Editor | Custom scripting for responses |

## Examples

### Example 1: Basic Usage

Access https://manage.fastly.com/services/all to list services.

### Example 2: Advanced Usage

Create a service, add a domain, and configure a host to serve custom content.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Compromise Infrastructure]] Compromise Infrastructure

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual service creations on Fastly tied to sensitive domains
- Traffic spikes from freetls.fastly.net subdomains
- Logins from unfamiliar IPs to management dashboard

## Related Procedures


## Related Tools

- [[tools/AWS-Console]]
- [[tools/Cloudflare-Dashboard]]

## References

- Official documentation: https://docs.fastly.com
- Related resources: Fastly TLS guide
