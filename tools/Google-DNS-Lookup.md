---
id: tool-uuid-456
url: 'https://dns.google.com/query'
tags:
  - dns
  - reconnaissance
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.164Z'
validated: true
submitted: true
---
# Google-DNS-Lookup

**Status**: Unverified

## Overview

Google DNS Lookup is a free, web-based service provided by Google for querying DNS records across various types, including CAA (type 257). It is commonly used in security testing for passive reconnaissance to identify configuration details like missing authorization records without requiring local installation.

## Description

This tool leverages Google's public DNS resolver (8.8.8.8) to perform authoritative queries on domain names. In offensive security, it helps detect weaknesses such as absent CAA records, which restrict certificate authorities for a domain. Users input parameters via a web interface, enabling quick checks for DNS misconfigurations that could lead to certificate misissuance risks. It supports DNSSEC validation for integrity.

## Features

- Feature 1: Supports querying any DNS record type, including obscure ones like 257 (CAA)
- Feature 2: DNSSEC validation to ensure response authenticity
- Feature 3: Short and long answers with trace options for debugging

## Installation

### Requirements

- Web browser (Chrome, Firefox, etc.)
- Internet connection

### Install Commands

No installation required; access via web.

## Basic Usage

Visit https://dns.google.com/query and enter domain, type, and options.

### Common Options

| Option | Description |
|--------|-------------|
| name | Target domain (e.g., hacker101.com) | 
| type | Record type (e.g., 257 for CAA) |
| dnssec | Enable DNSSEC validation (true/false) |

## Examples

### Example 1: Basic Usage

Query CAA for hacker101.com:

Access the site, set name=hacker101.com, type=257, dnssec=true, and submit.

### Example 2: Advanced Usage

Query with trace for full resolution path:

Set additional option edns_client_subnet for geolocation-aware queries if needed.

## Expected Output

JSON or formatted response showing answers, authority, and additional sections. For missing CAA: empty answers section with status like "NOERROR" but no records.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Log DNS queries to 8.8.8.8 from internal networks
- Detection method 2: Monitor for unusual type 257 queries in DNS traffic using Wireshark or SIEM

## Related Procedures


## Related Tools

- [[tools/Dig]]
- [[tools/Nslookup]]

## References

- Official documentation: https://developers.google.com/speed/public-dns/docs/dslookup
- Related resources: RFC 8659 for CAA records
