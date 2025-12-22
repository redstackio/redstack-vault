---
tags:
  - dns
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.533Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e7303d05-9d6b-49d0-a14b-3a4ecf475f57
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-DNS-CNAME-to-Uberflip

## Summary

This procedure verifies if a subdomain's DNS CNAME record points to a vulnerable third-party service like Uberflip's read.uberflip.com, confirming takeover potential.

## Description

DNS CNAME records alias subdomains to external services for content hosting. If pointed to a service like Uberflip but unclaimed, attackers can register it. This step uses DNS queries to extract the alias target, targeting any DNS-resolved environment. Prerequisites include DNS resolution access. Outcome: Identification of the exact service endpoint for further research.

## Requirements

1. Access to DNS resolver (e.g., public DNS like 8.8.8.8)
2. Command-line DNS tool like dig
3. Target subdomain name

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs
- Remove unused subdomains or point to null
- Integrate with certificate monitoring tools

## Objectives

1. Extract CNAME record for the target subdomain
2. Confirm alias to a claimable service endpoint
3. Document the misconfiguration for reporting or exploitation

## Instructions

### Step 1: Query CNAME Record

**Context**: Use DNS lookup to retrieve the CNAME alias for the subdomain.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig CNAME resources.hackerone.com
```

> This queries the DNS for the CNAME record. Expected output includes 'resources.hackerone.com. 3600 IN CNAME read.uberflip.com.' confirming the alias. If no CNAME, the subdomain may not be vulnerable.

### Step 2: Resolve Further if Needed

**Context**: Optionally, resolve the target to check for additional details.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig read.uberflip.com
```

> Verifies the Uberflip endpoint's resolution. Success: Confirms service infrastructure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- None

## Tags

- [[DNS]]
- [[recon]]
