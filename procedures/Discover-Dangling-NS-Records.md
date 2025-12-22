---
id: 123e4567-e89b-12d3-a456-426614174001
name: Discover Dangling NS Records
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.339Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - dns
  - reconnaissance
  - subdomain-takeover
commands:
  - '[[commands/dig-dns-query]]'
platforms:
  - DNS
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---

# Discover Dangling NS Records

## Summary

This procedure identifies misconfigured DNS NS records for subdomains that point to unclaimed zones in cloud providers, enabling subdomain takeover opportunities. It is commonly used in reconnaissance phases to map attack surfaces.

## Description

In this scenario, the attack begins by querying DNS records for a target subdomain like us-east4.37signals.com. Dangling NS records occur when a subdomain's nameservers are set to point to a cloud-hosted zone (e.g., AWS Route 53) that was deleted or never properly configured, leaving it unclaimed. By discovering these, an attacker can claim the zone and control the subdomain's DNS, leading to impacts like hosting malicious content or exploiting shared cookies for account takeovers. Prerequisites include public DNS access and knowledge of common cloud providers.

## Requirements

1. Access to DNS resolution tools (e.g., dig installed on Linux/macOS)
2. Target subdomain name (e.g., us-east4.37signals.com)
3. Attacker account on suspected cloud providers for verification

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling NS entries using automated tools like DNS linter scripts
- Monitor for unauthorized zone claims in cloud provider logs (e.g., AWS CloudTrail)
- Implement DNSSEC to prevent unauthorized NS changes

## Objectives

1. Identify NS records pointing to unclaimed cloud zones
2. Verify zone availability for takeover
3. Gather evidence for potential exploitation

## Instructions

### Step 1: Query NS Records

**Context**: Use DNS lookup to retrieve nameservers for the target subdomain, checking for cloud provider indicators.

**Command** ([[commands/dig-dns-query]]):
```bash
dig NS us-east4.37signals.com
```

> This command queries the authoritative NS records. Look for output like "ns-xxx.awsdns-xx.com", indicating an AWS zone. Expected output includes a list of nameservers; if they match unclaimed patterns, proceed to verification.

### Step 2: Verify Zone Claim Status

**Context**: Manually check the cloud provider console (e.g., AWS Route 53) to see if the zone is available for registration.

**Command** (No CLI; UI action):

> Log into the provider account and search for the zone name derived from the NS records (e.g., nagli.us-east4.37signals.com). If unclaimed, it confirms the dangling state.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-query]]

## Tools Used

- None specific

## Tags

- [[DNS]]
- [[Reconnaissance]]
- [[subdomain-takeover]]
