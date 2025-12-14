---
tags:
  - dns
  - reconnaissance
  - cname
type: procedure
tools:
  - '[[tools/dig]]'
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
updated_at: '2025-12-14T04:38:39.875Z'
sub_techniques:
  - '[[Hardware]]'
id: 54f085b3-3ba0-4a13-9db8-ac124289af80
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Query-DNS-Records-with-Dig

## Summary

This procedure uses the dig command to query DNS records for a subdomain, revealing CNAME pointers to external services that may be vulnerable to takeover if unused.

## Description

DNS investigation is crucial in subdomain takeover scenarios. By querying records, attackers identify if a CNAME points to a third-party service like Brandpad.io that is no longer maintained, allowing subsequent claiming. This targets DNS infrastructures in web environments.

## Requirements

1. dig tool installed (part of bind-utils on Linux)
2. Network access for DNS queries
3. Target subdomain name

## Defense

Defensive measures and detection strategies:

- Use DNS monitoring tools to alert on dangling records
- Rotate or remove unused CNAMEs promptly
- Employ certificate transparency logs to detect unauthorized subdomain usage

## Objectives

1. Extract CNAME and other DNS records
2. Confirm misconfiguration for takeover potential
3. Document evidence for proof-of-concept

## Instructions

### Step 1: Perform DNS Query

**Context**: Run dig to fetch records for the target subdomain, focusing on CNAME.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig brand.zen.ly
```

> This queries the DNS nameserver and outputs records, including the CNAME to brandpad.io, confirming the dangling pointer.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques

- [[Hardware]] Gather Victim Host Information: DNS

## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[Reconnaissance]]
