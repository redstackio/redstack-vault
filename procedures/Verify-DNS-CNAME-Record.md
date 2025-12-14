---
tags:
  - dns-lookup
  - cname
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-cname-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.364Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 71c0ed52-c74a-4ab6-87bb-eabc9e424483
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-DNS-CNAME-Record

## Summary

This procedure verifies DNS records for a suspected vulnerable subdomain to confirm the presence of a dangling CNAME pointing to a third-party service like unbouncepages.com, indicating potential takeover risk.

## Description

Once a subdomain is identified, query its DNS records to reveal CNAME entries. In the case of demo.greenhouse.io, a CNAME to unbouncepages.com without an active backing page creates a takeover opportunity. This step confirms the misconfiguration technically, allowing progression to exploitation.

## Requirements

1. DNS resolver access (e.g., public resolvers)
2. Command-line tools for DNS queries
3. Target subdomain name

## Defense

Defensive measures and detection strategies:

- Use DNS monitoring services to detect unresolved CNAMEs
- Automate scans for dangling records with tools like dnsdumpster
- Enforce DNS TTL policies for quick updates

## Objectives

1. Confirm CNAME configuration
2. Identify the pointed service
3. Validate dangling status

## Instructions

### Step 1: Query CNAME Record

**Context**: Perform a specific DNS lookup to retrieve CNAME details for the subdomain.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig CNAME demo.greenhouse.io
```

> This queries the authoritative DNS for the CNAME. Expected output: ;; ANSWER SECTION: demo.greenhouse.io. 3600 IN CNAME unbouncepages.com. Confirm if it resolves further or errors out.

### Step 2: Check Resolution Chain

**Context**: Follow the CNAME to verify if the target service is active.

**Command** ([[commands/dig-full-lookup]]):
```bash
dig demo.greenhouse.io +trace
```

> Trace the full resolution path. Expected output: Reveals if the chain ends in a non-existent or deleted resource on Unbounce.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/dig-cname-lookup]]
- [[commands/dig-full-lookup]]

## Tools Used


## Tags

- [[dns-query]]
- [[cname-verification]]
