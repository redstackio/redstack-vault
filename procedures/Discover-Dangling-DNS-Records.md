---
id: proc-001
name: Discover Dangling DNS Records
tags:
  - dns-recon
  - subdomain-enum
  - dangling-records
type: procedure
tools:
  - '[[tools/dnsrecon]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-lookup]]'
verified: false
platforms:
  - Cloud
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T05:32:31.200Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Discover Dangling DNS Records

## Summary

This procedure involves enumerating a target's DNS records to identify subdomains that point to non-existent or terminated cloud resources, such as a defunct AWS EC2 instance, setting the stage for potential subdomain takeover.

## Description

In scenarios like the 8x8.com vulnerability, replacing an EC2 instance without updating DNS leaves dangling records. Attackers perform passive and active reconnaissance on public DNS to find these, using tools to query records and check resolution. Prerequisites include public DNS access; no target credentials needed. Outcomes include a list of vulnerable subdomains exploitable for takeover.

## Requirements

1. Access to DNS resolution tools (e.g., dig, nslookup)
2. Wordlist for subdomain brute-forcing
3. Internet connectivity for public queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records with automated scripts to remove dangling entries
- Implement DNS monitoring tools like DNSSec or Cloudflare for anomaly detection
- Use CNAME flattening to obscure internal resources

## Objectives

1. Identify subdomains pointing to terminated resources
2. Verify non-responsiveness of resolved endpoints
3. Prepare for takeover validation

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Brute-force or passively discover subdomains associated with the target domain.

**Command** ([[commands/dig-lookup]]):
```bash
dig +short @8.8.8.8 ███████.8x8.com
```

> This queries Google's DNS for the subdomain's IP or CNAME. Expected output: An IP address or CNAME that does not resolve further, indicating a potential dangling record.

### Step 2: Scan for Dangling Records

**Context**: Use a specialized tool to perform comprehensive DNS reconnaissance and flag unresponsive records.

**Command** ([[commands/dnsrecon-brute]]):
```bash
dnsrecon -d 8x8.com -t brt -D /usr/share/wordlists/subdomains.txt -j output.json
```

> Parses results to check for records pointing to non-existent hosts. Expected output: JSON with subdomains and their status, highlighting those with errors like NXDOMAIN after resource termination.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/dig-lookup]]
- [[commands/dnsrecon-brute]]

## Tools Used

- [[tools/dnsrecon]]

## Tags

- [[dns-recon]]
- [[subdomain-enum]]
