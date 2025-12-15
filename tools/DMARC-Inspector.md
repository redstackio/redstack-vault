---
id: d4e5f6g7-h8i9-0123-defg-456789012345
url: 'https://dmarcian.com/dmarc-inspector/paragonie.com'
tags:
  - dmarc
  - dns
  - email-auth
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:59.001Z'
validated: true
submitted: true
---
# DMARC Inspector

**Status**: Unverified

## Overview

DMARC Inspector is an online tool for analyzing a domain's DMARC, SPF, and DKIM configurations by querying DNS TXT records, primarily used in security testing to identify email spoofing vulnerabilities.

## Description

This web-based utility from dmarcian allows users to input a domain and retrieve detailed reports on authentication records. It's ideal for offensive security to scout phishing opportunities via weak email policies, such as the missing DMARC on paragonie.com. Features include policy validation, alignment checks, and recommendations for compliance.

## Features

- Feature 1: DNS TXT record lookup for _dmarc, SPF, and DKIM
- Feature 2: Policy analysis (e.g., p=none, reject, quarantine)
- Feature 3: Reporting on authentication failure handling

## Installation

### Requirements

- Web browser with JavaScript enabled
- Internet connection

### Install Commands

No installation required; access via browser.

## Basic Usage

Enter domain in the search field on https://dmarcian.com/dmarc-inspector/.

### Common Options

| Option | Description |
|--------|-------------|
| Domain Input | Enter target domain (e.g., paragonie.com) |
| Analyze Button | Triggers DNS query and report generation |

## Examples

### Example 1: Basic Usage

1. Visit https://dmarcian.com/dmarc-inspector/
2. Enter "paragonie.com"
3. Click Analyze

### Example 2: Advanced Usage

Use for batch checking by scripting API if available, but typically manual for single domains.

## Expected Output

A report showing: "No DMARC record published" with details on SPF/DKIM status.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- DNS queries to _dmarc subdomains from reconnaissance IPs
- No direct detection as it's a passive web tool

## Related Procedures


## Related Tools

- [[MX Toolbox]]
- [[dig (DNS Lookup)]]

## References

- Official site: https://dmarcian.com/dmarc-inspector/
- DMARC.org documentation
