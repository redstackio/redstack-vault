---
tags:
  - dns
  - cname
  - reconnaissance
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/DomainTools]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:10.793Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1f732454-e5ff-4099-9d7c-a44e0a773ea4
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# DNS CNAME Enumeration for Subdomain Takeover

## Summary

This procedure involves querying DNS records to identify CNAME configurations for subdomains that point to external, unclaimed domains, setting the stage for subdomain takeover attacks.

## Description

In a subdomain takeover scenario, attackers scan for CNAME records aliasing company subdomains to third-party services. If the third-party domain lapses or is unclaimed, the attacker can register it and inherit control of the subdomain. This procedure focuses on enumerating the CNAME for a specific subdomain like recommendation.algolia.com, revealing a pointer to recommendation.us, which is available. Prerequisites include public DNS access; no authentication is needed. Expected outcomes include confirmation of a vulnerable alias, enabling further verification and exploitation.

## Requirements

1. Internet access for DNS queries
2. Access to a DNS lookup tool like DomainTools
3. Knowledge of the target subdomain

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using automated tools like dnsdumpster or subjack
- Monitor domain registrations for CNAME targets via WHOIS alerts
- Implement DNSSEC to prevent unauthorized takeovers

## Objectives

1. Discover misconfigured CNAME records
2. Identify potential takeover targets
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Query CNAME Record

**Context**: Perform a DNS lookup to resolve the CNAME for the target subdomain, identifying any external pointers.

Use [[tools/DomainTools]] to query:

Access the DomainTools DNS lookup interface and enter the subdomain (e.g., recommendation.algolia.com).

> This reveals the CNAME target, such as recommendation.us, indicating a potential vulnerability if unclaimed.

### Step 2: Analyze Record Details

**Context**: Review the resolved records for signs of misconfiguration, such as inactive or expired targets.

Examine the output from DomainTools for CNAME details, TTL, and any associated NS records.

> Expected output includes the full CNAME chain; success is confirmed if it points to a non-owned domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/DomainTools]]

## Tags

- [[DNS]]
- [[Reconnaissance]]
