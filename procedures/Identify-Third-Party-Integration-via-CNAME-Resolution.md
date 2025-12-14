---
id: p-cname-identify
tags:
  - cname
  - dns
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-resolve]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:31.511Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Third-Party Integration via CNAME Resolution

## Summary

This procedure involves querying DNS records to identify CNAME aliases that reveal third-party vendor integrations, which may inherit vulnerabilities from the pointed domain, as seen in the Twitter flightschool case.

## Description

In scenarios where subdomains use CNAME records to point to third-party services, attackers can uncover these integrations by performing DNS lookups. This step is crucial for identifying potential vulnerability inheritance, such as open redirects, without direct access to the target. The process targets public DNS and requires no authentication, focusing on domains like twitterflightschool.com to map out the attack surface.

## Requirements

1. Access to DNS resolution tools or command-line utilities like dig
2. Knowledge of the target domain (e.g., twitterflightschool.com)
3. Internet connectivity for public DNS queries

## Defense

Defensive measures and detection strategies:

- Monitor DNS queries for unusual reconnaissance patterns
- Use DNSSEC to validate CNAME records and prevent spoofing
- Regularly audit third-party CNAME configurations for inherited risks

## Objectives

1. Uncover third-party dependencies via DNS
2. Identify potential vectors for inherited vulnerabilities
3. Map the target's external integrations

## Instructions

### Step 1: Query CNAME Record

**Context**: Perform a DNS lookup to resolve the CNAME for the target subdomain, revealing the third-party vendor.

**Command** ([[commands/dig-resolve]]):
```bash
dig twitterflightschool.com CNAME
```

> This command queries the authoritative DNS server and outputs the CNAME alias, such as pointing to a vendor domain. Expected output includes the alias record confirming the integration.

### Step 2: Verify Resolution

**Context**: Confirm the CNAME points to an external vendor by tracing the full resolution chain.

**Command** ([[commands/dig-resolve]]):
```bash
dig +trace twitterflightschool.com
```

> Traces the DNS resolution path, showing the CNAME delegation. Success is indicated by the external vendor domain in the chain.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-resolve]]

## Tools Used

- None

## Tags

- [[cname]]
- [[DNS]]
- [[Reconnaissance]]
