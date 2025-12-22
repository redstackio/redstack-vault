---
id: tool-uuid-google-dns-lookup
url: 'https://dns.google.com/query'
tags:
  - dns
  - reconnaissance
  - lookup
type: tool
verified: false
platforms:
  - Web
  - DNS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.751Z'
validated: true
submitted: true
---
# Google-Public-DNS-Lookup

**Status**: Unverified

## Overview

Google Public DNS Lookup is a free web-based service for querying DNS records from Google's global DNS infrastructure. It is commonly used in security testing to enumerate DNS resource records, including security-related types like CAA (type 257), without installing software. Primary use cases include reconnaissance for misconfigurations in domain security setups.

## Description

This tool provides an intuitive interface for DNS queries, supporting all standard record types and options like DNSSEC validation. It returns raw DNS responses, making it ideal for verifying configurations like CAA records that prevent unauthorized certificate issuance. Queries are resolved via Google's anycast network for speed and reliability, with no rate limits for casual use.

## Features

- Feature 1: Support for all DNS record types (A, MX, CAA, etc.)
- Feature 2: DNSSEC validation to ensure response integrity
- Feature 3: Raw response display in text or JSON format

## Installation

### Requirements

- Web browser (Chrome, Firefox, etc.)
- Internet connection

### Install Commands

No installation required; access via web.

## Basic Usage

Access https://dns.google.com/query and fill in the form.

### Common Options

| Option | Description |
|--------|-------------|
| Name | Domain to query (e.g., gratipay.com) |
| Type | Record type (e.g., 257 for CAA) |
| DNSSEC | Enable validation (true/false) |

## Examples

### Example 1: Basic Usage

Query CAA for gratipay.com:

URL: https://dns.google.com/query?name=gratipay.com&type=257&dnssec=true

### Example 2: Advanced Usage

Query with specific class (default IN for Internet):

https://dns.google.com/query?name=example.com&type=257&dnssec=true&class=IN

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing queries to 8.8.8.8:53 (Google DNS) for type 257
- Web access logs to dns.google.com/query from security scanners

## Related Procedures


## Related Tools

- [[dig]]
- [[nslookup]]

## References

- Official documentation: https://developers.google.com/speed/public-dns/docs/using
- Related resources: RFC 8659 (CAA Records)
