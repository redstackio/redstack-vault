---
id: tool-certbot
url: 'https://certbot.eff.org/#ubuntutrusty-apache'
tags:
  - ssl
  - lets-encrypt
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:43.042Z'
validated: true
submitted: true
---
# certbot

**Status**: Unverified

## Overview

Utility for obtaining free SSL/TLS certificates from Let's Encrypt, used to secure taken-over subdomains for HTTPS exploitation.

## Description

Automates domain validation via HTTP challenge, installing certs for Apache/Nginx, critical for mimicking legitimate HTTPS traffic.

## Features

- Feature 1: Automated renewal
- Feature 2: Webroot validation
- Feature 3: Integration with web servers

## Installation

### Requirements

- Python 3
- Web server with document root

### Install Commands

```bash
apt install certbot
```

## Basic Usage

```bash
certbot --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --webroot | Use webroot plugin |
| -d | Domain to certify |

## Examples

### Example 1: Basic Usage

```bash
certbot certonly --webroot -w /var/www -d example.com
```

### Example 2: Advanced Usage

```bash
certbot renew --dry-run
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[External Remote Services]] External Remote Services

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Let's Encrypt rate limit hits
- Unusual cert issuances for subdomains

## Related Procedures

- [[procedures/Create-AWS-Cloudfront-Distribution-for-Takeover]]

## Related Tools

- [[GoDaddy Domain Verification]]

## References

- EFF Certbot docs
