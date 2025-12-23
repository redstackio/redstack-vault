---
id: tool-certbot
url: 'https://certbot.eff.org/'
tags:
  - ssl
  - tls
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.609Z'
validated: true
submitted: true
---
# Certbot

**Status**: Unverified

## Overview

Certbot is an automated tool for obtaining and installing free Let's Encrypt SSL/TLS certificates, crucial for securing taken-over subdomains to handle secure cookies.

## Description

In attacks, it's used post-takeover to enable HTTPS on malicious servers, bypassing secure flag restrictions on session cookies like UBIC_AUTH.

## Features

- Feature 1: Automated domain validation and cert renewal
- Feature 2: Integration with Apache/Nginx
- Feature 3: HTTP-01 challenge via file hosting

## Installation

### Requirements

- Ubuntu/Debian with Apache

### Install Commands

```bash
# On Ubuntu
apt install certbot python3-certbot-apache
```

## Basic Usage

```bash
certbot --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --apache | Auto-configure for Apache |
| -d | Domain to certify |

## Examples

### Example 1: Basic Usage

```bash
certbot certonly --standalone -d example.com
```

### Example 2: Advanced Usage

```bash
certbot --apache -d ping.ubnt.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Certificate Transparency logs showing new certs for subdomains
- Validation file requests during issuance

## Related Procedures

- [[procedures/Host-Malicious-Content-on-Taken-Over-Subdomain]]

## Related Tools

- [[tools/acme.sh]]
- [[tools/GoDaddy-Domain-Verification]]

## References

- Official documentation: https://certbot.eff.org/docs/
