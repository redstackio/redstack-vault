---
id: tool-alphassl-001
url: null
tags:
  - ssl-certificate
  - ca
  - alternative
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.676Z'
validated: true
submitted: true
---
# AlphaSSL

**Status**: Unverified

## Overview

AlphaSSL offers low-cost SSL certificates with simple verification, used as an alternative to Let's Encrypt for securing hijacked domains in phishing campaigns via file-based challenges.

## Description

As a Sectigo brand, it provides DV certs quickly. In attacks, it's used for easy issuance on taken-over subdomains to enable HTTPS without advanced setup, mimicking legitimate sites.

## Features

- Feature 1: Domain validation via HTTP file upload
- Feature 2: Rapid issuance (minutes)
- Feature 3: Compatible with CloudFront custom certs

## Installation

### Requirements

- Web hosting for validation file
- Email for order confirmation

### Install Commands

Web-based; no install.

## Basic Usage

Visit provider site, order DV cert, upload validation file to domain.

### Common Options

| Option | Description |
|--------|-------------|
| HTTP Validation | Place file at specified path |
| Domain | Enter hijacked subdomain |

## Examples

### Example 1: Basic Usage

Order cert for partners.ubnt.com, upload validation.txt to http://partners.ubnt.com/.well-known/.

### Example 2: Advanced Usage

Combine with CSR from CloudFront for seamless integration.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- CT logs for AlphaSSL-issued certs on owned domains
- Validation file requests in access logs

## Related Procedures


## Related Tools

- [[tools/Lets-Encrypt]]

## References

- Official documentation: https://www.alphassl.com/
- Related resources: Sectigo CA guidelines
