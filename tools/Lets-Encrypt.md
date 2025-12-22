---
id: tool-lets-encrypt-001
url: 'https://letsencrypt.org/'
tags:
  - ssl-certificate
  - https
  - ca
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.681Z'
validated: true
submitted: true
---
# Let's Encrypt

**Status**: Unverified

## Overview

Let's Encrypt provides free, automated SSL/TLS certificates, exploited in subdomain takeovers to secure hijacked domains via HTTP-01 challenges, enabling trusted phishing sites.

## Description

Using ACME protocol, it verifies domain control by serving files from the site. Attackers place challenge tokens on S3/CloudFront to obtain certs for impersonation without owning the domain.

## Features

- Feature 1: HTTP-01 challenge via file serving
- Feature 2: Automated issuance with certbot
- Feature 3: 90-day validity with auto-renewal

## Installation

### Requirements

- Domain control (via hosting)
- Certbot or similar client

### Install Commands

```bash
# Ubuntu
git clone https://github.com/certbot/certbot.git
cd certbot
./tools/letsencrypt-auto --help
```
Or: `snap install --classic certbot`

## Basic Usage

```bash
certbot --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --manual | Manual mode for custom challenges |
| --preferred-challenges http | Use HTTP-01 |
| -d domain | Specify domain |

## Examples

### Example 1: Basic Usage

```bash
certbot certonly --manual --preferred-challenges http -d partners.ubnt.com
```

### Example 2: Advanced Usage

Integrate with web server for auto-validation.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Phishing]] Phishing

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Certificate Transparency logs showing certs for subdomains
- Unexpected ACME challenges in web logs

## Related Procedures


## Related Tools

- [[tools/AlphaSSL]]

## References

- Official documentation: https://letsencrypt.org/docs/
- Related resources: EFF Certificate Transparency
