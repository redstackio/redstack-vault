---
id: proc-dns-lookup-ubnt
tags:
  - dns
  - reconnaissance
  - cname
type: procedure
tools:
  - '[[tools/nslookup]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nslookup-dns-query-for-cname]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Org Information]]'
updated_at: '2025-12-14T17:31:43.071Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Org Information]]'
---
# DNS-Lookup-for-Subdomain-Enumeration

## Summary

This procedure uses DNS queries to enumerate subdomain configurations, identifying CNAME records that point to cloud services like AWS Cloudfront, which may indicate takeover vulnerabilities.

## Description

In the context of subdomain takeover attacks, perform a DNS lookup on target subdomains to reveal CNAME chains. For ping.ubnt.com, this uncovers a dangling pointer to an unclaimed Cloudfront distribution, setting the stage for exploitation. Prerequisites include public DNS access; no authentication needed.

## Requirements

1. Access to a DNS resolver like Google Public DNS (8.8.8.8)
2. Target subdomain name (e.g., ping.ubnt.com)
3. Command-line tools like nslookup

## Defense

Defensive measures and detection strategies:

- Monitor DNS records for dangling CNAMEs using tools like DNSdumpster or internal audits
- Implement automated alerts for unclaimed cloud resources via AWS Config

## Objectives

1. Identify CNAME chains pointing to cloud providers
2. Detect potential takeover vectors
3. Gather evidence for vulnerability verification

## Instructions

### Step 1: Query DNS for CNAME

**Context**: Resolve the target subdomain to expose its DNS record chain.

**Command** ([[commands/nslookup-dns-query-for-cname]]):
```bash
nslookup ping.ubnt.com 8.8.8.8
```

> This command queries Google's DNS server for ping.ubnt.com, outputting the CNAME chain and IP. Expected: Non-authoritative answer with CNAMEs to dl.ubnt.com and d2cnv2pop2xy4v.cloudfront.net.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Org Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/nslookup-dns-query-for-cname]]

## Tools Used

- [[tools/nslookup]]

## Tags

- dns
- reconnaissance
