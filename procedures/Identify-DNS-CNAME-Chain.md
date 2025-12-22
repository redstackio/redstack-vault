---
tags:
  - dns
  - reconnaissance
  - cname
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-query]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:26.670Z'
sub_techniques: []
id: 8fe998b3-c77f-46f2-ac4a-61508a4b4eeb
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-DNS-CNAME-Chain

## Summary

This procedure involves querying DNS records to identify CNAME chains for a target subdomain, revealing potential misconfigurations that could lead to subdomain takeovers.

## Description

In scenarios like the registry.nodejs.org vulnerability, attackers start by examining DNS to find abandoned subdomains pointing to third-party services like CDNs. This reconnaissance uncovers chains where the target subdomain is not properly configured downstream, enabling exploitation without DNS control. Expected outcomes include mapping the resolution path and spotting gaps in service protections.

## Requirements

1. Access to DNS resolution tools (e.g., dig installed on Linux/macOS)
2. Target subdomain name (e.g., registry.nodejs.org)
3. Internet connectivity for public DNS queries

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or automated scripts
- Implement DNS monitoring for changes and subdomain registrations
- Use CDN provider alerts for unauthorized domain additions

## Objectives

1. Map the DNS resolution chain for the target subdomain
2. Identify if it points to external infrastructure like Fastly
3. Flag potential takeover vectors for further investigation

## Instructions

### Step 1: Query CNAME Record

**Context**: Start by retrieving the CNAME for the target subdomain to see where it points.

**Command** ([[commands/dig-dns-query]]):
```bash
dig registry.nodejs.org CNAME
```

> This command queries authoritative DNS servers for the CNAME record. Expected output includes lines like "registry.nodejs.org. 3600 IN CNAME registry.npmjs.org." confirming the alias.

### Step 2: Validate Resolution

**Context**: Ensure the record is active and not expired.

**Command** ([[commands/dig-dns-query]]):
```bash
dig +trace registry.nodejs.org
```

> The +trace option shows the full delegation path. Look for the CNAME in the answer section to confirm it's resolving correctly.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-query]]

## Tools Used

- None

## Tags

- [[DNS]]
- [[Reconnaissance]]
