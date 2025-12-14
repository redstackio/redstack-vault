---
id: proc-002
tags:
  - dns-recon
  - akamai
  - origin-ip
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup-for-origin-ip]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:29:57.325Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Hardware]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# DNS-Lookup-to-Identify-Origin-IP-Behind-Akamai

## Summary

This procedure uses DNS queries to trace the CNAME chain of the target domain, revealing the Akamai edge server and helping identify the internal origin IP for direct access.

## Description

Attackers perform reconnaissance on the target's DNS infrastructure to uncover backend servers hidden behind CDNs like Akamai. By querying A records, the CNAME chain exposes the load balancer setup. In this DoD application scenario, this leads to discovering the origin IP that lacks SSO enforcement. Expected outcomes include mapping the hosting setup and candidate IPs for further verification. Prerequisites: DNS resolution access and dig tool installed.

## Requirements

1. dig tool installed (part of BIND utilities)
2. Network access for DNS queries
3. Target domain name (e.g., ████)

## Defense

Defensive measures and detection strategies:

- Use DNSSEC to prevent zone walking
- Monitor DNS query logs for unusual patterns targeting CNAMEs
- Implement split DNS to hide internal records

## Objectives

1. Trace CNAME chain to Akamai
2. Identify potential origin IP
3. Gather infrastructure details for bypass

## Instructions

### Step 1: Query A Record

**Context**: This step resolves the target's A record to uncover the CNAME pointing to Akamai, indicating a load-balanced setup.

**Command** ([[commands/dig-dns-lookup-for-origin-ip]]):
```bash
dig A ████
```

> This command queries the IPv4 address for the domain, displaying the ANSWER SECTION with CNAMEs and Akamai IPs. Look for chains like domain CNAME akamai-edge.

**Expected Output**: ANSWER SECTION with CNAMEs such as ███. 2386 IN CNAME █████. and A record for Akamai edge server IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- [[Hardware]] DNS

## Commands Used

- [[commands/dig-dns-lookup-for-origin-ip]]

## Tools Used

- [[tools/dig]]

## Tags

- [[dns-recon]]
- [[akamai]]
- [[origin-ip]]
