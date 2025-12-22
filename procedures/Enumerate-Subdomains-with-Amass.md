---
id: 1cc9186d-3b66-4a65-bc03-abe748d83789
type: procedure
verified: true
submitted: true
created_at: '2020-06-29T16:22:08.379970+00:00'
updated_at: '2023-05-26T00:41:17.136514+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - dns
  - subdomain
  - enumeration
  - osint
platforms:
  - Linux
commands:
  - '[[commands/amass-enumerate-subdomains-with-ip-resolution]]'
  - '[[commands/amass-enumerate-subdomains-with-custom-resolvers]]'
  - '[[commands/extract-domains-from-amass-output]]'
  - '[[commands/extract-ips-from-amass-output]]'
tools:
  - '[[tools/amass]]'
validated: true
---

# Enumerate-Subdomains-with-Amass

## Summary

This procedure leverages OWASP Amass to perform passive and active subdomain enumeration against a target domain, querying multiple OSINT sources like Certificate Transparency logs, search engines, and DNS datasets. It resolves IPs for discovered subdomains and outputs structured results, helping identify hidden assets for further reconnaissance.

## Description

Amass combines passive intelligence gathering (e.g., from VirusTotal, Shodan) with active DNS brute-forcing and alterations, storing results in a GraphDB for visualization if needed. Use it early in engagements to uncover subdomains revealing internal services, cloud buckets, or admin panels. Specify an output directory for logs; limit queries to avoid bans. Integrates well with custom resolvers for accuracy.

## Requirements

- Target domain name
- Amass installed (go-based, easy compile)
- Verified resolvers file (from Dnsvalidator)
- Internet access for API queries

## Defense

- Implement DNS query rate limiting and sinkholing
- Monitor for subdomain enumeration patterns in DNS logs
- Use certificate transparency monitoring to detect scraping

## Objectives

- Discover 10+ subdomains via multiple sources
- Resolve IPs for all valid subdomains
- Export clean lists of domains and IPs

## Instructions

### Step 1: Basic Enumeration with IP Resolution

**Context**: Perform standard enum using default sources, enabling IP resolution to immediately map hosts.

**Command** ([[commands/amass-enumerate-subdomains-with-ip-resolution]]):

```bash
amass enum -ip -d $_TARGET_DOMAIN -o $_OUTPUT_FILE
```

Queries sources like Crtsh, VirusTotal; outputs to file with subdomains and IPs.

### Step 2: Advanced Enumeration with Custom Resolvers

**Context**: Use validated resolvers and source filtering for faster, more accurate results; cap queries to control runtime.

**Command** ([[commands/amass-enumerate-subdomains-with-custom-resolvers]]):

```bash
amass enum -rf $_RESOLVERS_FILE -src -ip -d $_TARGET_DOMAIN -max-dns-queries $_MAX_QUERIES_NUM -o $_OUTPUT_FILE
```

-src enables passive sources only; use 25-100 resolvers and 20000 max queries.

### Step 3: Extract Domains

**Context**: Parse output to isolate subdomain names for further processing.

**Command** ([[commands/extract-domains-from-amass-output]]):

```bash
cat $_RESULTS_FILE | cut -d']' -f2 | awk '{print $1}' | sort -u > $_DOMAINS_FILE
```

Removes duplicates and formats cleanly.

### Step 4: Extract IPs

**Context**: Isolate resolved IPv4 addresses for port scanning.

**Command** ([[commands/extract-ips-from-amass-output]]):

```bash
cat $_RESULTS_FILE | cut -d']' -f2 | awk '{print $2}' | sort -u > $_IPS_FILE
```

Filters to unique IPs only.
