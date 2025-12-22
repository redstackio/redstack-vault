---
url: 'https://www.domaintools.com/'
tags:
  - dns
  - whois
  - domain-lookup
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.785Z'
id: 7ab7c749-ee5a-48cc-b696-17b40957d45c
validated: true
submitted: true
---
# DomainTools

**Status**: Unverified

## Overview

DomainTools is a web-based platform for domain research, providing WHOIS lookups, DNS records, and domain availability checks, commonly used in security testing for identifying takeover opportunities.

## Description

DomainTools offers comprehensive domain intelligence, including historical WHOIS data, DNS resolution, and website screenshots. In offensive security, it's used to scout for dangling DNS records and unclaimed domains in subdomain takeover scenarios, such as verifying CNAME targets like recommendation.us.

## Features

- Feature 1: Real-time WHOIS queries for registration status
- Feature 2: DNS record enumeration (CNAME, NS, A records)
- Feature 3: Domain availability and ownership history

## Installation

### Requirements

- Web browser access
- Account for full features (free tier limited)

### Install Commands

No installation needed; access via web.

## Basic Usage

Access https://www.domaintools.com/ and use the search bar for queries.

### Common Options

| Option | Description |
|--------|-------------|
| WHOIS Search | Retrieve registration details |
| DNS Lookup | Resolve records like CNAME |
| Domain Profile | Full info including availability |

## Examples

### Example 1: Basic Usage

Search for "recommendation.us" in WHOIS to check availability.

### Example 2: Advanced Usage

Use DNS lookup for "recommendation.algolia.com" to get CNAME target.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to domaintools.com domains
- Query patterns in DNS logs for reconnaissance

## Related Procedures


## Related Tools

- [[WHOIS]]
- [[dnsdumpster]]

## References

- Official documentation: https://www.domaintools.com/support/
- Related resources: HackerOne reports on subdomain takeovers
