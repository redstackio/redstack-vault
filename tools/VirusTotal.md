---
id: tool-virustotal
url: 'https://www.virustotal.com'
tags:
  - reconnaissance
  - osint
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.424Z'
validated: true
submitted: true
---
# VirusTotal

**Status**: Unverified

## Overview

VirusTotal is a web-based service that analyzes files, URLs, domains, and IP addresses using multiple antivirus engines and provides insights into potential threats. In security testing, it's commonly used for OSINT to discover leaked data, malware indicators, and exposed endpoints associated with targets.

## Description

VirusTotal aggregates data from global scanners, user submissions, and web crawls to index URLs and domains. For offensive security, it excels in reconnaissance by revealing publicly shared links that may contain sensitive information, such as credential-embedded URLs. Features include domain relation graphs, URL listings, and historical data. It's free for basic use, with premium API access for automation.

## Features

- Feature 1: Domain and URL search with relation tabs showing linked endpoints
- Feature 2: File hashing and malware analysis for credential verification
- Feature 3: API integration for scripted queries

## Installation

### Requirements

- Web browser (no installation needed)
- Optional: API key for advanced use

### Install Commands

No installation required; access via web.

## Basic Usage

Navigate to https://www.virustotal.com and use the search bar.

### Common Options

| Option | Description |
|--------|-------------|
| Search Bar | Query domains, URLs, or hashes |
| Relations Tab | View associated URLs and IPs |
| Download Sample | Retrieve files for analysis |

## Examples

### Example 1: Basic Domain Search

Search for a domain to list associated URLs:

1. Go to https://www.virustotal.com
2. Enter "chaturbate.com" and select Domain.
3. Click "Relations" > "Urls" to browse.

### Example 2: Advanced Usage

Use the API for automated searches (requires key):

```bash
curl --request GET \
  --url 'https://www.virustotal.com/vtapi/v2/domain/report?apikey=YOUR_API_KEY&domain=chaturbate.com' \
  --header 'Accept: application/json'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Open Websites-Domains]] Search Open Technical Databases
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- API key leaks in logs
- High query volume from VirusTotal IPs
- User agent strings in web traffic

## Related Procedures


## Related Tools

- [[Shodan]]
- [[Censys]]

## References

- Official documentation: https://support.virustotal.com
- Related resources: VirusTotal API docs
