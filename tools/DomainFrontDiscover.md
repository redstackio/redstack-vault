---
id: 6a7511c7-b1db-44e9-a333-1d3804e800cc
type: tool
verified: true
created_at: '2019-08-28T21:17:34.026504+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - reconnaissance
  - domain-fronting
  - cloudfront
  - aws
url: 'https://github.com/insidetrust/domainfrontdiscover'
validated: true
---

# DomainFrontDiscover

**Status**: Unverified

## Overview

DomainFrontDiscover is a set of Python scripts designed to identify AWS CloudFront domains that are suitable for domain fronting techniques. Domain fronting allows attackers to bypass network filters by using a legitimate domain in the SNI field while directing traffic to a different backend via the HTTP Host header. This tool is commonly used in red team operations for reconnaissance and evasion planning against censored or monitored networks.

## Description

The tool automates the discovery of CloudFront distributions by querying public AWS endpoints, certificate transparency logs, and other sources. It then tests these domains for fronting compatibility, helping security testers find viable proxies for command-and-control (C2) communications or data exfiltration. It supports both enumeration of potential domains and validation testing, outputting results in JSON for further analysis.

## Features

- Feature 1: Automated enumeration of CloudFront domains from public sources
- Feature 2: Testing for domain fronting viability using crafted HTTPS requests
- Feature 3: JSON output for integration with other tools like jq or custom scripts
- Feature 4: Verbose logging and timeout controls for reliable testing

## Installation

### Requirements

- Python 3.6+
- pip-installed dependencies: requests, certifi

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3 python3-pip -y
git clone https://github.com/insidetrust/domainfrontdiscover.git
cd domainfrontdiscover

# Install Python dependencies
pip3 install -r requirements.txt
```

## Basic Usage

```bash
python3 domainfrontdiscover.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v, --verbose` | Enable verbose output for debugging |
| `--timeout` | Set request timeout in seconds (default: 5) |

## Examples

### Example 1: Basic Usage

Enumerate CloudFront domains:

```bash
python3 domainfrontdiscover.py --enumerate --output domains.json
```

### Example 2: Advanced Usage

Test a specific domain for fronting:

```bash
python3 domainfrontdiscover.py --test --domain d123.cloudfront.net --sni legitimate.com --verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual queries to AWS APIs or certificate transparency logs from scanning IPs
- Detection method 2: High volume of HTTPS probes to CloudFront endpoints with mismatched SNI/Host
- Detection method 3: Presence of domainfrontdiscover.py or its dependencies in process lists

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Censys]]
- [[crt.sh]]

## References

- Official GitHub: https://github.com/insidetrust/domainfrontdiscover
- AWS CloudFront Documentation: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
- Domain Fronting Technique: https://cloudfront.net
