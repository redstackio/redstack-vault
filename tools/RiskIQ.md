---
url: 'https://www.riskiq.com/'
tags:
  - threat-intel
  - breach-analysis
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.889Z'
id: b950f747-6f81-4573-b3d1-90f777686178
validated: true
submitted: true
---
# RiskIQ

**Status**: Unverified

## Overview

RiskIQ is a threat intelligence platform used for identifying and verifying breached accounts, particularly in social media attacks like this Twitter clickjacking incident.

## Description

RiskIQ provides digital footprint analysis, allowing security researchers to scan and identify thousands of infected Twitter accounts involved in viral propagation. It's commonly used in incident response to map breach scope.

## Features

- Feature 1: Account breach verification across platforms
- Feature 2: Threat actor tracking via infected profiles
- Feature 3: Integration with SIEM for alert correlation

## Installation

### Requirements

- Subscription to RiskIQ platform
- Web browser access

### Install Commands

No local install; SaaS-based.

```bash
# Access via web portal
```

## Basic Usage

```bash
# N/A - Web UI
```

### Common Options

| Option | Description |
|--------|-------------|
| Search | Query by username or domain |
| Export | Download breach data |

## Examples

### Example 1: Basic Usage

Search for infected Twitter accounts:

Browse to RiskIQ dashboard and query 'Twitter accounts with suspicious DM activity'.

### Example 2: Advanced Usage

Export list of 1,000+ verified breached accounts:

Use API or UI to filter by report tags like 'clickjacking'.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Open Websites-Domains]]
- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- API calls to RiskIQ endpoints
- Queries for known malicious domains

## Related Procedures


## Related Tools

- [[tools/Shodan]]
- [[tools/VirusTotal]]

## References

- Official documentation: https://www.riskiq.com/docs
- Related resources: HackerOne reports
