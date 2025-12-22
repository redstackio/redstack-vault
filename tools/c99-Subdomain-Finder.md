---
url: 'https://subdomainfinder.c99.nl/'
tags:
  - recon
  - subdomain-enumeration
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.478Z'
id: cd3ad7b7-b844-445c-bee1-8619b1c9b097
validated: true
submitted: true
---
# c99 Subdomain Finder

**Status**: Unverified

## Overview

c99 Subdomain Finder is a free online tool for enumerating subdomains of a target domain, useful in reconnaissance for identifying potential vulnerabilities like dangling records in security testing.

## Description

This web-based scanner aggregates data from public sources to list subdomains, including DNS details, aiding in subdomain takeover detection by flagging unclaimed ones with third-party pointers.

## Features

- Feature 1: Instant subdomain listing for any domain
- Feature 2: DNS record display (CNAME, A, etc.)
- Feature 3: No installation required; browser-based

## Installation

### Requirements

- Web browser

### Install Commands

No installation needed; access via URL.

## Basic Usage

Visit https://subdomainfinder.c99.nl/ and enter target domain.

### Common Options

| Option | Description |
|--------|-------------|
| Target Domain Input | Enter domain like imgur.com |

## Examples

### Example 1: Basic Usage

Enter 'imgur.com' to get subdomain list including '8ybhy85kld9zp9xf84x6.imgur.com'.

### Example 2: Advanced Usage

Review results for CNAMEs pointing to verify.squarespace.com.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Web traffic to subdomainfinder.c99.nl from recon IPs
- No local indicators as it's online

## Related Procedures

- [[procedures/Enumerate-Subdomains-for-Dangling-Records]]

## Related Tools

- [[tools/dnsdumpster]]

## References

- Official site: https://subdomainfinder.c99.nl/
