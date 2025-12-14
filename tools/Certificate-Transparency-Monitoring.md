---
url: 'https://crt.sh/'
tags:
  - certificate
  - transparency
  - recon
type: tool
platforms:
  - Web
  - Cloud
description: >-
  Method and tools for monitoring public certificate transparency logs to detect
  new SSL/TLS certificates and endpoints.
id: 023e7c72-fd78-449d-be8a-e757d384eeeb
created_at: '2025-12-14T17:32:39.210Z'
updated_at: '2025-12-14T17:32:39.210Z'
verified: false
validated: true
submitted: true
---
# Certificate Transparency Monitoring

**Status**: Unverified

## Overview

Certificate Transparency (CT) monitoring involves querying public logs of issued SSL/TLS certificates to discover new domains and endpoints in real-time, useful for reconnaissance in cloud environments like AWS.

## Description

CT logs are append-only records of certificates, accessible via services like crt.sh or Google's CT log servers. In offensive security, this detects newly created API endpoints (e.g., non-prod AWS subdomains) by filtering for recent issuances, enabling targeted probing without direct access.

## Features

- Feature 1: Real-time detection of new certificates
- Feature 2: Search by domain patterns (e.g., *.amazonaws.com)
- Feature 3: API access for automated monitoring

## Installation

### Requirements

- Web browser or API client (e.g., curl, Python requests)

### Install Commands

No installation; use online services or:

```bash
pip install certstream  # For streaming logs
```

## Basic Usage

Visit crt.sh and search for domains.

### Common Options

N/A for web UI; for API:

| Option | Description |
|--------|-------------|
| Query param | e.g., ?q=%.amazonaws.com&i=recent |

## Examples

### Example 1: Basic Usage

Browse https://crt.sh/?q=datazone.amazonaws.com

### Example 2: Advanced Usage

```bash
curl "https://crt.sh/?q=%.datazone.&output=json" | jq '.[] | select(.not_after > "$(date -d '1 day ago' +%Y-%m-%d)" )'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor outbound traffic to CT log servers (e.g., crt.sh)
- Log certificate issuance alerts in AWS
- Track queries for sensitive domains

## Related Procedures

- [[procedures/Monitor-Certificate-Transparency-for-New-AWS-Endpoints]]

## Related Tools

- [[tools/AWS-CLI]]

## References

- Official documentation: https://certificate.transparency.dev/
- crt.sh: https://crt.sh/
