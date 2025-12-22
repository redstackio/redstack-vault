---
id: proc-uuid-003
tags:
  - dns-query
  - cname
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-query-cname]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T04:38:39.500Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Query-DNS-for-CNAME-Records

## Summary

This procedure uses DNS querying tools to retrieve CNAME records for a specific subdomain, identifying if it points to an unregistered TLD vulnerable to takeover.

## Description

By querying the A record of a subdomain, the response reveals underlying CNAMEs. In this case, the CNAME targets a domain with an unregistered TLD (e.g., .████), which is available for purchase, allowing an attacker to claim it and control the subdomain for malicious purposes like phishing.

## Requirements

1. Installed DNS tool like dig
2. Target subdomain name
3. Resolver access (port 53 open)

## Defense

Defensive measures and detection strategies:

- Audit all CNAME records to ensure targets are owned and active
- Use DNSSEC for integrity validation
- Scan for dangling records with automated tools

## Objectives

1. Retrieve DNS records for the subdomain
2. Identify exploitable CNAMEs
3. Confirm NXDOMAIN or similar indicators of takeover potential

## Instructions

### Step 1: Execute DNS Query

**Context**: Query the A record to uncover the CNAME chain.

**Command** ([[commands/dig-query-cname]]):

```bash
dig subdomain.example.com
```

> This command performs a DNS lookup, defaulting to IN A query. Expected output includes ANSWER SECTION with CNAME to unregistered TLD and NXDOMAIN status.

### Step 2: Parse Response

**Context**: Analyze the output for the CNAME target.

Inspect the response for the TLD in the CNAME value.

> Success: TLD noted as unregistered (e.g., .████ not in IANA list).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/dig-query-cname]]

## Tools Used

- [[tools/dig]]

## Tags

- [[dns-query]]
- [[cname]]
- [[subdomain-takeover]]
