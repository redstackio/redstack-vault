---
tags:
  - reconnaissance
  - dns
  - subdomains
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.724Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 693bf7d3-524a-4092-ab3b-0245b3a51057
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Perform Domain Reconnaissance for Subdomains

## Summary

This procedure involves enumerating subdomains of a target domain to identify potential misconfigurations, such as those pointing to third-party services, as a precursor to subdomain takeover attacks.

## Description

In a subdomain takeover attack, the first step is reconnaissance to discover subdomains via DNS records. Attackers query public DNS for subdomains that may point to inactive resources on services like AWS S3 or Heroku. This reveals dangling records exploitable for takeover. The target environment is any domain with public DNS, and outcomes include a list of subdomains with their DNS details for further probing.

## Requirements

1. Internet access for DNS queries
2. Basic knowledge of DNS records (CNAME, A)
3. Tools like dig or nslookup

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling entries
- Implement DNS monitoring tools like DNSSEC or external scanners
- Use services like Subdomain Takeover scanners (e.g., dnsdumpster)

## Objectives

1. Discover all subdomains of the target
2. Identify third-party service pointers
3. Gather data for vulnerability assessment

## Instructions

### Step 1: Query DNS for Subdomain

**Context**: Start by performing a DNS lookup on suspected or enumerated subdomains to check their records.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig ███████.target.com
```

> This command queries the DNS server for the subdomain's record type, authority, and value. Look for CNAME records pointing to third-party domains like "inactive-bucket.s3.amazonaws.com". Expected output includes answer section with the record if it exists.

### Step 2: Enumerate Additional Subdomains if Needed

**Context**: If the specific subdomain is unknown, use brute-force or passive tools to list potential ones.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig @8.8.8.8 +short *.target.com
```

> This wildcard query helps discover subdomains. Filter results for third-party indicators.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[DNS]]
- [[subdomains]]
