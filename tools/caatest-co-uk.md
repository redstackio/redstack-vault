---
id: tool-uuid-001
name: caatest-co-uk
type: tool
verified: false
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:36.536Z'
platforms:
  - Web
tags:
  - dns
  - caa
  - reconnaissance
url: 'https://caatest.co.uk'
validated: true
submitted: true
---

# caatest-co-uk

**Status**: Unverified

## Overview

caatest.co.uk is an online DNS lookup service specialized in testing and viewing Certificate Authority Authorization (CAA) records for domains, aiding in security assessments to identify misconfigurations that could lead to unauthorized certificate issuance.

## Description

This web-based tool queries public DNS for CAA resource records (type 257), displaying whether a domain has restrictions on which Certificate Authorities can issue certificates. It's commonly used in offensive security for reconnaissance to uncover vulnerabilities like those enabling phishing or MITM attacks via fake certificates. No installation is required; it's accessible via any web browser.

## Features

- Feature 1: Simple domain input for CAA record queries
- Feature 2: Clear display of record presence/absence and details
- Feature 3: No authentication or setup needed for basic use

## Installation

### Requirements

- Web browser (e.g., Chrome, Firefox)
- Internet connection

### Install Commands

No installation required; access directly via URL.

## Basic Usage

Visit https://caatest.co.uk/ and enter a domain name to query.

### Common Options

| Option | Description |
|--------|-------------|
| Domain Input | Enter the target domain (e.g., sifchain.finance) |
| Submit | Initiate the DNS query |

## Examples

### Example 1: Basic Usage

1. Go to https://caatest.co.uk/sifchain.finance
2. View results showing no CAA records.

### Example 2: Advanced Usage

Query multiple domains manually by entering each one sequentially; no batch option available.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Domain Properties]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to caatest.co.uk from assessment IPs
- DNS query logs showing type 257 requests

## Related Procedures

- [[procedures/Check-Domain-CAA-Records]]

## Related Tools

- [[dig]] (CLI DNS tool)
- [[nslookup]]

## References

- Official site: https://caatest.co.uk
- CAA RFC: https://datatracker.ietf.org/doc/html/rfc8659
