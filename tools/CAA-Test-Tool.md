---
url: 'https://caatest.co.uk/'
tags:
  - dns
  - caa
  - reconnaissance
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.596Z'
id: 94368a8e-07f8-4158-8c49-56ac21d3189d
validated: true
submitted: true
---
# CAA-Test-Tool

**Status**: Unverified

## Overview

The CAA Test Tool is an online service for performing DNS lookups specifically to view a domain's Certificate Authority Authorization (CAA) records, helping identify misconfigurations that could allow unauthorized certificate issuances.

## Description

This web-based tool queries DNS for CAA resource records (type 257), which specify which CAs are permitted to issue certificates for a domain. It's commonly used in offensive security for reconnaissance to spot domains without these protective records, as seen in vulnerability reports like the one for gratipay.com. The tool provides a simple interface for inputting a domain and retrieving results without requiring local installation.

## Features

- Feature 1: Direct DNS query for CAA records (RR type 257).
- Feature 2: Clear indication of missing records and potential risks.
- Feature 3: No authentication or setup needed; browser-based.

## Installation

### Requirements

- Web browser with internet access.

### Install Commands

No installation required; access via web.

## Basic Usage

Enter the target domain on the website to query.

### Common Options

| Option | Description |
|--------|-------------|
| Domain Input | Enter the domain to check (e.g., gratipay.com) |
| Submit | Trigger the DNS query |

## Examples

### Example 1: Basic Usage

1. Visit https://caatest.co.uk/.
2. Input "gratipay.com".
3. Submit to view CAA records.

### Example 2: Advanced Usage

Use for batch checking by scripting API if available, but primarily manual for single domains.

## Expected Output

A web page displaying DNS response, e.g., "No CAA records found for gratipay.com", confirming the absence.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to caatest.co.uk domains.
- DNS queries for type 257 from reconnaissance tools.

## Related Procedures

- [[procedures/Check-for-CAA-DNS-Records]]

## Related Tools


## References

- https://caatest.co.uk/
- RFC 8659: DNS Certification Authority Authorization (CAA) Resource Record
