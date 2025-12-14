---
id: proc-004
tags:
  - recon
  - dns
  - domain-discovery
  - drupal
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-www-example]]'
  - '[[commands/dig-www-related]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:23:36.689Z'
sub_techniques:
  - '[[Hardware]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify-Related-Domains-with-DNS-Lookup

## Summary

This procedure performs DNS lookups on the target and related domains to confirm they resolve to the same IP, expanding the vulnerability scope.

## Description

After exploiting one domain, attackers check affiliates to identify shared hosting. Using dig for quick resolution helps map the attack surface without direct interaction. This is reconnaissance post-exploitation. Expected outcome: Matching IPs indicating same vulnerable host.

## Requirements

1. Access to DNS resolution tools
2. Known target domains
3. No special privileges needed

## Defense

Defensive measures and detection strategies:

- Monitor DNS queries for internal domains from external sources
- Use split DNS to obscure internal resolutions
- Implement domain shadowing protections

## Objectives

1. Discover related attack vectors
2. Confirm shared infrastructure
3. Broaden compromise potential

## Instructions

### Step 1: Resolve Primary Domain

**Context**: Get the IP for the exploited domain.

**Command** ([[commands/dig-www-example]]):
```bash
dig +short www.█████
```

> Short format DNS query. Expected output: IP like 192.0.2.1.

### Step 2: Resolve Related Domain

**Context**: Compare with another domain to check for same host.

**Command** ([[commands/dig-www-related]]):
```bash
dig +short www.██████████
```

> Expected output: Matching IP, confirming same server.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques

- [[Hardware]]

## Commands Used

- [[commands/dig-www-example]]
- [[commands/dig-www-related]]

## Tools Used

- [[tools/dig]]

## Tags

- reconnaissance
- dns
