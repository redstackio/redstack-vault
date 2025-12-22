---
id: tool-rapid7-fdns
name: Rapid7-FDNS-Dataset
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.650Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - recon
  - dns
url: >-
  https://www.rapid7.com/blog/post/2019/07/24/forward-dns-a-research-dataset-for-subdomain-enumeration/
validated: true
submitted: true
---

# Rapid7-FDNS-Dataset

**Status**: Unverified

## Overview

Rapid7's Forward DNS (FDNS) dataset is a passive reconnaissance tool providing a massive collection of DNS records for subdomain enumeration and identifying hijacking opportunities, commonly used in security research to map attack surfaces without active scanning.

## Description

The FDNS dataset is crawled periodically from global DNS resolvers, capturing forward lookups (domain to IP) in CSV format. It includes billions of records, enabling queries for specific domains like *.starbucks.bg to find subdomains pointing to cloud services. Ideal for offensive security to detect dangling records for takeovers, with no installation needed—just download and query.

## Features

- Feature 1: Comprehensive coverage of internet DNS records
- Feature 2: Timestamped data for historical analysis
- Feature 3: Free public access via Rapid7's open data initiative

## Installation

### Requirements

- Sufficient storage (datasets are GBs in size)
- Tools like gzip, grep for processing

### Install Commands

```bash
# No installation; download directly
wget https://datasets.powerdns.com/fdns/2023-01.csv.gz
```

## Basic Usage

```bash
zcat fdns-2023-01.csv.gz | head -5
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Dataset is file-based; use Unix tools for querying |

## Examples

### Example 1: Basic Usage

```bash
zcat fdns-2023-01.csv.gz | grep "starbucks.bg" | wc -l
```

### Example 2: Advanced Usage

```bash
zcat fdns-2023-01.csv.gz | awk -F',' '$1 ~ /starbucks/ {print $1}' > subdomains.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Rapid7 dataset hosts
- Large CSV downloads in logs
- Grep/awk processes on DNS files

## Related Procedures


## Related Tools

- [[tools/DNSdumpster]]
- [[tools/Sublist3r]]

## References

- Official documentation: https://www.rapid7.com/blog/post/2019/07/24/forward-dns-a-research-dataset-for-subdomain-enumeration/
- Related resources: PowerDNS datasets
